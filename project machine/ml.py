import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load the dataset
data = pd.read_csv(r"E:\Ai\Mastercard_stock_history.csv").drop(
    ["Dividends", "Stock Splits"], axis=1)  # Replace "mastercard_stock_data.csv" with your file name

# Convert Date column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Explore the data
print(data.head())
print(data.info())
print(data.describe())

# Visualize the data
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='High', data=data)
plt.title('Mastercard Stock Price (2006 - 2021)')
plt.xlabel('Date')
plt.ylabel('High Price (USD)')
plt.show()

# Feature Engineering
# data['Price_Range'] = data['High'] - data['Low']

# Handle missing values
data.dropna(inplace=True)

# Split data into features and target variable
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Preprocessing (if needed)

# Train Random Forest Regressor model
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
rf_model = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(
    estimator=rf_model, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print("Best Parameters:", best_params)

# Train the model with the best parameters
best_model = RandomForestRegressor(**best_params, random_state=42)
best_model.fit(X_train, y_train)

# Save the trained model
joblib.dump(best_model, "trained_model.pkl")

y_pred_train = best_model.predict(X_train)
train_mae = mean_absolute_error(y_train, y_pred_train)
train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
print("Training MAE:", train_mae)
print("Training RMSE:", train_rmse)

y_pred_test = best_model.predict(X_test)
test_mae = mean_absolute_error(y_test, y_pred_test)
test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
print("Testing MAE:", test_mae)
print("Testing RMSE:", test_rmse)
