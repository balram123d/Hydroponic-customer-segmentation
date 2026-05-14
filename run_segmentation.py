import sys
import os
from src.segment import run_segmentation

# Run the segmentation
rfm_df, cluster_stats = run_segmentation()

# Print summary of customer segments
print("\n" + "="*60)
print("CUSTOMER SEGMENTATION SUMMARY")
print("="*60)

segment_counts = rfm_df['segment'].value_counts()

for segment in ['High Value', 'Loyal', 'At Risk', 'Inactive']:
    count = segment_counts.get(segment, 0)
    percentage = (count / len(rfm_df)) * 100
    print(f"{segment:<15} : {count:>6} customers ({percentage:>5.1f}%)")

print("="*60)
print(f"Total Customers  : {len(rfm_df):>6}")
print("="*60)

# Print segment details
print("\nSegment Details:")
print("-"*60)
for segment in ['High Value', 'Loyal', 'At Risk', 'Inactive']:
    segment_data = rfm_df[rfm_df['segment'] == segment][['recency', 'frequency', 'monetary']]
    if len(segment_data) > 0:
        print(f"\n{segment}:")
        print(f"  Avg Recency  (days since order): {segment_data['recency'].mean():.1f}")
        print(f"  Avg Frequency (# of orders)    : {segment_data['frequency'].mean():.1f}")
        print(f"  Avg Monetary (total spent)     : ${segment_data['monetary'].mean():.2f}")
