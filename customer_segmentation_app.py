import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


st.title("📊 Customer Segmentation Dashboard")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.write(df.head())

   
    # Data Cleaning & Preprocessing
   
    if 'CustomerID' in df.columns:
        df.drop('CustomerID', axis=1, inplace=True)

    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    st.subheader("Cleaned Dataset")
    st.write(df.head())

    
    # Step 3: Feature Scaling
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    
    # Step 4: KMeans Clustering
    
    k = st.slider("Select Number of Clusters (K)", 2, 10, 4)
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = kmeans.fit_predict(scaled_data)

    st.subheader("Cluster Counts")
    st.write(df['Cluster'].value_counts())

    
    # Step 5: Dimensionality Reduction for Visualization
    
    pca = PCA(2)
    pca_data = pca.fit_transform(scaled_data)
    df['PCA1'] = pca_data[:,0]
    df['PCA2'] = pca_data[:,1]

    fig = px.scatter(df, x='PCA1', y='PCA2', color='Cluster',
                     title="Customer Segmentation (K-Means + PCA)",
                     template="plotly_dark", size_max=10)
    st.plotly_chart(fig)

    
    # Step 6: Cluster Profiling
    
    st.subheader("Cluster Profile")
    cluster_profile = df.groupby('Cluster').mean()
    st.write(cluster_profile)

    fig2 = px.bar(cluster_profile, barmode="group", title="Cluster Feature Averages")
    st.plotly_chart(fig2)

else:
    st.info("👆 Upload a CSV file to begin customer segmentation")
