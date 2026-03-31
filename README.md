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
  
      CV R² Scores: [0.98871681, 0.98838426, 0.98891416, 0.98828704, 0.98900483]
      Mean CV R²: 0.9887 ± 0.0003
  
  - 5-fold cross-validation yielded a mean R² of 0.9887 ± 0.0003 across all folds, consistent with the test R² of 98.9%. The negligible standard deviation indicates the model is highly stable and its performance is not dependent on any particular train/test split, suggesting reliable generalisation. This stability justified proceeding with the full model interpretation.
  - While these figures are impressive, such consistency and high R² across all folds also reinforces the earlier conclusion that the dataset is likely synthetic or highly structured. In real-world data you would typically expect more variance between folds and a lower mean R². So the cross-validation confirms the model is well-fitted to this dataset, but does not necessarily guarantee the same performance on messier, real-world student data.

- **The fitted regression equation is:**

      y (Performance Index) =  -33.92 + 2.85 * Hours Studied + 1.02 * Previous Scores + 0.61 * Extracurricular Activities + 0.48 * Sleep Hours + 0.19 * Sample Question Papers Practiced
  
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

  - The residual vs fitted plot shows randomly scattered points with no discernible pattern around the zero line, confirming the assumptions of linearity and homoscedasticity. The consistent spread of residuals across all fitted values suggests the model performs equally well across the full range of predicted Performance Index scores. Although there appears to be a slight outlier around fitted value ~40 with a residual near -8, it is not concerning considering the overall 2000 test records.

## Compare with other models: 
      - Linear Regression: R² = 0.9890
      - Ridge: R² = 0.9890
      - Lasso: R² = 0.9868
      - Decision Tree: R² = 0.9762
- To contextualise the linear regression results, three alternative models were trained and evaluated on the same test set. Linear Regression and Ridge Regression achieved identical R² scores of 0.9890, suggesting minimal multicollinearity among predictors and confirming that regularisation was unnecessary
- Lasso Regression performed marginally lower at 0.9868, likely due to its tendency to shrink smaller coefficients toward zero, potentially penalising weaker predictors such as Sleep Hours and Sample Question Papers Practiced.
- The Decision Tree Regressor recorded the lowest R² of 0.9762, which is a meaningful result. Its relatively weaker performance on this dataset implies that the underlying relationships between predictors and Performance Index are predominantly linear, retrospectively validating the choice of linear regression as the most appropriate model.

## Conclusion:

