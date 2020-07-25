import requests
from bs4 import BeautifulSoup
import json
import time
headers = {
    'authority': 'www.reddit.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
}


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j]['subscribers'] < arr[j+1]['subscribers']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


x = [i.strip() for i in open("reddit.txt").readlines()]
subreddits = []
t = len(x)
i = 0
while i < t:
    s = x[i]
    name = s.split("/")[4]
    response = requests.get(s, headers=headers)
    likedictionary = json.loads(response.text)
    try:
        online = likedictionary['data']['accounts_active']
        subscribers = likedictionary['data']['subscribers']
    except KeyError:
        print("Key Error")
        time.sleep(5)
    subreddit = {'name': name, 'subscribers': subscribers, 'online': online}
    print(subreddit)
    subreddits.append(subreddit)
    i += 1
subreddits = bubbleSort(subreddits)
print(subreddits)
f = open('redditsorted.txt', 'w')
for s in subreddits:
    f.write(f"{s} \n")
f.close()
