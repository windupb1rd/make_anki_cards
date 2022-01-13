import requests, json


api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  # add a word to the end of the link


def search_a_word(query: str):
    result = {}
    all_definitions = []
    response = json.loads(requests.get(api+query).text)
    if type(response) == dict:
        if response['title'] == 'No Definitions Found':
            return False
    else:
        result['word'] = response[0]['word']  # 0 word
        result['transcription'] = response[0]['phonetic']  # 1 transcription
        try:
            result['audio'] = response[0]['phonetics'][0]['audio'].replace('//ssl.', 'http://')
        except Exception:
            result['audio'] = ''
        for i in range(5):
            try:
                result[f'definition{i}'] = response[0]['meanings'][0]['definitions'][i]['definition']
                all_definitions.append((f"{i+1}. "+response[0]['meanings'][0]['definitions'][i]['definition']))
            except Exception:
                result[f'definition{i}'] = None
            try:
                result[f'example{i}'] = response[0]['meanings'][0]['definitions'][i]['example']
            except Exception:
                result[f'example{i}'] = None
            result['all_definitions'] = all_definitions
        return result
