import json
import urllib.request
import requests
import os


# код из документации к аддону для приложения anki. Аддон открывает порт на локалхосте для взаимодействия с приложением
# https://foosoft.net/projects/anki-connect/
def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']
# ----------


# invoke('createDeck', deck='test1')
# result = invoke('deckNames')
# print('got list of decks: {}'.format(result))


def download_audio(link_to_mp3, filename):
    media_folder = '/home/windupbird/snap/anki-woodrow/35/.local/share/Anki2/Aleksandr/collection.media'
    link = requests.get(link_to_mp3)
    open(os.path.join(media_folder, filename+'.mp3'), 'wb').write(link.content)
    return '[sound:'+filename+'.mp3]'


def add_card(wordcard):  # поля предварительно создаются в шаблоне карточек в anki
    if 'TEST' not in invoke('deckNames'):
        invoke('createDeck', deck='TEST')
    invoke('addNote', note={
            "deckName": "TEST",
            "modelName": "my_note_type",
            "fields": {
                "Term": f"{wordcard['word']}",
                "Transcription": f"[{wordcard['transcription']}]",
                "Translation": f"{(wordcard['reverso_translations'])}",
                "Definition": f"{wordcard['all_definitions']}",
                "Context": f"{wordcard['reverso_examples']}",
                "Audio": f"{download_audio(wordcard['audio'], wordcard['word'])}",  # звук пока не работает, так как аудио должны заранее находиться в папке с медиа. Но кнопка появляется
    }})
    return 'DONE'

# /home/windupbird/snap/anki-woodrow/35/.local/share/Anki2/Aleksandr/collection.media