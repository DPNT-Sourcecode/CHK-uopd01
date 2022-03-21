# noinspection PyUnusedLocal
# skus = unicode string

PRICE_BY_ITEM = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
# We'll map items to lists of length 2 tuples such that the first element
# is the number of items, second element is the total discounted price
DISCOUNT_OFFERS_BY_ITEM = {"A": [(3, 130), (5, 200)], "B": [(2, 4)]}
# for get one free offers, first element is number of items, second is the item you get for free
GET_ONE_FREE_OFFERS_BY_ITEM = {"E": (2, "B")}


def compute_price_with_special_offer(*, num_items, regular_price, special_offer_quantity, special_offer_price):
    price = 0
    num_special_offers = num_items // special_offer_quantity
    num_regular_items = num_items % special_offer_quantity
    price += num_special_offers * special_offer_price
    price += num_regular_items * regular_price
    return price


def checkout(skus):
    skus_list = [sku for sku in skus]

    # basic input validation
    if any([sku not in PRICE_BY_ITEM for sku in skus_list]):
        return -1

    # compute number of items per item
    number_per_item = {}
    for sku in skus_list:
        if sku in number_per_item:
            number_per_item[sku] += 1
        else:
            number_per_item[sku] = 1

    # apply get one free offers
    for sku in number_per_item:
        if sku in GET_ONE_FREE_OFFERS_BY_ITEM:
            number_of_items, free_item = GET_ONE_FREE_OFFERS_BY_ITEM[sku]
            if free_item in number_per_item:
                number_of_free_items = number_per_item[sku] // number_of_items
                number_per_item[free_item] -= number_of_free_items

    # compute total checkout value
    total = 0
    for sku in number_per_item:
        regular_price = PRICE_BY_ITEM[sku]
        if sku in DISCOUNT_OFFERS_BY_ITEM:
            # our strategy is to apply every offer and return the highest discounted price thus finding the "best offer"
            best_discounted_price = 0
            for special_offer_quantity, special_offer_price in DISCOUNT_OFFERS_BY_ITEM[sku]:
                discounted_price = compute_price_with_special_offer(
                    num_items=number_per_item[sku],
                    regular_price=regular_price,
                    special_offer_quantity=special_offer_quantity,
                    special_offer_price=special_offer_price,
                )
                if discounted_price > best_discounted_price:
                    best_discounted_price = discounted_price

            total += best_discounted_price
        else:
            total += regular_price * number_per_item[sku]

    return total






