from reverso_context_api import Client


client = Client("en", "ru", credentials=("sheyan44@gmail.com", "DGO8qs9rptO"))


def translations(query):
    return list(client.get_translations(query))


def get_examples(query, quantity=100):
    list_of_results = []

    def samples(word):  # итератор, выдает по одному значению через вызов из функции next
        all_examples = client.get_translation_samples(word, cleanup=True)
        for example in all_examples:
            yield example

    i = samples(query)
    while quantity > 0:
        list_of_results.append(next(i))
        quantity -= 1
    return list_of_results


examples = get_examples('go', quantity=10)
print(examples[0:2])
print(examples[2:4])
print(examples)
# print(next(examples))
# print(next(examples))

# print(one_example_at_a_time('run'))
# suggestions = list(client.get_search_suggestions()
# print(list(x))



# for context in client.get_translation_samples("shenanigans", cleanup=True):
#     print(context)

# list(Client("de", "en").get_search_suggestions("bew")))

# next(client.get_favorites())
