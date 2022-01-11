import reverso_context, free_dictionary_api

def search_new_word(query):
    word_and_transcript = free_dictionary_api.search_a_word(query)
    if not word_and_transcript:
        return 'No defenitions found :('
    else:
        examples_from_reverso = reverso_context.get_examples(query, quantity_in_one_step=10)
        collected_data_from_dictionaries = {
                      'word': word_and_transcript[0],
                      'transcription': f'[{word_and_transcript[1]}]',
                      'translations': reverso_context.translations(query),
                      'definition1': word_and_transcript[2],
                      'example1': word_and_transcript[3],
                      'definition2': word_and_transcript[4],
                      'example2': word_and_transcript[5],
                      'synonyms': '',
                      'reverso_examples': next(examples_from_reverso),
                      }
        return collected_data_from_dictionaries


def make_cards_from_reverso_favorites():
    pass

def get_examples_from_reverso(query):
    reverso_context.get_examples(query, quantity_in_one_step=10)
    pass


wordcard = search_new_word(input('Enter a word: '))
print(wordcard['word'], wordcard['transcription'], sep='     ')
print('-'*20)
print(wordcard['translations'])
print('-'*20)
print(wordcard['definition1'],end='')
print(wordcard['definition2'], '\n' if not '' else '', end='')
# print(wordcard['definition3'], '\n' if not '' else '', end='')
# print(wordcard['definition2'], '\n' if not '' else '', end='')
print('-'*20)
for example in wordcard['reverso_examples']: print(example)
