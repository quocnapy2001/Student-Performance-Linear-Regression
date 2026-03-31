from data_0 import df
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression

### Predictors & Target
X = df.drop("Performance Index", axis = 1)
y = df['Performance Index']

### Train Test-split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42
    )

### Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

### Cross-Validation:
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')

print(f"CV R² Scores: {cv_scores}")
print(f"Mean CV R²: {cv_scores.mean():.4f} ± {cv_scores.std():.4f}")

# Linear Formula
print("\nIntercept: ", model.intercept_)
print("\n")
print(list(zip(X_train.columns,model.coef_)))

### Regression Formula
print(
    f"\nRegression model is y = {model.intercept_:.2f} + "
    f"{model.coef_[0]:.2f} * Hours Studied + "
    f"{model.coef_[1]:.2f} * Previous Scores + "
    f"{model.coef_[2]:.2f} * Extracurricular Activities + "
    f"{model.coef_[3]:.2f} * Sleep Hours + "
    f"{model.coef_[4]:.2f} * Sample Question Papers Practiced"
)

### Make Prediction
y_pred = model.predict(X_test)