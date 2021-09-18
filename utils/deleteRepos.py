from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token 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",
    "X-OAuth-Scopes": "repo"
}

with open('repos.txt', 'r') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for l in urls:
    requests.delete(url=l, headers=headers)
    sleep(2)