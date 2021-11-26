
import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')


print(logo)
print('Welcome to the secret auction program!')


def final_bid(bids):
    highest_bid = 0
    highest_name = ""
    for key in bids:
        # print('Bidder (key) is [{0}], bid (value) [{1}]'.format(
        # key, bids[key]))
        if highest_bid < bids[key]:
            highest_bid = bids[key]
            highest_name = key
    print(f'The winner is {highest_name} with a bid of ${highest_bid}')


bids = {}
bidding = True
while bidding:
    name = input('What is your name?\n')
    bid = int(input('How much do you bid?\n$'))
    bids[name] = bid
    another_bidder = input(
        'Are there any other bidders? Type "yes" or "no"\n').lower()
    if another_bidder == 'no':
        bidding = False
        clearConsole()
        final_bid(bids)
    else:
        clearConsole()
