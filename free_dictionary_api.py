import requests, json


api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  # add a word to the end of the link


def search_a_word(query):
    result = []
    response = json.loads(requests.get(api+query).text)
    if type(response) == dict:
        if response['title'] == 'No Definitions Found':
            return False
            # return f"{response['title']}\n{response['message']}"
    else:
        # result
        return response


# print(search_a_word(''))
# print(json.loads(requests.get(api+'snider').text))
# print(result[0]['word'], result[0]['phonetic'])
