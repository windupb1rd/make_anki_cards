import requests, json


api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  # add a word to the end of the link


def search_a_word(query: str):
    result = []
    response = json.loads(requests.get(api+query).text)
    if type(response) == dict:
        if response['title'] == 'No Definitions Found':
            return False
            # return f"{response['title']}\n{response['message']}"
    else:
        result.append(response[0]['word'])  # 0 word
        result.append(response[0]['phonetic'])  # 1 transcription
        try:
            result.append(response[0]['meanings'][0]['definitions'][0]['definition'])  # 2 definition1
        except Exception:
            result.append('')
        try:
            result.append(response[0]['meanings'][0]['definitions'][0]['example'])  # 3 example for definition1
        except Exception:
            result.append('')
        try:
            result.append(response[0]['meanings'][0]['definitions'][1]['definition'])  # 4 definition2
        except Exception:
            result.append('')
        try:
            result.append(response[0]['meanings'][0]['definitions'][1]['example'])  # 5 example for definition2
        except Exception:
            result.append('')
        return result


# print(search_a_word(''))
# print(json.loads(requests.get(api+'run').text))
# print(result[0]['word'], result[0]['phonetic'])
