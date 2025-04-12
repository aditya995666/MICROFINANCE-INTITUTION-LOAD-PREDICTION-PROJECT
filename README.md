## Project Link of Google Drive  :- https://drive.google.com/drive/folders/15CIi_Dn2LR77U_uCK_nmKY52T4ImPLR9?usp=sharing





# Project
Problem statement: A Microfinance Institution (MFI) is an organization that offers financial services to low income populations. MFS becomes very useful when targeting especially the unbanked poor families living in remote areas with not much sources of income. The Microfinance services (MFS) provided by MFI are Group Loans, Agricultural Loans, Individual Business Loans and so on. Many microfinance institutions (MFI), experts and donors are supporting the idea of using mobile financial services (MFS) which they feel are more convenient and efficient, and cost saving, than the traditional hightouch model used since long for the purpose of delivering microfinance services. Though, the MFI industry is primarily focusing on low income families and are very useful in such areas, the implementation of MFS has been uneven with both significant challenges and successes. Today, microfinance is widely accepted as a povertyreduction tool, representing $70 billion in outstanding loans and a global outreach of 200 million clients. We are working with one such client that is in the Telecom Industry. They are a fixed wireless telecommunications network provider. They have launched various products and have developed their business and organization based on the budget operator model, offering better products at Lower Prices to all valueconscious customers through a strategy of disruptive innovation that focuses on the subscribRecall and Precision.







## 📊 Slide 1: Title

Microfinance Service Analysis

## 📁 Slide 2: Dataset Overview
 📄 Dataset: Micro-credit-Data-file.csv

 🛠 Tools Used:  Pandas, NumPy, Matplotlib, Seaborn

 🎯 Goal: Predict microfinance client behavior using ML pipeline


## 🧹 Slide 3: Data Preprocessing

 🗑 Removed redundant/irrelevant columns

🧼 Cleaned and formatted data

📊 Used .describe() and .info() for statistical summary

## 📈 Slide 4: Exploratory Data Analysis (EDA)
🌡 Correlation Matrix with sns.heatmap()

📈 Distribution plots for age, loan_amount, income

🔢 Frequency check with value_counts()

📦 Outlier detection using boxplot

## ⚙️ Slide 5: Feature Engineering

🔤 Applied Label Encoding for categorical columns

🧮 Created new features from existing data


## 🏗 Slide 6: Model Building
🧪 Splitted dataset using train_test_split()

🤖 Algorithms Used:

 LogisticRegression
 SVM
 DecisionTreeClassifier
 RandomForestClassifier
 GradientBoostingClassifier
 XGBoostClassifier
 AdaboostClassifier

## 📊 Slide 7: Model Evaluation
✅ Accuracy Score

🧾 Classification Report

🔁 Confusion Matrix

## 🏁 Slide 8: Results & Insights

🥇 Best Model: RandomForestClassifier

📌 Accuracy Achieved: ~[88%-90%]

 PCA helped reduce noise & improved model stability

 ## 🌐 Slide 9: Streamlit Deployment
Deployment via Streamlit:

Created an interactive dashboard for model predictions and visualizations.

Used Streamlit to showcase predictions, accuracy scores, and insights in a user-friendly interface.

