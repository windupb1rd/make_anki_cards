import reverso_context, free_dictionary_api


def search(query):
    main = free_dictionary_api.search_a_word(query)
    if not main:
        return 'No defenitions found :('
    else:
        examples = reverso_context.get_examples(query, quantity_in_one_step=5)
        final_card = {'word': main[0],
                      'transcription': main[1],
                      'translations': list(reverso_context.translations(query))[:10],
                      'defenition1': '',
                      'exampes1': '',
                      'reverso_examples': next(examples),
                      }


        return final_card


print(search(input('Enter a word: ')))
