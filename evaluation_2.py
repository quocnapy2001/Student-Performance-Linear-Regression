from linear_1 import X_test, y_test, y_pred, model
from sklearn import metrics
import matplotlib.pyplot as plt
from data_0 import sns


### R2 - Coeff of determination
r_squared = model.score(X_test, y_test)

### Adjusted R2
## Number of records in the test data
n = X_test.shape[0]     
## Number of predictor variables in the test set
p = X_test.shape[1]

adj_R2 = 1 - ((1-r_squared) * (n-1) / (n - p -1))
print(f"Adjusted R-Square is: {adj_R2:.2%}.")

### Mean Absolute Error (MAE)
mae = metrics.mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error (MAE) is: {mae:.2f}.")

### Mean Squared Error (MSE)
mse = metrics.mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (MSE) is: {mse:.2f}.")

### Root Mean Squared Error (RMSE)
rmse = metrics.mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error (RMSE) is: {rmse:.2f}.")

### Residual Plot
residuals = y_test - y_pred

plt.figure(figsize=(8, 5))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.3)
plt.axhline(0, color='red', linestyle='--', linewidth=1)
plt.xlabel("Fitted Values (Pred. Performance Index)")
plt.ylabel("Residuals")
plt.title("Residual vs Fitted Plot")
plt.tight_layout()
plt.show()