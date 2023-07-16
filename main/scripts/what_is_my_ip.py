import requests

def get_info_by_ip():
        response = requests.get(url='http://ip-api.com/json/').json()
        data = {
            'IP': response.get('query'),
            'City': response.get('city'),
        }
        return data

print(get_info_by_ip())