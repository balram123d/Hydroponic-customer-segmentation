# Hydroponic Customer Segmentation

K-Means clustering model that segments hydroponic retail customers using RFM analysis (Recency, Frequency, Monetary value). Built with Python, pandas, and scikit-learn. Transforms raw transaction data into actionable customer segments to support targeted marketing and retention strategy.

## Problem Statement

Hydroponic retail businesses struggle to identify and prioritize customers with the highest lifetime value. Without customer segmentation, marketing efforts are undifferentiated and retention strategies lack precision. This leads to:

- **Wasted marketing budget** on low-value customers
- **Missed opportunities** to upsell high-value customers
- **Poor resource allocation** for customer retention programs
- **Inability to tailor messaging** to different customer lifecycles

## Solution

This project uses **RFM (Recency, Frequency, Monetary) Analysis** combined with **K-Means Clustering** to automatically segment customers into four actionable groups:

- **High Value** - Recent, frequent purchasers with high spending
- **Loyal** - Recent customers with consistent purchase behavior
- **At Risk** - Previously active customers showing declining engagement
- **Inactive** - Customers with low engagement and spending

These segments enable data-driven decisions for targeted marketing campaigns, personalized retention efforts, and resource optimization.

## Tech Stack

- **Python 3.x**
- **pandas** - Data loading and manipulation
- **NumPy** - Numerical computations
- **scikit-learn** - StandardScaler, K-Means clustering

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Hydroponic-customer-segmentation
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the customer segmentation pipeline:

```bash
python run_segmentation.py
```

This will:
1. Load and clean the raw transaction data from `data/raw/`
2. Engineer RFM features from the transaction history
3. Scale features using StandardScaler
4. Apply K-Means clustering with 4 clusters
5. Label clusters based on RFM profiles
6. Save segmented customer data to `output/customer_segments.csv`
7. Print a summary table showing customer distribution across segments and their average RFM metrics

## Output

The script generates `output/customer_segments.csv` with columns:

- `customer_id` - Unique customer identifier
- `recency` - Days since last order (lower = more recent)
- `frequency` - Number of orders placed
- `monetary` - Total amount spent ($)
- `cluster` - K-Means cluster assignment (0-3)
- `segment` - Business segment label (High Value, Loyal, At Risk, Inactive)

## Business Segment Definitions & Recommendations

### High Value Customers
- **Profile**: Recent purchases, frequent orders, high spending
- **Business Actions**:
  - Premium VIP programs and exclusive early access to new products
  - Personalized outreach and concierge service
  - Cross-sell/upsell opportunities for premium products
  - Loyalty rewards to maximize lifetime value

### Loyal Customers
- **Profile**: Recent purchases, frequent orders (may have lower spend)
- **Business Actions**:
  - Frequency-based rewards and tiered loyalty programs
  - Bundled product offers to increase average order value
  - Community engagement and brand ambassadors
  - Exclusive content and early product launches

### At Risk Customers
- **Profile**: Declining activity (high recency) but previously engaged
- **Business Actions**:
  - Targeted win-back campaigns with special offers
  - Personalized re-engagement emails highlighting new products
  - Surveys to understand reasons for declining engagement
  - Limited-time incentives to reactivate purchases

### Inactive Customers
- **Profile**: Low engagement and low spending
- **Business Actions**:
  - Cost-effective email re-engagement campaigns
  - Clearance/promotional offers to test interest
  - Reactivation drip campaigns with emphasis on new features
  - Segment analysis to decide on further investment

## Project Structure

```
Hydroponic-customer-segmentation/
├── README.md
├── LICENSE
├── requirements.txt
├── run_segmentation.py
├── src/
│   └── segment.py
├── data/
│   └── raw/
│       └── Days since last order by customer last order date.csv
└── output/
    └── customer_segments.csv (generated after running)
```

## License

See LICENSE file for details.
