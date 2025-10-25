import boto3
import requests
import sys
import json
import os

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
    print("length of gt: " + str(len(gt)))
    
    if os.environ.get("AWS_ACCESS_KEY_ID") and os.environ.get("AWS_SECRET_ACCESS_KEY") and os.environ.get("AWS_DEFAULT_REGION"):
        aws_f_name = os.environ["AWS_F_NAME"]
        client = boto3.client('lambda')
        client.update_function_configuration(
            FunctionName=aws_f_name,
            Environment={
                'Variables': {
                    'x_gt': gt
                }
            }
        )
    
    else:
        with open("./gt.txt", "w", encoding="utf-8") as f:
            f.write(gt)


main()
