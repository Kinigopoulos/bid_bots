# Source code:
# https://codegolf.stackexchange.com/questions/147576/first-price-sealed-bid-auction
import hashlib
from global_variables import set_variables
# Import all bot classes here
from all_in_bot import AllInBot
from random_bot import RandomBot
from zero_bot import ZeroBot
from average_bot import AverageBot
from bit_below_bot import BitBelowBot
from all_in_half_bot import AllInHalfBot
from counter_bot import CounterBot
from collecting_bot import CollectingBot
from last_win_bot import LastWinBot
from half_in_bot import HalfInBot
from persistent_bot import PersistentBot
from average_biding_bot import AverageBidingBot
from no_tie_bot import NoTieBot
from selective_bot import SelectiveBot
from all_plus_one import AllPlusOne
from attack_bot import AttackBot
from thorn_on_my_side import ThornOnMySide
from max_possible_bot import MaxPossibleBot
from linear_regression_bot import LinearRegressionBot

# Enter all the bots here
bot_list = [
    AllInBot,
    RandomBot,
    ZeroBot,
    AverageBot,
    BitBelowBot,
    AllInHalfBot,
    CounterBot,
    CollectingBot,
    LastWinBot,
    HalfInBot,
    PersistentBot,
    AverageBidingBot,
    NoTieBot,
    SelectiveBot,
    AllPlusOne,
    AttackBot,
    ThornOnMySide,
    MaxPossibleBot,
    LinearRegressionBot
]


def generate_hash_number(num):
    n = 1
    while num > 1:
        n * num
        num -= 1
    return n


# Random function to shuffle the bots' turns
def decide_order(ls):
    hash_num = int(hashlib.sha1(str(ls).encode()).hexdigest(), 16) % hash_number
    nls = []
    for i in range(number_of_players, 0, -1):
        nls.append(ls[hash_num % i])
        del ls[hash_num % i]
        hash_num //= i
    return nls


def auction(ls):
    global score, total
    pl = decide_order(sorted(ls))
    bots = [bot_list[i]() for i in pl]
    dollar = [0] * number_of_players
    prev_win, prev_bid = -1, -1
    for rounds in range(number_of_rounds):
        bids = []
        for i in range(number_of_players):
            dollar[i] += dollars
        for i in range(number_of_players):
            tmp_win = prev_win
            if prev_win == i:
                tmp_win = 0
            elif prev_win != -1 and prev_win < i:
                tmp_win += 1
                if not winner_is_known:
                    tmp_win = -10

            bid = int(bots[i].play_round(tmp_win, prev_bid))
            if bid < 0 or bid > dollar[i]:
                raise ValueError(pl[i], bots[i].__class__, bid)
            bids.append((bid, i))
        # Sort the bids in descending order
        bids.sort(reverse=True)
        winner = 0

        # If this game-rule is True then remove any ties that are possible winners
        if ties_disqualify:
            for i in range(number_of_players):
                if i == 0:
                    if bids[i][0] != bids[i + 1][0]:
                        winner = i
                        break
                elif i == number_of_players - 1:
                    if bids[i - 1][0] == bids[i][0]:
                        winner = -1
                    else:
                        winner = i
                else:
                    if bids[i][0] != bids[i - 1][0] and bids[i][0] != bids[i + 1][0]:
                        winner = i
                        break

        if winner == -1:
            prev_win, prev_bid = -1, -1
        else:
            prev_bid, prev_win = bids[winner]
            score[pl[prev_win]] += 1
            total[pl[prev_win]] += prev_bid
            dollar[prev_win] -= prev_bid


def organise_auction(player_list, m):
    if len(player_list) == number_of_players:
        auction(player_list)
    else:
        for new_player in range(m + 1, N):
            new_list = player_list.copy()
            new_list.append(new_player)
            organise_auction(new_list, new_player)


number_of_players = 4
number_of_rounds = 10
hash_number = generate_hash_number(number_of_players)
dollars = 500
ties_disqualify = True
winner_is_known = True

N = len(bot_list)
score = [0] * N
total = [0] * N


def play_auction_game(players, rounds, dollars_, ties, know_winner):
    global number_of_players, number_of_rounds, dollars, hash_number, ties_disqualify, winner_is_known
    number_of_players = players
    number_of_rounds = rounds
    dollars = dollars_
    hash_number = generate_hash_number(number_of_players)
    ties_disqualify = ties
    winner_is_known = know_winner

    set_variables(dollars, number_of_players, number_of_rounds)

    # Organise recursively all possible combinations with the bots.
    organise_auction([], -1)
    # Sort bots according to best score.
    res = sorted(map(list, zip(score, total, bot_list)), key=lambda k: (-k[0], k[1]))

    class TieRemoved:
        pass

    for i in range(N - 1):
        if (res[i][0], res[i][1]) == (res[i + 1][0], res[i + 1][1]):
            res[i][2] = res[i + 1][2] = TieRemoved
    for sc, t, tp in res:
        print('%-20s Score: %-6d Total: %d' % (tp.__name__, sc, t))
