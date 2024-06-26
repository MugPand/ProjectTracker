from bs4 import BeautifulSoup
import requests

username = 'MugPand'
base_url = 'https://github.com/' + username
repos_url = 'https://github.com/' + username + '?tab=repositories'

# extracts the (up to 6) pinned repos on user profile
def get_pinned_repos():
    response = requests.get(base_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        print("===========================================")

        pinned_repo_titles = soup.find_all("span", class_="repo")

        for repo in pinned_repo_titles:
            print(repo.get_text(strip=True))
            data.append([repo.get_text(strip=True)])

        print("===========================================")

        pinned_repo_descs = soup.find_all("p", class_="pinned-item-desc color-fg-muted text-small mt-2 mb-0")
        for idx, descs in enumerate(pinned_repo_descs):
            print(descs.get_text(strip=True))
            data[idx].append(descs.get_text(strip=True))

        return data
    else:
        print(f'Error: Unable to fetch the page. Status code {response.status_code}')

# extracts all public repos associated with a user
def get_all_repos():
    response = requests.get(repos_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        data = []

        print("===========================================")

        repo_titles = soup.find_all("a", itemprop="name codeRepository")
        for repo in repo_titles:
            #print(repo)
            desc_text = repo.get_text(strip=True)
            if desc_text == 'MugPand' or desc_text == 'Alz-Check': continue
            data.append([desc_text])
            # print(repo.get_text(strip=True))

        print("===========================================")

        repo_descs = soup.find_all("p", itemprop="description")
        for idx, title in enumerate(repo_descs):
            title_text = title.get_text(strip=True)
            data[idx].append(title_text)
            # print(title.get_text(strip=True))

        print(data)
        return data
    else:
        print(f'Error: Unable to fetch the page. Status code {response.status_code}')


unique_data = set()
data = get_all_repos()

# output data to files
with open('all_repos.txt', 'w') as f:
    for name, desc in data:
        f.write(name + ', ' + desc + '\n')
        unique_data.add((name, desc))

data = get_pinned_repos()

with open('pinned_repos.txt', 'w') as f:
    for name, desc in data:
        f.write(name + ', ' + desc + '\n')
        unique_data.add((name, desc))

with open('unique.txt', 'w') as f:
    for name, desc in unique_data:
        f.write(name + ', ' + desc + '\n')