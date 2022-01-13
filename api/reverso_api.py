from reverso_context_api import Client
import config

client = Client("en", config.lang, credentials=(config.email, config.password))


def translations(query):
    get_translations = list(client.get_translations(query))
    if len(get_translations) > 10:
        return get_translations[:10]
    else:
        return get_translations


def get_examples(query, quantity_in_one_step=5):
    list_of_results = []

    def download_examples_one_by_one(entered_word):
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


# for context in client.get_translation_samples("shenanigans", cleanup=True):
#     print(context)

# list(Client("de", "en").get_search_suggestions("bew")))

# next(client.get_favorites())
