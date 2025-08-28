# 📊 Customer Segmentation Dashboard

This project is an interactive Customer Segmentation System built with Python, Streamlit, and Plotly.  
It allows businesses to upload customer data, analyze purchasing behavior, and group customers into meaningful clusters using K-Means Clustering.

---

## 🚀 Features

- Upload your own dataset (CSV format)
- Automatic data cleaning and preprocessing
- Feature scaling using StandardScaler
- Apply K-Means clustering with adjustable number of clusters
- 2D Visualization of clusters using PCA
- Cluster profiling with average feature values
- Interactive bar charts and scatter plots using Plotly

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – for the interactive dashboard
- **Pandas, NumPy** – for data manipulation
- **Scikit-learn** – for clustering & preprocessing
- **Plotly Express** – for interactive visualizations

---

## 📂 Project Structure

```
├── customer_segmentation_dashboard.py   # Main Streamlit app
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── sample_dataset.csv                  # Example dataset (Mall Customers)
```

---

## 📦 Installation

**Clone this repository:**
```bash
git clone https://github.com/your-username/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard
```

**Create a virtual environment (recommended):**
```bash
python -m venv venv
# For Mac/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate
```

**Install required dependencies:**
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

**Run the Streamlit app:**
```bash
streamlit run customer_segmentation_dashboard.py
```

- Open your browser at [http://localhost:8501](http://localhost:8501)
- Upload a CSV file (e.g., Mall_Customers.csv)
- Select the number of clusters with the slider
- Explore customer segments through interactive charts

---

## 📊 Example Dataset

You can use the Mall Customers Dataset from Kaggle:  
🔗 [Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)

**Example columns:**
- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## 📸 Screenshots

*Dashboard Example*



---

## 📌 Future Improvements

- Add more clustering algorithms (DBSCAN, Hierarchical)
- Integrate predictive modeling (e.g., churn prediction)
- Deploy the app online with Streamlit Cloud / Heroku

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to contribute, feel free to fork this repo and submit a PR.

---

## 📄 License

This project
