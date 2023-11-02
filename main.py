import boto3
import requests
import sys
import json

client = boto3.client('lambda')

activate_url = "https://api.twitter.com/1.1/guest/activate.json"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

def main():
    gt = ""

    header_dic = {
        "Authorization": "Bearer " + bearer_token
    }
    r = requests.post(activate_url,headers=header_dic)

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
