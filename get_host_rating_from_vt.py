import requests
import base64

url_to_check_base64 = base64.urlsafe_b64encode("http://www.somedomain.com/this/is/my/url".encode()).decode().strip("=")
url = "https://www.virustotal.com/api/v3/urls/{}".format(url_to_check_base64)

headers = {
  "accept": "application/json",
  "x-apikey": "prKs'Nlh]E%/X{Wwv!69`~4:D3&dG>B$"
}

response = requests.get(url, headers=headers)
print(response.text)
