from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
yes_or_no = True
players_info = []
players_names = []
print(logo)
print("Welcome to the secret auction program.")
while yes_or_no:
    player_name = input("What is your name?: ")
    players_names.append(player_name)
    player_bid = int(input("What's your bid?: $"))
    players_info.append({player_name: player_bid})
    user_yes_or_no = input(
        "Are there any other bidders? Type 'yes' or 'no.'").lower()
    if user_yes_or_no == "yes":
        yes_or_no = True
        clear()
    elif user_yes_or_no == "no":
        yes_or_no = False
        clear()
max = players_info[-1][player_name]
for dicts in range(len(players_info) - 2, -1, -1):
    if max < players_info[dicts][players_names[dicts]]:
        max = players_info[dicts][players_names[dicts]]
for dicts in range(len(players_info) - 1, -1, -1):
    if players_info[dicts][players_names[dicts]] == max:
        print(
            f"The winner is {players_names[dicts]} with a bid of ${players_info[dicts][players_names[dicts]]}"
        )
