import anki_connect_api
import reverso_api
import free_dictionary_api


def search_new_word(query):
    wordcard = free_dictionary_api.search_a_word(query)
    if not wordcard:
        return False
    else:
        examples_from_reverso = reverso_api.get_examples(query, quantity_in_one_step=10)
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
    user_input = input('Добавить катрочку с этим словом в anki?')
    print(user_input)
    if user_input == 'y':
        return anki_connect_api.add_card(wordcard)
    else:
        return '-'*30


# -----run-----
print(print_to_console(input('Enter a word: ')))
# x = search_new_word('run')
# print(x)
# t = x['reverso_translations']
# j = ', '.join(t)
# d = [x]
# print(j)

# for definition in range(5):
#     print(f'{definition + 1}. ' + wordcard[f'definition{definition}'].capitalize() + '\n' \
#               if wordcard[f'definition{definition}'] is not None else '', end='')