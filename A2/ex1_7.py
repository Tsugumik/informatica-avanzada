import numpy as np
import matplotlib.pyplot as plt

ts = np.array([float(l) for l in open("sales_series.txt", "r")])

predictions_3week = []
for i in range(3, len(ts)):
    mean_sales = np.mean(ts[i-3:i])
    predictions_3week.append(mean_sales)

predictions_7week = []
for i in range(7, len(ts)):
    mean_sales = np.mean(ts[i-7:i])
    predictions_7week.append(mean_sales)

weeks = np.arange(1, len(ts) + 1)

weeks_3week_pred = np.arange(4, len(ts) + 1)
weeks_7week_pred = np.arange(8, len(ts) + 1)

plt.figure(figsize=(12, 8))

plt.plot(weeks, ts, color='blue', marker='o', label='Actual Sales')
plt.plot(weeks_3week_pred, predictions_3week, color='green', marker='o', linestyle='--', label='3-Week Average Prediction')
plt.plot(weeks_7week_pred, predictions_7week, color='red', marker='o', linestyle='--', label='7-Week Average Prediction')

plt.title('Sales Predictions Based on Moving Averages')
plt.xlabel('Week Number')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()
