# 🎓 Student Score Predictor

This project aims to predict a student's **math score** based on various demographic and academic preparation attributes such as gender, lunch type, parental education level, and test preparation course.

## 🚀 Problem Statement

Student performance prediction has always been a valuable domain in educational data science. The objective of this project is to:

> **Predict the math score of a student** using their demographic details and academic background.

With accurate predictions, educators and stakeholders can:

- Identify students at risk.
- Customize learning plans.
- Make informed decisions to improve educational outcomes.

---

## 📊 Dataset Description

The dataset consists of the following features:

| Feature                       | Description                                             |
| ----------------------------- | ------------------------------------------------------- |
| `gender`                      | Gender of the student (`male` / `female`)               |
| `race_ethnicity`              | Group classification of the student                     |
| `parental_level_of_education` | Highest education level of the parents                  |
| `lunch`                       | Type of lunch provided (`standard` / `free/reduced`)    |
| `test_preparation_course`     | Whether the student completed a test preparation course |
| `math_score`                  | **Target** - Math score of the student                  |
| `reading_score`               | Reading score                                           |
| `writing_score`               | Writing score                                           |

The project focuses on **predicting `math_score`**.

---

## 🧠 Models Used

We experimented with multiple machine learning regression models:

- ✅ Linear Regression
- ✅ Decision Tree Regressor
- ✅ Random Forest Regressor
- ✅ Gradient Boosting Regressor
- ✅ K-Nearest Neighbors Regressor
- ✅ XGBoost Regressor
- ✅ CatBoost Regressor
- ✅ AdaBoost Regressor

All models were trained and evaluated using standard metrics such as **R² Score**, **MAE**, and **MSE**.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy, Matplotlib, Seaborn** (for EDA and data handling)
- **Scikit-learn** (for modeling and preprocessing)
- **XGBoost**, **CatBoost**, **LightGBM** (advanced boosting algorithms)
- **Joblib** (for model serialization)

---

## 📈 Results

After testing and comparing all models, the best-performing regressor was selected based on:

- Highest R² Score
- Lowest Mean Absolute Error (MAE)
- Generalization on test data

Model performance comparison charts and evaluation metrics are included in the notebook.

---

## 🔧 Project Structure
