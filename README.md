# Student-Performance-Linear-Regression

## AIM: 
- This project is for study purpose with the goal to utilise supervised learning such as linear regression to predict student performance based on academic and behavioural predictors.

## STEP: 
- Load the dataset.
- Visualize relationships between variables.
- Select features and target variable.
- Split data into training and testing sets.
- Train a linear regression model.
- Interpret model coefficients.
- Generate predictions on test data.
- Evaluate model performance.
- Encode categorical variables.
- Retrain and compare models.

## DATA:
- **Description:** The Student Performance Dataset is a dataset designed to examine the factors influencing academic student performance. The dataset consists of 10,000 student records, with each record containing information about various predictors and a performance index.
- **Features:**
  + **Hours Studied:** The total number of hours spent studying by each student.
  + **Previous Scores:** The scores obtained by students in previous tests.
  + **Extracurricular Activities:** Whether the student participates in extracurricular activities (Yes or No).
  + **Sleep Hours:** The average number of hours of sleep the student had per day.
  + **Sample Question Papers Practiced:** The number of sample question papers the student practiced.
    
- **What is the response aka labels?****
  + **Performance Index:** A measure of the overall performance of each student.
  + The performance index represents the student's academic performance and has been rounded to the nearest integer. The index ranges from 10 to 100, with higher values indicating better performance.

- **Why use regression?** The response variable in this dataset is continuous => this is a regression problem.


## DATA INSPECTION:
<img width="1025" height="886" alt="image" src="https://github.com/user-attachments/assets/0fdfbef6-fcf3-40ee-b254-be67c56bf803" />

- Previous Scores is a very strong predictor of Performance Index and might be the strongest predictor.
- Hours Studied and Sample Question Papers Practiced are also positively correlated with performance.
- Sleep Hours shows weak relationship.
- Extracurricular Activities shows no clear relationship => may still have small impact.
- Performance Index distribution is normal => Linear regression is appropriate.

## LINEAR REGRESSION:
- **Formula:** y (Performance Index) =  -33.92 + 2.85 * Hours Studied + 1.02 * Previous Scores + 0.61 * Extracurricular Activities + 0.48 * Sleep Hours + 0.19 * Sample Question Papers Practiced
  
  - Hours Studied and Previous Scores have the largest positive impact on performance. Specifically, holding all other variables constant, a one-unit increase in Hours Studied is associated with an increase of 2.85 points in the Performance Index, while a one-unit increase in Previous Scores is associated with an increase of 1.02 points.
  - Extracurricular Activities is a binary variable (1 = Yes, 0 = No). The coefficient of 0.61 indicates that, on average, students who participate in extracurricular activities score approximately 0.61 points higher than those who do not, holding other factors constant.
- Overall, the model suggests that academic effort (Hours Studied) and prior ability (Previous Scores) are the most influential factors in predicting student performance.

## Evaluation Metrics:
  - **Adjusted R-Square:** 98.90%. => This shows an excellent model fit, indicating that the selected predictors explain nearly all variation in student performance.
  - **Mean Absolute Error (MAE):** 1.61. => This indicates that, on average, the model’s predictions deviate from the actual values by approximately 1.6 points.
  - **Mean Squared Error (MSE):** 4.08.
  - **Root Mean Squared Error (RMSE):** 2.02. =>  This shows very low prediction error, with predicted values typically within around 2 points of the actual performance scores.

## Conclusion:
- The results indicate that student performance can be predicted with a high degree of accuracy using the selected variables, particularly hours studied and previous scores.
- However, the exceptionally strong model performance is likely to reflect the structured and simplified nature of the dataset, and may not fully generalise to more complex real-world conditions.
