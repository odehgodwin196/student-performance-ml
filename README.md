              Student Performance Prediction Using Machine Learning
              
1. Introduction

Educational institutions are constantly seeking ways to improve student academic performance. One approach is to analyze historical academic data and identify patterns that influence student success.

This project develops a machine learning model that predicts students' final exam scores (G3) using academic and socio-demographic features such as study time, number of past failures, parental education level, and class attendance.

By predicting student performance early, educators can provide targeted interventions to students who may be at risk of poor academic outcomes.

2. Problem Statement

Many schools lack tools to identify students who may perform poorly before final examinations.

Without early insights, students who struggle academically may not receive the necessary support in time.

This project aims to use machine learning techniques to predict student final exam scores, allowing educators to identify risk factors affecting student performance.

3. Objectives of the Study
General Objective

To develop a machine learning model capable of predicting student final exam scores based on academic and demographic features.

Specific Objectives

To preprocess and clean the student performance dataset

To explore relationships between student attributes and exam scores

To train multiple machine learning regression models

To evaluate and compare model performance

To build a predictive system that estimates students' final exam scores

4. Dataset Description

The dataset used in this project is the Student Performance Dataset, which contains academic records and background information about students.

The dataset includes features such as:

Feature	Description
age	Student age
studytime	Weekly study time
failures	Number of past class failures
absences	Number of school absences
G1	First period grade
G2	Second period grade
G3	Final exam grade
Medu	Mother's education level
Fedu	Father's education level
internet	Internet access at home

The target variable in this study is:

G3 — Final Exam Score

The goal of the model is to predict the value of this variable.

5. Data Preprocessing

Data preprocessing is an important step in machine learning because raw datasets often contain inconsistencies, missing values, or categorical variables that need transformation.

Several preprocessing steps were performed to prepare the dataset for model training.

5.1 Handling Missing Values

Missing values were checked using:

df.isna().sum()

Where missing values were present, appropriate strategies such as mean or mode imputation were applied depending on the data type.

5.2 Encoding Categorical Variables

Machine learning models require numerical input, therefore categorical variables were converted into numerical form.

This was achieved using one-hot encoding with the help of the pandas library.

Example categorical variables encoded include:

sex

address

parent occupation

subject

Binary variables such as internet access were mapped as:

yes → 1
no → 0
5.3 Feature Scaling

Feature scaling was performed using StandardScaler from scikit-learn.

Scaling ensures that numerical variables with different ranges do not disproportionately influence the model.

Examples of scaled features include:

age

studytime

failures

absences

G1

G2

6. Feature Selection

Feature selection was performed to reduce model complexity and prevent overfitting.

Only the most relevant features were used as input variables.

Selected features include:

G1

G2

studytime

failures

absences

Medu

Fedu

schoolsup

famsup

internet

sex_M

Target variable:

G3

7. Model Development

To determine the most effective model for predicting student exam scores, multiple regression algorithms were trained and compared.

The models used include:

Linear Regression

Random Forest Regressor

Gradient Boosting Regressor

These models were implemented using the scikit-learn.

Training multiple models allows comparison of their predictive performance.

8. Model Evaluation

The models were evaluated using the following performance metrics:

Metric	Description
MAE	Mean Absolute Error
RMSE	Root Mean Squared Error
R²	Coefficient of Determination

The evaluation results were:

Model	MAE	RMSE	R²
Linear Regression	0.958	1.725	0.807
Random Forest	0.997	1.811	0.787
Gradient Boosting	1.022	1.794	0.791

Based on these results, Linear Regression produced the best performance.

9. Model Interpretation

To better understand how the model makes predictions, explainable AI techniques were applied.

Feature importance analysis revealed that the most influential predictors of final exam performance include:

Second period grade (G2)

First period grade (G1)

Study time

Number of past failures

Absences

These findings suggest that previous academic performance strongly influences final exam results.

10. Deployment of the Model

To make the model accessible and interactive, a web-based dashboard was developed using Streamlit.

The application allows users to:

input student academic information

predict final exam scores

display predicted grades

provide recommendations for academic improvement

This interactive system demonstrates the practical application of machine learning in educational analytics.

11. Conclusion

This project demonstrated how machine learning can be used to predict student academic performance.

The results indicate that previous grades and study-related factors are strong indicators of final exam success.

Such predictive systems can assist educators in identifying students who may require additional academic support.

12. Future Work

Future improvements to this project may include:

incorporating larger educational datasets

applying deep learning models

developing a complete educational analytics dashboard

integrating classification models for pass/fail prediction
