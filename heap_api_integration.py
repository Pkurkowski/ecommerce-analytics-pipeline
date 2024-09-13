import requests

HEAP_APP_ID = 'your_heap_app_id'
HEAP_API_URL = 'https://heapanalytics.com/api/track'

# Load processed data
df = pd.read_csv('processed_event_data.csv')

def send_event_to_heap(row):
    event_data = {
        'app_id': HEAP_APP_ID,
        'identity': row['session_id'],
        'event': row['event_name'],
        'timestamp': row['event_timestamp'],
        'properties': {
            'product_category': row['product_category'],
            'cart_value': row['cart_value'],
            'referrer_url': row['referrer_url']
        }
    }
    response = requests.post(HEAP_API_URL, json=event_data)
    return response.status_code

# Send events to Heap
df.apply(send_event_to_heap, axis=1)
