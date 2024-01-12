from bs4 import BeautifulSoup
import requests

base_url = 'https://github.com/MugPand'
repos_url = 'https://github.com/MugPand?tab=repositories'

def get_pinned_repos():
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.text
        print(f'Title: {title}')

        print("===========================================")

        pinned_repo_descs = soup.find_all("p", class_="pinned-item-desc color-fg-muted text-small mt-2 mb-0")
        for repo in pinned_repo_descs:
            print(repo.get_text(strip=True))

        print("===========================================")

        pinned_repo_titles = soup.find_all("span", class_="repo")
        for title in pinned_repo_titles:
            print(title.get_text(strip=True))
    else:
        print(f'Error: Unable to fetch the page. Status code {response.status_code}')

def get_all_repos():
    response = requests.get(repos_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.text
        print(f'Title: {title}')

        print("===========================================")

        repo_descs = soup.find_all("a", itemprop="name codeRepository")
        for repo in repo_descs:
            print(repo)
            # print(repo.get_text(strip=True))

        print("===========================================")

        repo_titles = soup.find_all("p", itemprop="description")
        for title in repo_titles:
            print(title.get_text(strip=True))

    else:
        print(f'Error: Unable to fetch the page. Status code {response.status_code}')

get_all_repos()