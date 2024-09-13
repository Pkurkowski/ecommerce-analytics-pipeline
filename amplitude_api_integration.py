AMPLITUDE_API_KEY = 'your_amplitude_api_key'
AMPLITUDE_API_URL = 'https://api2.amplitude.com/2/httpapi'

def send_event_to_amplitude(row):
    event_data = {
        'api_key': AMPLITUDE_API_KEY,
        'events': [{
            'user_id': row['session_id'],
            'event_type': row['event_name'],
            'time': row['event_timestamp'],
            'event_properties': {
                'product_category': row['product_category'],
                'cart_value': row['cart_value'],
                'referrer_url': row['referrer_url']
            }
        }]
    }
    response = requests.post(AMPLITUDE_API_URL, json=event_data)
    return response.status_code

# Send events to Amplitude
df.apply(send_event_to_amplitude, axis=1)
