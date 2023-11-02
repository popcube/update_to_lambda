import requests
import sys
import json

activate_url = "https://api.twitter.com/1.1/guest/activate.json"
bearer_token = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

header_test = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    # "Accept-Language": "en-US,en;q=0.9,ja;q=0.8"
    "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": 'guest_id_marketing=v1%3A169892750676421865; guest_id_ads=v1%3A169892750676421865; guest_id=v1%3A169892750676421865; personalization_id="v1_zzbjpr6MRgGPyM2+PGnxQw=="',
    "Origin": "https://twitter.com",
    "Referer": "https://twitter.com/",
    "Sec-Ch-Ua": '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Client-Transaction-Id": "SAbF6nkIF9rIOc2+1U6cfBbeExPJ/H3ahsDQPXZuNV39a6n1jmPVKjQZ2xg9NGa9wGt4vEirLauT/N3S1OcDiNBH8UXsSQ",
    "X-Twitter-Active-User": "yes",
    "X-Twitter-Client-Language": "en"
}
def main():
    header_dic = {
        "Authorization": "Bearer " + bearer_token
    }

    cookie_dic = {
        "guest_id_marketing": "v1%3A169892750676421865",
        "guest_id_ads": "v1%3A169892750676421865",
        "guest_id": "v1%3A169892750676421865",
        "personalization_id": '"v1_zzbjpr6MRgGPyM2+PGnxQw=="'
      }
    queries = {}

    # r = requests.post(activate_url, cookies={},
    #                  params=queries, headers=header_dic)
    r = requests.post(activate_url, headers=header_dic)
    
    if not r.ok:
        print("activate url post failed")
        sys.exit(1)

    # print(r.text)
    # print()
    # print(r.headers)
    # print(r.status_code)
    # print(r.content)

    
    gt = json.loads(r.text)["guest_token"]
    print(gt)

main()
