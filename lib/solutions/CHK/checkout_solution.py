# noinspection PyUnusedLocal
# skus = unicode string

PRICE_BY_ITEM = {"A": 50, "B": 30, "C": 20, "D": 15}
# We'll map items to length 2 tuples such that the first element
# is the number of items, second element is the total discounted price
SPECIAL_OFFERS_BY_ITEM = {"A": [3, 130], "B": [2, 45]}


def checkout(skus):
    skus_list = skus.split(",")

    # basic input validation
    if any([sku not in PRICE_BY_ITEM for sku in skus_list]):
        return -1

    raise NotImplementedError()

