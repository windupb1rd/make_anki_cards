import json
import urllib.request
import requests
import os
import card_style_and_deck_config


# https://foosoft.net/projects/anki-connect/
import config


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
    deck_to_add = config.deck_name

    def unpack_tuples_of_context_examples(list_of_tuples, word):
        examples_unpacked = []
        for tup in list_of_tuples:
            example_and_translation = list(tup)
            make_translation_cursive = '<i>'+example_and_translation.pop(1)+'</i>'
            example_and_translation.append(make_translation_cursive)
            examples_unpacked.append(' // '.join(example_and_translation).replace(word, f'<b>{word}</b>')+'<br>')
        return examples_unpacked

    def create_model_and_deck(deck_to_add):
        if config.deck_to_copy_schedule_settings_from != 'none':
            config_id = invoke('getDeckConfig', deck="400 Must - have words for the TOEFL")['id']
        else:
            config_id = '1641449709710'
        invoke('createDeck', deck=deck_to_add)
        invoke('saveDeckConfig', config=card_style_and_deck_config.deck_conf)
        invoke('setDeckConfigId', decks=[deck_to_add], configId=config_id)
        try:
            invoke('modelTemplates', modelName='myCardType')
        except Exception:
            invoke('createModel', modelName="myCardType",
                   inOrderFields=["Term", "Transcription", "Translation", "Definition", "Context", "Audio"],
                   css=card_style_and_deck_config.style, cardTemplates=[{
                    "Name": "myCardType",
                    "Front": card_style_and_deck_config.front,
                    "Back": card_style_and_deck_config.back
                }])

    if deck_to_add not in invoke('deckNames'):
        create_model_and_deck(deck_to_add)

    invoke('addNote', note={
            "deckName": deck_to_add,
            "modelName": "myCardType",
            "fields": {
                "Term": f"{wordcard['word']}",
                "Transcription": f"[{wordcard['transcription']}]",
                "Translation": f"{', '.join(wordcard['reverso_translations'])}",
                "Definition": f"{'<br>'.join(wordcard['all_definitions'])}",
                "Context": f"{'<br>'.join(unpack_tuples_of_context_examples(wordcard['reverso_examples'], wordcard['word']))}",
                "Audio": f"{download_audio(wordcard['audio'], wordcard['word'])}",
            }})
    return f'The new card "{wordcard["word"]}" has been added to your deck "{deck_to_add}".'


# print(invoke('getDeckConfig', deck="400 Must - have words for the TOEFL"))