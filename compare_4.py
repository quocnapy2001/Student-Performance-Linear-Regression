from sklearn.linear_model import Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from linear_1 import LinearRegression, X_train, X_test, y_train, y_test

models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=1.0),
    "Decision Tree": DecisionTreeRegressor(random_state=42)
}

for name, m in models.items():
    m.fit(X_train, y_train)
    score = m.score(X_test, y_test)
    print(f"{name}: R² = {score:.4f}")
