import requests
import base64
import os
import json
import urllib.request


domain = "mx.meshify.io"
mailgunUrl = "https://api.mailgun.net/v3/domains/"+domain+"/messages/"
MailgunApiKey = os.environ.get("MailgunApiKey")


def handler(event, context):
    print("event")
    print(event)
    mailid = event["mailid"]

    auth = base64.b64encode('%s:%s' % 'api',MailgunApiKey)
    request = urllib.request.Request(mailgunUrl+mailid)
    request.add_header('Authorization','Basic '+auth)
    result = []
    with urllib.request.urlopen(request) as response:
        content = response.read()
        print(content)
        jsonPayload = json.loads(content)
        result.append(jsonPayload)
    return result
