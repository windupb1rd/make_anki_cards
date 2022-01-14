from api import free_dictionary_api, reverso_api, anki_connect_api
import config


def search_new_word(query):
    wordcard = free_dictionary_api.search_a_word(query)
    if not wordcard:
        return False
    else:
        examples_from_reverso = reverso_api.get_examples(query, quantity_in_one_step=config.number_of_reverso_context_examples_in_a_card)
        wordcard['reverso_examples'] = next(examples_from_reverso)
        wordcard['reverso_translations'] = reverso_api.translations(query)
        return wordcard


def make_cards_from_reverso_favorites():
    pass


def print_to_console(query):
    wordcard: dict = search_new_word(query)
    try:
        print(wordcard['word'], wordcard['transcription'], sep='     ')
    except TypeError:
        return 'No definitions found'
    print('-' * 30)
    print(wordcard['reverso_translations'])
    print('-' * 30)
    for definition in wordcard['all_definitions']: print(definition)
    print('-' * 30)
    for example in wordcard['reverso_examples']: print(example)
    print('-' * 30)
    user_input = input('Do you want to add a card with this word to Anki? y/n ')
    if user_input == 'y':
        try:
            return anki_connect_api.add_card(wordcard)
        except Exception as error:
            return run(str(error).capitalize())
    else:
        return run('__run__')


def run(inp):
    if inp != '__run__':
        print(inp)
    inp = input('Enter a word: ')
    while inp != 'exit':
        print(print_to_console(inp))
        return run('__run__')


# -----run-----
run('__run__')
