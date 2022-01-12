import json
import urllib.request
import requests
import os


# код из документации к аддону для приложения anki. Аддон открывает порт на локалхосте для взаимодействия с приложением
# https://foosoft.net/projects/anki-connect/     документация
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
# ------------------------------------------------------


def download_audio(link_to_mp3, filename):
    media_folder = '/home/windupbird/snap/anki-woodrow/35/.local/share/Anki2/Aleksandr/collection.media'
    link = requests.get(link_to_mp3)
    open(os.path.join(media_folder, filename+'.mp3'), 'wb').write(link.content)
    return '[sound:'+filename+'.mp3]'


def add_card(wordcard):
    deck_to_add = 'my_deck'

    def unpack_tuples_of_context_examples(list_of_tuples, word):
        examples_unpacked = []
        for tup in list_of_tuples:
            examples_unpacked.append(' // '.join(list(tup)).replace(word, f'<b>{word}</b>')+'<br>')
        return examples_unpacked

    if deck_to_add not in invoke('deckNames'):
        config_id_from_other_deck = invoke('getDeckConfig', deck="400 Must - have words for the TOEFL")['id']
        invoke('createDeck', deck=deck_to_add)
        invoke('setDeckConfigId', decks=[deck_to_add], configId=config_id_from_other_deck)
    invoke('addNote', note={
            "deckName": deck_to_add,
            "modelName": "my_note_type",
            "fields": {
                "Term": f"{wordcard['word']}",
                "Transcription": f"[{wordcard['transcription']}]",
                "Translation": f"{', '.join(wordcard['reverso_translations'])}",
                "Definition": f"{'<br>'.join(wordcard['all_definitions'])}",
                "Context": f"{'<br>'.join(unpack_tuples_of_context_examples(wordcard['reverso_examples'], wordcard['word']))}",
                "Audio": f"{download_audio(wordcard['audio'], wordcard['word'])}",
            }})
    return f'The new card "{wordcard["word"]}" has been added to your deck "{deck_to_add}".'
