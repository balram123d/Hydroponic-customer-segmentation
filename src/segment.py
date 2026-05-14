import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os


def run_segmentation():
    """
    Run customer segmentation analysis using RFM clustering.
    Returns the segmented dataframe and cluster statistics.
    """
    # Load data
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'customer_rfm_data.csv')
    df = pd.read_csv(data_path)

    # Clean data
    df = df.dropna()  # Remove rows with missing values

    # Drop duplicate columns
    df = df.loc[:, ~df.columns.duplicated()]

    # Select relevant columns for RFM and rename
    # Recency: Days since last order (lower is better, so we keep as-is)
    # Frequency: Customer number of orders
    # Monetary: Total amount spent
    rfm_df = df[['Customer ID', 'Days since last order', 'Customer number of orders', 'Total amount spent']].copy()
    rfm_df.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    # Prepare features for clustering
    X = rfm_df[['recency', 'frequency', 'monetary']].values

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Apply K-Means clustering with 4 clusters
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm_df['cluster'] = kmeans.fit_predict(X_scaled)

    # Calculate average RFM scores for each cluster
    cluster_stats = rfm_df.groupby('cluster')[['recency', 'frequency', 'monetary']].mean()

    # Label clusters based on RFM characteristics
    def label_cluster(cluster_id):
        avg_recency = cluster_stats.loc[cluster_id, 'recency']
        avg_frequency = cluster_stats.loc[cluster_id, 'frequency']
        avg_monetary = cluster_stats.loc[cluster_id, 'monetary']
        
        # Determine labels based on RFM profiles
        # High Value: Low recency (recent), high frequency, high monetary
        # Loyal: Low recency, high frequency (regardless of monetary)
        # At Risk: High recency with moderate frequency/monetary
        # Inactive: High recency, low frequency
        
        freq_median = rfm_df['frequency'].median()
        monetary_median = rfm_df['monetary'].median()
        recency_median = rfm_df['recency'].median()
        
        if avg_recency <= recency_median and avg_frequency >= freq_median and avg_monetary >= monetary_median:
            return 'High Value'
        elif avg_recency <= recency_median and avg_frequency >= freq_median:
            return 'Loyal'
        elif avg_recency > recency_median and avg_frequency >= freq_median:
            return 'At Risk'
        else:
            return 'Inactive'

    # Apply labels to dataframe
    rfm_df['segment'] = rfm_df['cluster'].apply(label_cluster)

    # Save results
    output_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'customer_segments.csv')
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rfm_df.to_csv(output_path, index=False)

    return rfm_df, cluster_stats


if __name__ == '__main__':
    rfm_df, cluster_stats = run_segmentation()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'output', 'customer_segments.csv')
    
    print(f"Segmentation complete! Results saved to {output_path}")
    print(f"\nCluster Statistics:")
    print(cluster_stats)
    print(f"\nSegment Distribution:")
    print(rfm_df['segment'].value_counts())
