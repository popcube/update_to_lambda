import boto3
import requests

client = boto3.client('lambda')


def get_token_from_texts(token_name, r_text):
    token_index = r_text.find(token_name + "=")
    return r_text[token_index+len(token_name + "="): r_text.find(";", token_index)]


def main():
    r = requests.get("https://twitter.com/elonmusk/status/1692431667548528661")

    if not r.ok:
        print("elonmusk")
        print(r.status_code)
        # print(r.headers)
        print(r.text)
        # sys.exit(1)

    gt = get_token_from_texts("gt", r.text)
    print("gt: " + gt)

    client.update_function_configuration(
        FunctionName='Twitter_frontend_multi_acc_dynamodb',
        Environment={
            'Variables': {
                'test_env': 'some_string'
            }
        }
    )


main()
