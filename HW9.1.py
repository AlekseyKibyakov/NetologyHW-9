import requests
from pprint import pprint

def rate_by_intelligence(names):
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    list_of_chars = response.json()
    dict_of_chars = {}
    for char in list_of_chars:
        if char['name'] in names:
            dict_of_chars.setdefault(char['name'], char['powerstats']['intelligence'])
    max_intelligence = max(dict_of_chars.values())
    result_dict = {k: v for k, v in dict_of_chars.items() if v == max_intelligence}
    print(f'The smartest character: {result_dict}')

if __name__ == '__main__':
    rate_by_intelligence(['Captain America', 'Hulk', 'Thanos'])
