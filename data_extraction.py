import snowflake.connector
import pandas as pd

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

# Query to extract eCommerce event data
query = """
    SELECT event_id, user_id, event_type, event_timestamp, 
           product_id, product_category, session_id, page_url, referrer_url, cart_value
    FROM ecommerce_events
    WHERE event_timestamp >= CURRENT_DATE - INTERVAL '7 DAY';
"""

# Load data into a pandas DataFrame
df = pd.read_sql(query, conn)
conn.close()

# Display the data for verification
print(df.head())

# Save the data for further processing
df.to_csv('ecommerce_event_data.csv', index=False)
