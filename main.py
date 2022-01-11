import reverso_context, free_dictionary_api


def search_new_word(query):
    wordcard = free_dictionary_api.search_a_word(query)
    if not wordcard:
        return 'No defenitions found :('
    else:
        examples_from_reverso = reverso_context.get_examples(query, quantity_in_one_step=5)
        wordcard['reverso_examples'] = next(examples_from_reverso)
        wordcard['reverso_translations'] = reverso_context.translations(query)
        return print_to_console(wordcard)


def make_cards_from_reverso_favorites():
    pass


def get_examples_from_reverso(query):
    reverso_context.get_examples(query, quantity_in_one_step=10)
    pass


def print_to_console(wordcard):
    print(wordcard['word'], wordcard['transcription'], sep='     ')
    print('-' * 30)
    print(wordcard['reverso_translations'])
    print('-' * 30)
    for defenition in range(5):
        print(f'{defenition+1}. '+wordcard[f'definition{defenition}'].capitalize()+'\n'\
                  if wordcard[f'definition{defenition}'] is not None else '', end='')
    print('-' * 30)
    for example in wordcard['reverso_examples']: print(example)
    print(wordcard)
    return '-'*30


# -----run-----
print(search_new_word(input('Enter a word: ')))
