import json
from difflib import get_close_matches


def dictionary(key):
    data = json.load(open('data.json', 'r'))
    key = key.lower()
    if key in data:
        return data[key]
    elif len(get_close_matches(key, data.keys())) > 0:
        yn = input("did you mean %s instead! enter y if yes, or n if no:" % get_close_matches(key, data.keys())[0])
        if yn == 'y':
            return data[get_close_matches(key, data.keys())[0]]
        elif yn == 'n':
            return f'please double check the spelling of the word you just entered'
        else:
            return f'the input was not y or n'

    else:
        return f'The word does not exist.'


ukey = str(input())
print(dictionary(ukey))
