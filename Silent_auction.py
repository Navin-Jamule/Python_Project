# Dictionary to store each bidder's name and their bid amount
bidder = {}

# Flag to control the bidding loop
exit = False

# Loop to collect bids from multiple users
while not exit:
    bidder_name = str(input('What is your name? '))       # Ask for bidder's name
    bidder_amount = int(input('What is your bid? '))      # Ask for bidder's bid amount
    
    bidder[bidder_name] = bidder_amount                   # Store the bid in the dictionary with name as key

    stop_bid = str(input('Is there anyone else to bid? yes or no: '))  # Ask if there are more bidders
    print('\n'*25)                                        # Clear the screen for next bidder (creates space)

    if stop_bid == 'no':
        exit = True                                       # Stop the loop if no more bidders

# Initialize variables to track the highest bid and winner name
current_bid = 0
winner_name = ''

# Loop through all bids to find the highest one
for bids in bidder:
    value = bidder[bids]                     # Get the bid amount
    if current_bid <= value:                 # If current bid is less than or equal to the new bid
        current_bid = value                  # Update the highest bid
        winner_name = bids                   # Update the winner's name

# Announce the winner
print(f'Winner is {winner_name} with the bid of {current_bid}')
