import requests, json


api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  # add a word to the end of the link


def search_a_word(query: str):
    result = {}
    response = json.loads(requests.get(api+query).text)
    if type(response) == dict:
        if response['title'] == 'No Definitions Found':
            return False
    else:
        result['word'] = response[0]['word']  # 0 word
        result['transcription'] = response[0]['phonetic']  # 1 transcription
        for i in range(5):
            try:
                result[f'definition{i}'] = response[0]['meanings'][0]['definitions'][i]['definition']
            except Exception:
                result[f'definition{i}'] = None
            try:
                result[f'example{i}'] = response[0]['meanings'][0]['definitions'][i]['example']
            except Exception:
                result[f'example{i}'] = None
        return result


# print(search_a_word('run'))
# print(json.loads(requests.get(api+'run').text))
# print(result[0]['word'], result[0]['phonetic'])
