# Sets is a matching game, played with a special deck of cards. Each
# card in the deck has a pictogram on it.
#
# Each pictogram has four properties; each property has three choices:
#
#   - Shape   (pill/diamond/squiggle)
#   - Number  (1/2/3)
#   - Color   (red/green/purple)
#   - Fill    (solid/open/hatch)
#
# The deck is made up of one card with each possible combination of
# properties. No two cards are exactly the same.
#
# The objective of the game is to find sets of three cards which
# form a "set".
# A set is formed when ALL of the following are true
# about a group of three cards:
#
# - They all have the same number or have three different numbers.
# - They all have the same shape or have three different shapes.
# - They all have the same fill or have three different fills.
# - They all have the same color or have three different colors.
#
# Here's an example
# https://d2r55xnwy6nx47.cloudfront.net/uploads/2016/05/SETPoint_2000.png
# https://mrrgteacher.files.wordpress.com/2011/12/sets_examples1-1024x586.png
# find set follow reqs
#
# different properties a card can have
PROPERTIES = {
    'shape': ['Pill', 'Diamond', 'Squiggle'],
    'number': [1, 2, 3],
    'color': ['Red', 'Green', 'Purple'],
    'fill': ['Solid', 'Open', 'Hatch'],
}

# example of a card instance
my_card = {
    'shape': 'Pill',
    'number': 2,
    'color': 'Purple',
    'fill': 'Solid',
}


def validateRequirement1(cards, req_dict, bool_list):
    # req 1
    # They all have the same number
    # or have three different numbers.
    propertyValidatorStrings('number', cards, req_dict, 'req1', bool_list)


def validateRequirement2(cards, req_dict, bool_list):
    # req 2
    # They all have the same shape
    # have three different shapes.
    propertyValidatorStrings('shape', cards, req_dict, 'req2', bool_list)


def validateRequirement3(cards, req_dict, bool_list):
    # req 3
    # They all have the same fill
    # have three different fills.
    propertyValidatorStrings('fill', cards, req_dict, 'req3', bool_list)


def validateRequirement4(cards, req_dict, bool_list):
    # req 4
    # They all have the same color or
    # have three different colors.
    propertyValidatorStrings('color', cards, req_dict, 'req4', bool_list)


# key name , cards dictionary, results dictionary, requirement
def propertyValidatorStrings(key_name, cards, req_dict, requirement, bool_list):
    list_of_strings = []
    for key in cards:
        # print(key[key_name])
        list_of_strings.append(key[key_name])

    print(list_of_strings)
    is_all_values_the_same = all(number == list_of_strings[0] for number in list_of_strings)
    print(is_all_values_the_same)
    is_all_values_different = all(number != list_of_strings[0] for number in list_of_strings)
    print(is_all_values_different)
    print(list_of_strings)
    print(key_name)

    if (not is_all_values_different):
        req = {requirement: 'is a set'}
        req_dict.append(req)
        bool_list.append(True)
        return
    if (is_all_values_the_same):
        req = {requirement: 'is a set'}
        req_dict.append(req)
        bool_list.append(True)
        return

    req = {requirement: 'is not a set'}
    req_dict.append(req)
    bool_list.append(False)
    return


def is_set(cards):
    req_dict = []
    bool_list = []
    validateRequirement1(cards, req_dict, bool_list)
    validateRequirement2(cards, req_dict, bool_list)
    validateRequirement3(cards, req_dict, bool_list)
    validateRequirement4(cards, req_dict, bool_list)
    print(bool_list)
    print(req_dict)
    return all(val == bool_list[0] for val in bool_list)


if __name__ == '__main__':
    # valid
    # ['Pill', 3, 'Red', 'Solid']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 1, 'Purple', 'Open']
    card1 = {
        'shape': 'Pill',
        'number': 3,
        'color': 'Red',
        'fill': 'Solid',
    }
    card2 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card3 = {
        'shape': 'Squiggle',
        'number': 1,
        'color': 'Purple',
        'fill': 'Open',
    }

    # valid
    # ['Pill', 2, 'Green', 'Open']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 2, 'Green', 'Solid']
    card4 = {
        'shape': 'Pill',
        'number': 2,
        'color': 'Green',
        'fill': 'Open',
    }
    card5 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card6 = {
        'shape': 'Squiggle',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }

    # not valid
    # ['Pill', 2, 'Green', 'Solid']
    # ['Diamond', 2, 'Green', 'Hatch']
    # ['Squiggle', 2, 'Green', 'Solid']
    card7 = {
        'shape': 'Pill',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }
    card8 = {
        'shape': 'Diamond',
        'number': 2,
        'color': 'Green',
        'fill': 'Hatch',
    }
    card9 = {
        'shape': 'Squiggle',
        'number': 2,
        'color': 'Green',
        'fill': 'Solid',
    }
    print("test below:")
    print(is_set([card1, card2, card3]), True)
    print(is_set([card4, card5, card6]), True)
    print(is_set([card7, card8, card9]), False)