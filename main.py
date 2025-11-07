import boto3
import requests
import sys
import json
import os

activate_url = os.environ["ACTIVATE_URL"]
bearer_token = os.environ["BEARER_TOKEN"]

# extract gt from HTML text
def get_token_from_texts(token_name, r_text):
    token_index = r_text.find(token_name + "=")
    if token_index == 0: return ""
    token_end_index = r_text[token_index:].find(";")
    if token_end_index == -1: return ""
    return r_text[token_index+len(token_name)+1: token_end_index + token_index]

def main():
    gt = ""

    # header_dic = {
    #     "Authorization": "Bearer " + bearer_token
    # }
    header_dic = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "sec-ch-ua": "Google Chrome 122.0.0.0",
        "sec-ch-ua-arch": "Intel",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
    }
    r = requests.get(activate_url, headers=header_dic)

    if not r.ok:
        print("activate url get failed")
        print(r.status_code)
        # print(r.headers)
        print(r.text)
        sys.exit(1)
    
    try:
        # gt = json.loads(r.text)["guest_token"]
        gt = get_token_from_texts("gt", r.text)
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
