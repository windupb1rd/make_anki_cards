import requests, json

import config

api = 'https://api.dictionaryapi.dev/api/v2/entries/en/'  # add a word to the end of the link
headers = {'Host': 'api.dictionaryapi.dev',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
'Connection': 'keep-alive',}

def search_a_word(query: str):
    result = {}
    all_definitions = []
    response = json.loads(requests.get(api+query, headers=headers).text)
    if type(response) == dict:
        if response['title'] == 'No Definitions Found':
            return False
    else:
        result['word'] = response[0]['word']  # 0 word
        try:
            result['transcription'] = response[0]['phonetic']  # 1 transcription
        except Exception:
            result['transcription'] = ''
        try:
            result['audio'] = response[0]['phonetics'][0]['audio'].replace('//ssl.', 'http://')
        except Exception:
            result['audio'] = ''
        for i in range(config.maximum_number_of_definitions_in_a_card):
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
