import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f'Status code:{r.status_code}')
response_dict = r.json()
print(response_dict['total_count'])
repo_dicts = response_dict['items']

repo_links, stars, labels = [], [], []


for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)


    stars.append(repo_dict['stargazers_count'])
    # print(repo_dict['html_url'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)


print(labels)
# print(repo_dicts[0]['url'])


# 可视化
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels
}]

my_layout = {
    'title': 'Github上最受欢迎的项目',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
    }
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html', auto_open=False)


