from controller import play_auction_game, print_bots, reset_scores

play_auction_game(4, 10, 500, True, True)
print_bots()


reset_scores()
# Play a weekly tournament with dollars increasing
dollars = [1000, 2000, 3000, 4000, 5000, 6000, 7000]
for d in dollars:
    play_auction_game(4, 10, d, True, True)
    print_bots()


reset_scores()
# Play a weekly tournament with amount of players increasing
players = [2, 3, 4, 5, 6, 7, 8]
for p in players:
    play_auction_game(p, 10, 500, True, True)
    print_bots()

reset_scores()
# Play a weekly tournament with amount of rounds increasing
rounds = [1, 2, 3, 4, 5, 10, 20]
for r in rounds:
    play_auction_game(4, r, 500, True, True)
    print_bots()
