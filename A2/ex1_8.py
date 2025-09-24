import numpy as np

ts = np.array([float(l) for l in open("sales_series.txt", "r")])

def calculate_rmse(actual_values, predicted_values):
    actual_values = np.array(actual_values)
    predicted_values = np.array(predicted_values)

    squared_differences = (actual_values - predicted_values) ** 2

    mean_squared_error = np.mean(squared_differences)

    rmse = np.sqrt(mean_squared_error)

    return rmse


predictions_3week = []
for i in range(3, len(ts)):
    mean_sales = np.mean(ts[i - 3:i])
    predictions_3week.append(mean_sales)

actual_3week = ts[3:]

rmse_3week = calculate_rmse(actual_3week, predictions_3week)
print(f"RMSE for 3-week average predictions: {rmse_3week:.2f}")

predictions_7week = []
for i in range(7, len(ts)):
    mean_sales = np.mean(ts[i - 7:i])
    predictions_7week.append(mean_sales)

actual_7week = ts[7:]

rmse_7week = calculate_rmse(actual_7week, predictions_7week)
print(f"RMSE for 7-week average predictions: {rmse_7week:.2f}")
