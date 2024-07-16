import requests
import json

url = 'https://stream.wikimedia.org/v2/stream/recentchange'
response = requests.get(url, stream=True)

with open('recentchange.json', 'w') as file:
    for line in response.iter_lines():
        if line:
            line_str = line.decode('utf-8')
            if line_str.startswith("data: "):  # Only process lines that contain actual data
                json_str = line_str[6:]  # Remove the "data: " prefix
                try:
                    data = json.loads(json_str)
                    file.write(json.dumps(data) + '\n')
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e} - Line: {json_str}")
