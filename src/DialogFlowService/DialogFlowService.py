import json
import requests
from pprint import pprint


class DialogFlowService:
    def __init__(self):
        self.url = "https://api.dialogflow.com/v1/query?v=20150910"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR TOKEN"
        }

    def SendIntent(self, message):
        body: any = {
            "contexts": ["welcome", "recommender"],
            "lang": "pt",
            "query": message,
            "sessionId": "1",
            "timezone": "America/Buenos_Aires"
        }

        response = requests.post(
            self.url, data=json.dumps(body), headers=self.headers)

        data = json.loads(response.text)
        bot_response = data["result"]["fulfillment"]["speech"]

        pprint(data)

        return bot_response


# dfService = DialogFlowService()
# response = dfService.SendIntent("eae")
