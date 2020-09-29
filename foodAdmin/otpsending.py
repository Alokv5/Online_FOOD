
import requests
import json

def sendASMS(contactno = "9506146168",message="Sorry Message not Available"):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno


    headers = {
        'authorization': "UVG44dY4hQ6e1Xxrl9F5jAO4IIhBsCE5CZU7qbd9b0acnV1dKE3OHyzTJwhw",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return json.loads(response.text)


 