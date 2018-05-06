import requests
import base64
import os
import json

domain = "mx.meshify.io"
mailgunUrl = "https://api.mailgun.net/v3/"+domain+"/messages"
MailgunApiKey = os.environ.get("MailgunApiKey")


def handler(event, context):
    print("event")
    print(event)
    return event
