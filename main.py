import boto3
import requests
import sys
import json
import os

client = boto3.client('lambda')

activate_url = os.environ["ACTIVATE_URL"]
bearer_token = os.environ["BEARER_TOKEN"]
aws_f_name = os.environ["AWS_F_NAME"]

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
    print("length of gt: " + str(len(gt)))

    client.update_function_configuration(
        FunctionName=aws_f_name,
        Environment={
            'Variables': {
                'x_gt': gt
            }
        }
    )


main()
