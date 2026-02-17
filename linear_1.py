from data_0 import *
from sklearn.model_selection import train_test_split
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

print("\nIntercept: ", model.intercept_)
print("\n")
print(list(zip(X_train.columns,model.coef_)))

### Regression Formula
print("\nRegression model is y = ",
      model.intercept_,"+",
      model.coef_[0],"* Hours Studied +",
      model.coef_[1],"* Previous Scores +",
      model.coef_[2],"* Extracurricular Activities +",
      model.coef_[3],"* Sleep Hours +",
      model.coef_[3],"* Sample Question Papers Practiced",
      )

### Make Prediction
y_pred = model.predict(X_test)