import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=start'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)
print(f'Status code:{r.status_code}')
response_dict = r.json()
print(response_dict['total_count'])

repo_dicts = response_dict['items']
print(f"\nrepo:{len(repo_dicts)}")

repo_dict = repo_dicts[0]
# print(f"\nkeys:{len(repo_dict)}")
#
# # for i in sorted(repo_dict.keys()):
# #     print(i)
# print([i for i in sorted(repo_dict.keys())])
#
# for i in repo_dicts:
#     if i['name'] == "awesome-python":
#         print('1')
#         print(i['html_url'])


print(f"name:{repo_dict['name']}")
print(f"html_url:{repo_dict['html_url']}")


