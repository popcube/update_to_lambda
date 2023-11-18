import boto3
import requests
import sys
import json
import os

client = boto3.client('lambda')

activate_url = os.environ["ACTIVATE_URL"]
bearer_token = os.environ["BEARER_TOKEN"]

def main():
    gt = ""

    header_dic = {
        "Authorization": "Bearer " + bearer_token
    }
    r = requests.post(activate_url, headers=header_dic)

    if not r.ok:
        print("activate url post failed")
        print(r.status_code)
        # print(r.headers)
        print(r.text)
        sys.exit(1)
    
    try:
        gt = json.loads(r.text)["guest_token"]
    except Exception as e:
        print("gt was not included in reponse from activate url")
        print()
        print(e)
    print("gt: " + gt)

    client.update_function_configuration(
        FunctionName='Twitter_frontend_multi_acc_dynamodb',
        Environment={
            'Variables': {
                'x_gt': gt
            }
        }
    )


main()
