## Project Link  Google Drive  :- https://drive.google.com/drive/folders/15CIi_Dn2LR77U_uCK_nmKY52T4ImPLR9?usp=sharing




# 💳 Microfinance Service Project: Presentation Outline
#
# Slide 1: Title Slide 🎯
Title	Microfinance Service Prediction: Risk and Uptake Analysis
Subtitle	Leveraging Telecom and Loan History Data for Binary Classification
Project Goal	Develop a machine learning model to predict Service Uptake/Default Risk among microfinance customers.

#Slide 2: Project Context & Objective 🧠
Title	Business Problem and Data Pipeline
Business Problem	A microfinance provider needs to accurately identify which customers are most likely to utilize a service or default on a small loan. This informs targeted marketing, pricing, and risk management.
Dataset Source	Customer behavioral data (e.g., telecom usage, loan history) spanning 30 and 90-day windows.
Target Variable	label (Binary Classification): 1 (Action/Target Customer) or 0 (No Action/Non-Target).
Key Metrics	F1-Score, AUC-ROC, and Precision/Recall. F1 is prioritized due to likely class imbalance.
Methodology	1. EDA & Cleaning → 2. Feature Engineering → 3. Imbalance Handling → 4. Model Training (Classification) → 5. Evaluation

# Slide 3: Exploratory Data Analysis (EDA) - Target & Imbalance 📊
Title	Target Variable Distribution: Addressing Imbalance
Insight	The target variable (label) is critical but is almost always imbalanced in financial/service uptake data (i.e., far more 0s than 1s).
Implication	Models trained on raw data will be biased toward predicting the majority class (0), leading to poor detection of the critical minority class (1).
Key Visualization 1	Bar Plot: Target Variable (label) Count
Instruction: Insert a bar chart (or count plot) clearly showing the count of '0' vs. '1'.
Data Structure	The dataset contains 37 features, including financial metrics (loan counts, amounts) and usage metrics (daily decrease in usage, rental charges) over 30 and 90 days.

#  Slide 4: EDA - Behavioral Feature Analysis 📈
Title	Bivariate Analysis of Key Predictors
Focus	Comparing the distribution of important numerical features between the two classes (label 0 vs. label 1).
Key Feature Group	Loan and Usage Metrics: Columns ending in 30 and 90 (e.g., daily_decr30, rental90, maxamnt_loans30).
Key Visualization 2	Box Plot / KDE Plot: daily_decr30 vs. label
Instruction: Insert a plot (e.g., a Box Plot or KDE plot) showing the distribution of daily decrease in usage over 30 days (daily_decr30) for customers with label=0 and label=1.
Expected Insight	Customers in the target class (1) are expected to show significantly different usage patterns (e.g., higher or more consistent activity) than non-target customers (0).

# Slide 5: Data Cleaning & Preprocessing ⚙️
Title	Data Preparation and Feature Handling
Feature Removal	Dropped irrelevant/unique identifier columns like msisdn, pcircle (if single value), and Unnamed: 0.
Handling Dates	pdate (Date of sanction) converted to numerical features (e.g., Days since epoch, Month, Day of Week) or was dropped if deemed irrelevant to loan prediction.
Handling Outliers/Skewness	Outliers in financial features (like daily_decr30) were likely handled using techniques like log transformation or clipping, as these features often have heavily skewed distributions.
Feature Scaling	Standardization (StandardScaler) or Normalization (MinMaxScaler) applied to numerical features for model compatibility.

# Slide 6: Feature Engineering 🧪
Title	Creating Predictive Ratio Features
Goal	Extract stable, predictive patterns by creating ratio and difference features between 30-day and 90-day metrics.
New Features Examples	* Usage\_Stability\_Ratio: daily_decr30 / daily_decr90 (Measures recent change in usage)
* Loan\_Continuity: amnt_loans30 / amnt_loans90 (Measures if loan amounts are stable or changing)
* AON\_Log: log(aon) (Used to normalize the distribution of 'Age On Network' for linearity)
Benefit	These ratio features are often less sensitive to absolute spend levels and better capture the rate of change in customer behavior, which is key for risk assessment.

# Slide 7: Addressing Class Imbalance
Title	Mitigating Bias: The Imbalance Problem
Problem	The severe imbalance (Slide 3) causes models to learn poorly from the minority class (1).
Solution (Likely Used)	Employed one or more of the following techniques:
* Oversampling (e.g., SMOTE): Artificially creates synthetic data points for the minority class.
* Undersampling (e.g., NearMiss): Reduces the number of majority class samples.
* Class Weighting: Assigns a higher penalty/weight to misclassifications of the minority class (e.g., in Logistic Regression or Tree Models).
Benefit	Ensures the model learns the distinguishing characteristics of the target customer group (label=1).

# Slide 8: Model Training & Selection 🤖
Title	Classifier Evaluation and Hyperparameter Tuning
Models Evaluated	Typically: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting (XGBoost/LightGBM).
Best Performer	[RANDOMFOREST CLASSIFIER ] (e.g., XGBoost, known for handling tabular data and imbalance well).
Tuning Strategy	Used GridSearchCV or RandomizedSearchCV with Cross-Validation to optimize parameters (e.g., n_estimators, max_depth, learning_rate).
Rationale	Ensemble methods (like Gradient Boosting or Random Forest) are generally chosen as they capture the non-linear relationship between usage patterns and risk better than linear models.

# Slide 9: Results and Model Evaluation ✅
Title	Final Performance and Business Impact
* AUC-ROC Score: [Insert Specific Value] (Measures the model's ability to distinguish between classes)
* F1-Score: [Insert Specific Value] (The harmonic mean of Precision and Recall, best for imbalanced data)
Key Visualization 3	Confusion Matrix (Test/Validation Set)
Instruction: Insert the confusion matrix plot. Highlight the True Positives (Correctly predicted targets) and False Negatives (Missed targets), as minimizing False Negatives is critical for business success.
Key Visualization 4	ROC Curve
Instruction: Insert the Receiver Operating Characteristic (ROC) curve plot. The area under the curve (AUC) should be high (closer to 1.0).e.

