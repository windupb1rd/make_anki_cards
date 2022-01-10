import reverso_context, free_dictionary_api


def search(query):
    if not free_dictionary_api.search_a_word(query):
        return 'No defenitions found :('
    else:

        translations = reverso_context.translations(query)
        examples = reverso_context.get_examples(query, quantity_in_one_step=5)


print(search(input('Enter query: ')))