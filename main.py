import time
import requests

while True:
    api_url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
    response = requests.get(api_url, stream=True)
    try :
        for line in response.iter_lines():
            if line:
                print(line)
    except Exception as e:
        print("Error")

    time.sleep(1)