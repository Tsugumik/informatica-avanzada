import numpy as np
import matplotlib.pyplot as plt
from ex1_8 import calculate_rmse

ts = np.array([float(l) for l in open("sales_series.txt", "r")])

rmse_values = []
avg_lengths = range(1, 11)

for k in avg_lengths:
    predictions = []
    for i in range(k, len(ts)):
        mean_sales = np.mean(ts[i - k:i])
        predictions.append(mean_sales)

    actual_values = ts[k:]

    if len(actual_values) > 0:
        error = calculate_rmse(actual_values, predictions)
        rmse_values.append(error)
    else:
        rmse_values.append(np.nan)

best_avg_length = avg_lengths[np.argmin(rmse_values)]
worst_avg_length = avg_lengths[np.argmax(rmse_values)]
print(f"The best average length is: {best_avg_length} with RMSE: {rmse_values[best_avg_length - 1]:.2f}")
print(f"The worst average length is: {worst_avg_length} with RMSE: {rmse_values[worst_avg_length - 1]:.2f}")


plt.figure(figsize=(10, 6))
plt.plot(avg_lengths, rmse_values, marker='o', linestyle='-')
plt.title('RMSE as a Function of Moving Average Length')
plt.xlabel('Length of Moving Average (k)')
plt.ylabel('RMSE')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 8))

predictions_best = []
for i in range(best_avg_length, len(ts)):
    mean_sales = np.mean(ts[i - best_avg_length:i])
    predictions_best.append(mean_sales)

predictions_worst = []
for i in range(worst_avg_length, len(ts)):
    mean_sales = np.mean(ts[i - worst_avg_length:i])
    predictions_worst.append(mean_sales)

plt.plot(np.arange(1, len(ts) + 1), ts, color='blue', marker='o', label='Actual Sales')

weeks_best = np.arange(best_avg_length + 1, len(ts) + 1)
plt.plot(weeks_best, predictions_best, color='green', marker='s', linestyle='--',
         label=f'Best Prediction ({best_avg_length}-week avg)')

weeks_worst = np.arange(worst_avg_length + 1, len(ts) + 1)
plt.plot(weeks_worst, predictions_worst, color='red', marker='^', linestyle=':',
         label=f'Worst Prediction ({worst_avg_length}-week avg)')

plt.title('Sales Predictions with Best and Worst-Performing Averages')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
