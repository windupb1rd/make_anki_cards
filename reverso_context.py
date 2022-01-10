from reverso_context_api import Client


client = Client("en", "ru", credentials=("sheyan44@gmail.com", "DGO8qs9rptO"))


def translations(query):
    return client.get_translations(query)


def get_examples(query, quantity_in_one_step=10):
    list_of_results = []

    def download_examples_one_by_one(entered_word):  # итератор, выдает по одному значению через вызов из функции next
        all_examples = client.get_translation_samples(entered_word, cleanup=True)
        for example in all_examples:
            yield example

    result = download_examples_one_by_one(query)
    for j in range(10):
        quantity = quantity_in_one_step
        while quantity > 0:
            list_of_results.append(next(result))
            quantity -= 1
        yield list_of_results
        list_of_results.clear()


# examples = get_examples('go', quantity_in_one_step=5)
# print(next(examples))
# print(next(examples))
# print(next(examples))
# print(next(examples))
# print(examples)
# print(next(examples))
# print(next(examples))

# print(one_example_at_a_time('run'))
# suggestions = list(client.get_search_suggestions()
# print(list(x))



# for context in client.get_translation_samples("shenanigans", cleanup=True):
#     print(context)

# list(Client("de", "en").get_search_suggestions("bew")))

# next(client.get_favorites())
