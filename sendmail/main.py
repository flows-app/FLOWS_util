import requests
import base64
import os
import json

domain = "mx.flows.app"
mailgunUrl = "https://api.mailgun.net/v3/"+domain+"/messages"
MailgunApiKey = os.environ.get("MailgunApiKey")


def handler(event, context):
    print("event")
    print(event)
    print("custom", context.client_context.custom)

    userid = context.client_context.custom['userid']
    flowname = context.client_context.custom['flowname']
    target = event['target']
    subject = event['subject']
    body = event['body']

    result = requests.post(mailgunUrl,
        auth=("api", MailgunApiKey),
        data={"from": "🤖 - "+flowname+" <bot@flows.app>",
              "to": [ target ],
              "subject": subject,
              "text": body
             }
        )
    print("response")
    print(result)
    print(result.text)
    return json.loads(result.text)
