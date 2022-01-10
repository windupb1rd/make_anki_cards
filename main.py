import reverso_context, free_dictionary_api


def search(query):
    main = free_dictionary_api.search_a_word(query)
    if not main:
        return 'No defenitions found :('
    else:
        reverso_context.translations(query)
        examples = reverso_context.get_examples(query, quantity_in_one_step=5)
        return main


print(search(input('Enter query: ')))