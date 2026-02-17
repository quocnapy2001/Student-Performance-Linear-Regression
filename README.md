# Student-Performance-Linear-Regression

AIM: This project is for study purpose with the goal to utilises supervised learning such as linear regression to predict student perfromance based on academic and behavioural predictors.

STEP: 
- Load the dataset
- Visualize relationships between variables
- Select features and target variable
- Split data into training and testing sets
- Train a linear regression model
- Interpret model coefficients
- Generate predictions on test data
- Evaluate model performance
- Encode categorical variables
- Retrain and compare models

DATA:
- Description: The Student Performance Dataset is a dataset designed to examine the factors influencing academic student performance. The dataset consists of 10,000 student records, with each record containing information about various predictors and a performance index.
- Features:
  + Hours Studied: The total number of hours spent studying by each student.
  + Previous Scores: The scores obtained by students in previous tests.
  + Extracurricular Activities: Whether the student participates in extracurricular activities (Yes or No).
  + Sleep Hours: The average number of hours of sleep the student had per day.
  + Sample Question Papers Practiced: The number of sample question papers the student practiced.
    
- What is the response aka labels?
  + Performance Index: A measure of the overall performance of each student.
  + The performance index represents the student's academic performance and has been rounded to the nearest integer. The index ranges from 10 to 100, with higher values indicating better performance.

- Why use regression? The response variable in this dataset is continuous => this is a regression problem


DATA INSPECTION:
<img width="1025" height="886" alt="image" src="https://github.com/user-attachments/assets/0fdfbef6-fcf3-40ee-b254-be67c56bf803" />

- Previous Scores is a very strong predictor of Performance Index and might be the strongest predictor.
- Hours Studied and Sample Question Papers Practiced are also positively correlated with performance.
- Sleep Hours shows weak relationship.
- Extracurricular Activities shows no clear relationship => may still have small impact.
- Performance Index distribution is normal => Linear regression is appropriate.

LINEAR REGRESSION:
- Formula: PerformanceIndex=𝛽0+𝛽1×PreviousScores+𝛽2×SleepHours+𝛽3×SampleQuestionPapersPracticed + 𝛽4xExtracurricularActivities
- y is 
