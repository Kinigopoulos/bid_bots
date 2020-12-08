# Source code:
# https://codegolf.stackexchange.com/questions/147576/first-price-sealed-bid-auction
import hashlib
# Import all bot classes here
from all_in_bot import AllInBot
from random_bot import RandomBot
from zero_bot import ZeroBot
from average_bot import AverageBot


# Enter all the bots here
bot_list = [
    AllInBot,
    RandomBot,
    ZeroBot,
    AverageBot
]


def generate_hash_number(num):
    n = 1
    while num > 1:
        n * num
        num -= 1
    return n


# Random function to shuffle the bots' turns
def decide_order(ls):
    hash = int(hashlib.sha1(str(ls).encode()).hexdigest(), 16) % hash_number
    nls = []
    for i in range(4, 0, -1):
        nls.append(ls[hash % i])
        del ls[hash % i]
        hash //= i
    return nls


number_of_players = 4
number_of_rounds = 10
hash_number = generate_hash_number(number_of_players)

N = len(bot_list)
score = [0] * N
total = [0] * N


def auction(ls):
    global score, total
    pl = decide_order(sorted(ls))
    bots = [bot_list[i]() for i in pl]
    dollar = [0] * number_of_players
    prev_win, prev_bid = -1, -1
    for rounds in range(number_of_rounds):
        bids = []
        for i in range(number_of_players):
            dollar[i] += 500
        for i in range(number_of_players):
            tmp_win = prev_win
            if prev_win == i:
                tmp_win = 0
            elif prev_win != -1 and prev_win < i:
                tmp_win += 1
            bid = int(bots[i].play_round(tmp_win, prev_bid))
            if bid < 0 or bid > dollar[i]:
                raise ValueError(pl[i])
            bids.append((bid, i))

        bids.sort(reverse=True)
        winner = 0
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


def organise_auction(player_list, m, n):
    if n == -1:
        auction(player_list)
    else:
        for new_player in range(m + 1, N - n):
            player_list.append(new_player)
            organise_auction(player_list, m + 1, n - 1)


organise_auction([], -1, N - 1)
res = sorted(map(list, zip(score, total, bot_list)), key=lambda k: (-k[0], k[1]))


class TIE_REMOVED: pass


for i in range(N - 1):
    if (res[i][0], res[i][1]) == (res[i + 1][0], res[i + 1][1]):
        res[i][2] = res[i + 1][2] = TIE_REMOVED
for sc, t, tp in res:
    print('%-20s Score: %-6d Total: %d' % (tp.__name__, sc, t))
