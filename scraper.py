from bs4 import BeautifulSoup
import requests

base_url = 'https://github.com/MugPand'
repos = 'https://github.com/MugPand?tab=repositories'

response = requests.get(base_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.text
    print(f'Title: {title}')

    pinned_repo_descs = soup.find_all("p", class_="pinned-item-desc color-fg-muted text-small mt-2 mb-0")
    for repo in pinned_repo_descs:
        print(repo)

    pinned_repo_titles = soup.find_all("span", class_="repo")
    for title in pinned_repo_titles:
        print(title)

else:
    print(f'Error: Unable to fetch the page. Status code {response.status_code}')