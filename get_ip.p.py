import requests

def get_ip():
    url = 'http://httpbin.org/get'
    respond = requests.get(url)

    if respond.status_code == 200:
        json_data = respond.json()
        ip_address = json_data['origin']
        print(ip_address)
get_ip()