# 🚗 Car Price Prediction Web App

A complete **end-to-end Machine Learning project** that predicts the **price of a used car** based on multiple features such as car name, company, fuel type, year, and kilometers driven. The project includes **data cleaning, feature engineering, model training using Scikit-learn Pipelines**, and a **modern Streamlit web application** for real-time predictions.
<img width="1119" height="790" alt="Screenshot 2025-12-17 152831" src="https://github.com/user-attachments/assets/620fea9e-353a-4182-833d-07d598b5aa2c" />



---
# Link For the Model file : https://nbviewer.org/github/abhinavkumar1268b/Car-Price-Predictor/blob/main/car_price_predict/ml_model.ipynb

## 📌 Project Overview

Buying or selling a used car often involves uncertainty in pricing. This project solves that problem by using **machine learning** to estimate a fair car price based on historical data.

The project covers:

* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training with Pipeline
* Model Serialization (Pickle)
* Streamlit Web App
* Ready for Cloud Deployment

---

## 🧠 Machine Learning Workflow

1. **Data Cleaning**

   * Removed invalid values like *"Ask for Price"*
   * Converted text-based numeric columns to numbers
   * Handled missing values using median and most-frequent strategies

2. **Feature Engineering**

   * Extracted numeric values from `kms_driven`
   * One-Hot Encoded categorical columns:

     * `name`
     * `company`
     * `fuel`

3. **Model Building**

   * Used `ColumnTransformer` for preprocessing
   * Built an end-to-end `Pipeline`
   * Trained regression model for price prediction

4. **Evaluation**

   * Evaluated using **R² Score**
   * Cross-validated to ensure consistency

---

## 🏗️ Tech Stack Used

| Category         | Tools               |
| ---------------- | ------------------- |
| Language         | Python              |
| Data Analysis    | Pandas, NumPy       |
| Visualization    | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn        |
| Web App          | Streamlit           |
| Model Saving     | Pickle              |
| Version Control  | Git & GitHub        |

---

## 📂 Project Structure

```
car_price_predict/
│
├── model.pkl              # Trained ML pipeline
├── data.csv               # Dataset
├── notebook.ipynb         # EDA & Model Training
│
├── car_app/
│   ├── app.py              # Streamlit application
│   └── requirements.txt    # Project dependencies
│
└── README.md
```

---

## 🌐 Web Application Features

* Dropdown-based inputs (no manual typing)
* Modern UI with clean layout
* Real-time price prediction
* Error-safe input handling
* Uses trained ML pipeline directly (no reprocessing)

---

## 🚀 How to Run the Project Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/car-price-predictor.git
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📊 Model Input Features

| Feature | Description        |
| ------- | ------------------ |
| name    | Car model name     |
| company | Manufacturer       |
| year    | Manufacturing year |
| kms     | Kilometers driven  |
| fuel    | Fuel type          |

---

## ✅ Key Learnings

* Importance of **consistent feature names** between training and inference
* Using **Pipelines** to avoid data leakage
* Handling categorical variables with OneHotEncoder
* Building production-ready ML applications
* Debugging real-world ML deployment issues

---

## 📈 Future Improvements

* Add more regression models
* Improve UI with charts and confidence intervals
* Add database support
* Deploy on cloud with CI/CD

---

## 👤 Author

**Abhinav Kumar**
Aspiring Data Scientist & Machine Learning Engineer

---

⭐ If you like this project, don’t forget to give it a star on GitHub!
