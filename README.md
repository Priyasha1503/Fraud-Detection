🛡️ Fraud Detection System

A data-driven fraud detection project simulating how payment gateways monitor transactions in real-time to identify fraud.
This project demonstrates how exploratory data analysis (EDA), feature engineering, and visualization can reveal hidden fraud patterns before machine learning models even come into play.

📌 Features

📂 Dataset Cleaning & Preprocessing

Removed duplicates & missing values

Converted timestamps → Year, Month, Day

Encoded categorical features like Transaction_Type and Fraud

🔎 Feature Engineering

Extracted year & month trends for fraud monitoring

Classified transactions by type & channel

Built fraud vs non-fraud distribution insights

📊 Fraud Analysis & Visualization

Fraud percentage by year, month, and transaction type

Plotted anomaly spikes using Seaborn and Plotly

Fraud clusters around specific merchants/customers

🛠 Tech Stack

Python → Pandas, NumPy, Seaborn, Plotly

Jupyter Notebook for analysis

Matplotlib for trend visualization

⚙️ Installation

Clone the repo

git clone https://github.com/yourusername/Fraud-Detection-System.git
cd Fraud-Detection-System


Install dependencies

pip install -r requirements.txt


Run Jupyter Notebook

jupyter notebook

📂 Project Structure
Fraud-Detection-System/
│── data/
│   └── transactions.csv      # dataset
│── notebooks/
│   └── fraud_analysis.ipynb  # main notebook
│── src/
│   └── preprocessing.py      # data cleaning utils
│── README.md
│── requirements.txt

📈 Results

✔️ Identified fraudulent clusters with clear anomalies.
✔️ Fraud distribution: <2% of total transactions, but heavily concentrated in certain months/merchants.
✔️ Visual dashboards for fraud vs non-fraud transactions.

🚀 Future Scope

Add machine learning models (Logistic Regression, Random Forest, XGBoost) for predictive fraud detection.

Integrate real-time fraud alerts using streaming data (Kafka / Spark).

Enhance fraud patterns with geolocation & device-based features.

🏦 Why This Project?

Fraud detection in fintech is not just about algorithms — it’s about protecting people’s money.
This project builds the first layer of fraud monitoring used by banks & payment systems:
👉 rule-based anomaly detection + visualization, which then feeds into advanced ML-driven fraud detection systems.

🔗 Connect

👩‍💻 Author: Priyasha Sabbavarapu
📧 Email: priyashadevi@gmail.com

🔗 LinkedIn https://www.linkedin.com/in/priyasha1503/
