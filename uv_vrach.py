import requests
url = "http://10.0.1.179/PatNotes/Flag"

START = "2018-02-28"
END = "2018-02-28"

querystring = {"date":["ge"+START,"le"+END]}

payload = ""
headers = {
    'content-type': "application/json",
    'authorization': "N3 1B0ADEB6-58E8-440D-B83E-BB63657CC2D5"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)