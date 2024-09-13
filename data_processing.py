import pandas as pd

# Load raw event data
df = pd.read_csv('ecommerce_event_data.csv')

# Create a dictionary of user actions
event_map = {
    'page_view': 'Viewed Page',
    'product_view': 'Viewed Product',
    'add_to_cart': 'Added to Cart',
    'purchase': 'Completed Purchase',
    'checkout_start': 'Started Checkout'
}

# Map event types to friendly names
df['event_name'] = df['event_type'].map(event_map)

# Convert event timestamps to readable format
df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])

# Aggregating conversion funnel data (simple example)
funnel = df[df['event_name'].isin(['Viewed Product', 'Added to Cart', 'Started Checkout', 'Completed Purchase'])]

# Group data by user session and calculate drop-off rates
funnel_summary = funnel.groupby(['session_id', 'event_name']).size().unstack(fill_value=0)
funnel_summary['add_to_cart_rate'] = (funnel_summary['Added to Cart'] / funnel_summary['Viewed Product']) * 100
funnel_summary['purchase_rate'] = (funnel_summary['Completed Purchase'] / funnel_summary['Started Checkout']) * 100

# Save processed data
funnel_summary.to_csv('processed_event_data.csv')

# Display the funnel summary
print(funnel_summary.head())
