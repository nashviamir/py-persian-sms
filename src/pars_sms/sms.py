import requests
import json
import re


class Response:
    
    def __init__(self, r):
        pattern = re.compile(r'(?<!^)(?=[A-Z])')

        if r.get("IsSuccessful"):
            for k, v in r.items():
                setattr(self, pattern.sub('_', k).lower(), v)

        else:
            raise Exception(r.get("Message"))


class Sms:

    base_url = "https://RestfulSms.com/api"

    def __init__(self, api_key, secret_key, line_number=None):
        self.api_key = api_key
        self.secret_key = secret_key
        self.line_number = line_number


    def _create_url(self, url):
        return f"{self.base_url}/{url}"


    def _extract_token_from_response(self, response):
        return response.token_key


    def get_token(self):
        url = self._create_url("token")
        headers = {
            "Content-Type" : "application/json"
        }
        payload = {
            "UserApiKey": self.api_key,
            "SecretKey": self.secret_key
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers).json()
        return self._extract_token_from_response(Response(r))


    def send(self, recipient, template=None, text=None, params=None):
        if template is None and text is None:
            raise Exception("template or text is required")
        
        if template is None:
            url = self._create_url("MessageSend")
            headers = {
                "Content-Type" : "application/json",
                "x-sms-ir-secure-token" : self.get_token()
            }

            payload = {
                "Messages":[text],
                "MobileNumbers": [recipient],
                "LineNumber": self.line_number,
                "CanContinueInCaseOfError": True
            }
            r = requests.post(url, data=json.dumps(payload), headers=headers).json()
            return Response(r)

        else:
            url = self._create_url("UltraFastSend/UserApiKey")
            headers = {
                "Content-Type" : "application/json"
            }
            paramschanged = [{"Parameter":key, "ParameterValue": value} for key, value in params.items()]

            payload = {
                "mobile" : recipient,
                "ParameterArray" : paramschanged,
                "TemplateId" : template,
                "UserApiKey": self.api_key,
                "SecretKey": self.secret_key
            }
            r = requests.post(url, data=json.dumps(payload), headers=headers).json()
            
            return Response(r)
            

    def send_bulk_sms(self, recipients, texts):
        url = self._create_url("MessageSend")
        headers = {
            "Content-Type" : "application/json",
            "x-sms-ir-secure-token" : self.get_token()
        }

        payload = {
            "Messages":texts,
            "MobileNumbers": recipients,
            "LineNumber": self.line_number,
            "CanContinueInCaseOfError": True
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers).json()
        return Response(r)



