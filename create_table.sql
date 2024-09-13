CREATE TABLE ecommerce_events (
    event_id STRING,
    user_id STRING,
    event_type STRING,
    event_timestamp TIMESTAMP,
    product_id STRING,
    product_category STRING,
    session_id STRING,
    page_url STRING,
    referrer_url STRING,
    cart_value FLOAT
);
