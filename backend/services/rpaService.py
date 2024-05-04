import requests
import os
from dotenv import load_dotenv
load_dotenv() 

client_id = os.getenv('CLIENT_ID')
refresh_token = os.getenv('REFRESH_TOKEN')

def getToken(client_id, refresh_token):
    url = "https://account.uipath.com/oauth/token"
    payload = f"client_id={client_id}&refresh_token={refresh_token}&grant_type=refresh_token"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['access_token']

class RPAService:
    token = ''

    def __init__(self) -> None:
        self.token = getToken(client_id, refresh_token)

    def getProcess(self):
        url = "https://cloud.uipath.com/canthouniversity/DefaultTenant/orchestrator_/odata/Jobs"
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        response = requests.request("GET", url, headers=headers)
        return response.json()
    
    def runProcess(self, process_key, arguments):
        url = "https://cloud.uipath.com/canthouniversity/DefaultTenant/orchestrator_/odata/Jobs/UiPath.Server.Configuration.OData.StartJobs"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'X-UiPath-OrganizationUnitId': '5181513'
        }
        body = {
            "startInfo": {
                "ReleaseKey": process_key,
                "Strategy": "ModernJobsCount",
                "InputArguments": arguments
            }
        }
        print(headers)
        print(body)
        try:
            response = requests.request("POST", url, headers=headers, json=body)
            return response.json()
        except Exception as e:
            return e
