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

- **Why use regression?** The response variable, Performance Index, is continuous and ranges from 10 to 100, making this a regression problem. The subsequent pairplot further supports this choice, as it reveals roughly linear relationships between the key predictors and the target variable.

## DATA INSPECTION:
<img width="1025" height="886" alt="image" src="https://github.com/user-attachments/assets/0fdfbef6-fcf3-40ee-b254-be67c56bf803" />

- Previous Scores shows the strongest linear relationship with Performance Index, as evidenced by the tight, upward-sloping scatter in the pairplot.
- Hours Studied and Sample Question Papers Practiced are moderately positively correlated with Performance Index, suggesting that academic effort and practice contribute meaningfully to performance, though less strongly than prior ability.
- Sleep Hours shows a weak positive relationship with Performance Index. Despite this, it is retained in the model as sleep is a theoretically meaningful factor in academic performance.
- Extracurricular Activities shows no visually distinct separation in the pairplot between Yes and No groups, suggesting a limited effect. However, it is included in the model to quantify this impact precisely.
- Performance Index follows an approximately normal distribution, which satisfies a key assumption of linear regression that residuals are normally distributed, making it an appropriate modelling choice.

## LINEAR REGRESSION:
- **Cross Validation:** 
  - CV R² Scores: [0.98871681, 0.98838426, 0.98891416, 0.98828704, 0.98900483]
  - Mean CV R²: 0.9887 ± 0.0003
  - 5-fold cross-validation yielded a mean R² of 0.9887 ± 0.0003 across all folds, consistent with the test R² of 98.9%. The negligible standard deviation indicates the model is highly stable and its performance is not dependent on any particular train/test split, suggesting reliable generalisation.

- **Formula:** y (Performance Index) =  -33.92 + 2.85 * Hours Studied + 1.02 * Previous Scores + 0.61 * Extracurricular Activities + 0.48 * Sleep Hours + 0.19 * Sample Question Papers Practiced
  
  - Hours Studied and Previous Scores have the largest positive impact on performance. Specifically, holding all other variables constant, a one-unit increase in Hours Studied is associated with an increase of 2.85 points in the Performance Index, while a one-unit increase in Previous Scores is associated with an increase of 1.02 points.
  - Extracurricular Activities is a binary variable (1 = Yes, 0 = No). The coefficient of 0.61 indicates that, on average, students who participate in extracurricular activities score approximately 0.61 points higher than those who do not, holding other factors constant.
  - Overall, the model suggests that academic effort (Hours Studied) and prior ability (Previous Scores) are the most influential factors in predicting student performance.

## Evaluation:
- **Metrics:**
  - **Adjusted R-Square:** 98.90%. => This shows an excellent model fit, indicating that the selected predictors explain nearly all variation in student performance.
  - **Mean Absolute Error (MAE):** 1.61. => This indicates that, on average, the model’s predictions deviate from the actual values by approximately 1.6 points.
  - **Mean Squared Error (MSE):** 4.08.
  - **Root Mean Squared Error (RMSE):** 2.02. =>  This shows very low prediction error, with predicted values typically within around 2 points of the actual performance scores.

- **Residuals Plot:**
  
<img width="567" height="352" alt="image" src="https://github.com/user-attachments/assets/713d0406-db6b-45b9-a55b-8aeec302cb27" />

  - The residual vs fitted plot shows randomly scattered points with no discernible pattern around the zero line, confirming the assumptions of linearity and homoscedasticity. The consistent spread of residuals across all fitted values suggests the model performs equally well across the full range of predicted Performance Index scores.


## Conclusion:
- The results indicate that student performance can be predicted with a high degree of accuracy using the selected variables, particularly hours studied and previous scores.
- However, the exceptionally strong model performance is likely to reflect the structured and simplified nature of the dataset, and may not fully generalise to more complex real-world conditions.
