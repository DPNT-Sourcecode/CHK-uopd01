# noinspection PyUnusedLocal
# skus = unicode string

PRICE_BY_ITEM = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
# We'll map items to lists of length 2 tuples such that the first element
# is the number of items, second element is the total discounted price
# F is a special case where it "looks" like a "get one free" offer, but it's actually a
# discount offer since it requires at least 3 F's in the basket and applies the price of 2
DISCOUNT_OFFERS_BY_ITEM = {"A": [(3, 130), (5, 200)], "B": [(2, 45)], "F": [(3, 20)]}
# for get one free offers, first element is number of items, second is the item you get for free
GET_ONE_FREE_OFFERS_BY_ITEM = {"E": (2, "B")}


def compute_price_with_special_offers(num_items, regular_price, *offers):
    # validate pairs of (number_of_item, offer)
    assert all([len(offer) == 2 for offer in offers])

    # sort from best to worst offer
    offers = sorted(offers, key=lambda x: x[0], reverse=True)

    price = 0
    remaining_items = num_items
    # apply offers from best to worst
    for offer_quantity, offer_price in offers:
        num_offers = remaining_items // offer_quantity
        remaining_items = remaining_items % offer_quantity
        price += num_offers * offer_price
    price += remaining_items * regular_price
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
            total += compute_price_with_special_offers(number_per_item[sku], regular_price, *DISCOUNT_OFFERS_BY_ITEM[sku])
        else:
            total += regular_price * number_per_item[sku]

    return total



