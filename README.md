# 📦 Supply Chain Analysis using Machine Learning

A machine learning-based system for analyzing, modeling, and predicting revenue within the supply chain. It leverages powerful regression algorithms and rich feature engineering to extract business insights and support decision-making across inventory, production, logistics, and sales.

---

## 📈 Features

- 🔍 Automated Exploratory Data Analysis (EDA)
- 🧹 Robust Data Preprocessing and Feature Engineering
- 📊 Feature Selection using `SelectKBest`
- 🤖 Multiple Regressor Models:
  - Linear Regression
  - Random Forest
  - CatBoost
  - LightGBM
- 🛠️ Hyperparameter Tuning with `GridSearchCV`
- 📉 Residual and Prediction Analysis
- 🧠 Business Insights & Recommendations
- 💾 Model Export for Deployment (`.pkl`)

---
### 📌 Sample Visualizations

#### 🔧 Feature Importances (Random Forest)
![Feature Importances](images/feature_importance.png)

#### 🎯 Actual vs Predicted Revenue
![Actual vs Predicted](images/actual_vs_predicted.png)

#### 📉 Residuals Distribution
![Residuals](images/residuals_distribution.png)


---

## 📷 Suggested Plots to Export for `images/` Folder

You already generate the following — just **save them as images** in your script like this:

```python
plt.savefig('images/feature_importance.png')


