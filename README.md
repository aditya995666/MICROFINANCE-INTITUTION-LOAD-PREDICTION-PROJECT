## Project Link  Google Drive  :- https://drive.google.com/drive/folders/15CIi_Dn2LR77U_uCK_nmKY52T4ImPLR9?usp=sharing


# Slide 1: Title Slide
# Microfinance Service: Customer Churn Prediction


# Slide 2: Project Overview
Project Goal:

To build a machine learning model that can accurately predict customer churn for a micro-credit service.

Objectives:

Data Cleaning & Preparation: To process and clean the raw customer data to make it suitable for modeling.

Exploratory Data Analysis (EDA): To uncover insights and patterns related to customer behavior and churn.

Model Development: To train and evaluate multiple classification models to identify the best predictor of churn.

Handling Imbalance: To address the class imbalance in the dataset to ensure the model is not biased towards the majority class.

# Slide 3: Data Loading and Initial Exploration
Dataset:

The project uses a single dataset: Micro-credit-Data-file (1).csv.

Initial Data Profile:

Dimensions: The dataset contains 209,593 records and 37 features.

Content: Features include customer demographics (age on network), transactional data (recharge amounts, daily decrease), loan history (count and amount of loans), and payback behavior.

Target Variable: The label column (renamed to churn_label) indicates whether a customer is likely to churn.

# Slide 4: Data Cleaning and Preprocessing
Key Steps Performed:

Column Renaming: All columns were renamed to be more descriptive and understandable (e.g., aon to age_on_network_days).

Data Integrity Check: The dataset was checked for null values and duplicates. None were found, indicating good initial data quality.

Feature Dropping: The row_id column was dropped as it serves only as an index.

Data Type Conversion:

Object-type columns like customer_id and record_date were converted into numerical formats.

The customer_circle column was label-encoded to be used in the model.

# Slide 5: Exploratory Data Analysis (EDA) - Target Variable
Churn Label Distribution:

A count plot of the churn_label revealed a significant class imbalance.

The vast majority of customers are labeled as '1' (likely to churn/default), while a much smaller portion are labeled as '0'.

Implication:

This imbalance can bias the model, causing it to perform poorly on the minority class. This issue was addressed later using the SMOTE technique.

(A bar chart showing the imbalanced distribution of the 'churn_label' would be included here.)

# Slide 6: EDA - Data Distributions & Outliers
Analysis of Feature Distributions:

Distribution plots (distplots) were used to visualize the spread and skewness of various numerical features like age_on_network_days, avg_daily_decr_30d, and total_rental_30d.

Many features showed significant skewness and the presence of outliers.

Outlier Detection:

Box plots were generated for all numerical columns to visually identify data points lying far outside the typical range.

(Include examples of a distplot and a box plot from the notebook on this slide.)

# Slide 7: Outlier Treatment
Method:

Outliers were handled by removing values that fell outside the range defined by the Interquartile Range (IQR) method.

This process helps in creating a more robust model that is less sensitive to extreme values.

Impact:

After outlier removal, the shape of the dataset was reduced, leading to a cleaner and more representative sample for model training.

# Slide 8: Handling Class Imbalance with SMOTE
Problem:

As identified during EDA, the target variable was highly imbalanced.

Solution: SMOTE (Synthetic Minority Over-sampling Technique)

SMOTE was applied to the training data to balance the classes.

It works by creating synthetic samples of the minority class, thus providing the model with a more balanced view of the data. This helps prevent the model from simply predicting the majority class every time.

# Slide 9: Model Building
Machine Learning Models Used:

A variety of classification algorithms were trained to find the best performer:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

AdaBoost Classifier

Gradient Boosting Classifier

Process:

The dataset was split into features (X) and the target variable (y).

The data was then divided into training and testing sets (80/20 split).

Each model was trained on the SMOTE-balanced training data.

# Slide 10: Model Evaluation
Metrics Used:

The performance of each model was evaluated using standard classification metrics:

Accuracy: Overall correctness of the model.

Precision: The ratio of correctly predicted positive observations to the total predicted positives.

Recall: The ratio of correctly predicted positive observations to all observations in the actual class.

F1-Score: The weighted average of Precision and Recall.

Confusion Matrix: A table showing the performance of the classification model on a set of test data for which the true values are known.

(A sample Classification Report and Confusion Matrix from one of the models would be displayed here.)

# Slide 11: Results & Best Model
Performance Summary:

The classification reports for all models were analyzed to compare their performance.

The Random Forest Classifier and Gradient Boosting Classifier generally showed the highest F1-scores and a good balance between precision and recall, making them the top-performing models for this task.

# Conclusion:

Based on the evaluation, the Gradient Boosting Classifier was selected as the most suitable model for predicting customer churn.

Slide 12: Conclusion & Future Work
Summary of Findings:

The project successfully developed a model to predict customer churn using various user behavior features.

Data cleaning, outlier treatment, and handling class imbalance with SMOTE were critical steps for building an effective model.

Ensemble methods like Random Forest and Gradient Boosting proved to be the most effective for this classification problem.curve (AUC) should be high (closer to 1.0).e.

