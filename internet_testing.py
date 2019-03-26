import requests
import time

while True:
    try:
        r = requests.head("https://www.alexandroforte.com/")
        print(r.status_code)
    except requests.ConnectionError:
        print("failed to connect")
    time.sleep(10)
