dollars = 500
number_of_players = 4
number_of_rounds = 10


def set_variables(d, p, r):
    global dollars, number_of_players, number_of_rounds
    dollars = d
    number_of_players = p
    number_of_rounds = r


def get_players():
    return number_of_players


def get_dollars():
    return dollars


def get_rounds():
    return number_of_rounds
