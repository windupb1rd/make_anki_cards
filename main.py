import reverso_context, free_dictionary_api


def search_new_word(query):
    wordcard = free_dictionary_api.search_a_word(query)
    if not wordcard:
        return 'No defenitions found :('
    else:
        examples_from_reverso = reverso_context.get_examples(query, quantity_in_one_step=5)
        wordcard['reverso_examples'] = next(examples_from_reverso)
        wordcard['reverso_translations'] = reverso_context.translations(query)
        return wordcard


def make_cards_from_reverso_favorites():
    pass


def get_examples_from_reverso(query):
    reverso_context.get_examples(query, quantity_in_one_step=10)
    pass


def print_to_console(query):
    wordcard: dict = search_new_word(query)
    print(wordcard['word'], wordcard['transcription'], sep='     ')
    print('-' * 30)
    print(wordcard['reverso_translations'])
    print('-' * 30)
    for definition in range(5):
        print(f'{definition+1}. '+wordcard[f'definition{definition}'].capitalize()+'\n'\
                  if wordcard[f'definition{definition}'] is not None else '', end='')
    print('-' * 30)
    for example in wordcard['reverso_examples']: print(example)
    return '-'*30


# -----run-----
print(print_to_console(input('Enter a word: ')))
