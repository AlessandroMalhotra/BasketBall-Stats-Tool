from constants import PLAYERS

import copy

players_copy = copy.deepcopy(PLAYERS)
Teams = [[], [], []]


def clean_data(players_copy):
    for player in players_copy:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['height'] = int(player['height'].strip('inches'))
        player['guardians'] = player['guardians'].split('and')


def balance_teams(Teams, experienced, inexperienced):
    Teams[0].extend(experienced[:3])
    Teams[0].extend(inexperienced[:3])
    Teams[1].extend(experienced[3:6])
    Teams[1].extend(experienced[3:6])
    Teams[2].extend(experienced[6:9])
    Teams[2].extend(experienced[6:9])
    
def menu():
    welcome = """
BASKETBALL TEAM STATS TOOL

---- MENU----

Here are your choices:
1) Display Team Stats
2) Quit
"""
    print(welcome)
    user_attempt = user_input()


def user_input():
    user_input = None

    while user_input != "1" and user_input != "2":
        user_input = input("Enter 1 or 2:  ")
        print(user_input)
                   
    if user_attempt == 1:
        team_menu()
    
    elif user_attempt == 2:
        print("Thank you, have a nice day!")


def team_menu():
    teams = ['Panthers', 'Bandits', 'Warriors']
    
    for index, team in enumerate(teams, 1):
        print(f"\n{index}.{team}")
    
    while True:
        try:
            user_attempt = int(input("\nEnter an option > 1 "))
            while user_attempt < 0 or user_attempt > 3:
                user_attempt = int(input("\nInvalid entry outside of the range. \n\nEnter a number between 1 and 3: "))
            return user_input
        except ValueError:
            print("Oh no! That's not a valid value. Try again...")
                   
    if user_attempt == 1:
        panthers_stats()
    
    elif user_attempt == 2:
        bandits_stats()
    
    elif user_attempt == 3:
        warrior_stats()

def average_height(team):
    height = 0
    for player in team:
        height += player['height']
    average_height = height / len(team)
    return round(average_height)
    
def panthers_stats(Teams):
    total_players = len(Teams[0])
    total_experienced = len(Teams[0]) // 2
    total_inexperienced = len(Teams[0]) // 2
    panthers_average_height = average_height(Teams[0])
    
    print(f"""
    Team: Panthers Stats
    --------------------
    Total players: {total_players}
    Total experienced: {total_experienced}
    Total inexperienced: {total_inexperienced}
    Average height: {panthers_average_height}
    """)
    
    team_players = []
    for players in Teams[0]:
        name = players["name"]
        team_players.append(name)
    print("Players on Team: {}".format(", ".join(team_players)))
    
    team_guardians = []
    for players in Teams[0]:
    	guardian = ','.join(players['guardians'])
    	team_guardians.append(guardian)
    print('\n'"Guardians on Team: {}".format(", ".join(team_guardians)))
    
    

def bandits_stats(Teams):
    total_players = len(Teams[1])
    total_experienced = len(Teams[1]) // 2
    total_inexperienced = len(Teams[1]) // 2
    bandits_average_height = average_height(Teams[1])
    
    print(f"""
    Team: Bandits Stats
    --------------------
    Total players: {total_players}
    Total experienced: {total_experienced}
    Total inexperienced: {total_inexperienced}
    Average height: {bandits_average_height}
    """)
    
    
    team_players = []
    for players in Teams[1]:
        name = players["name"]
        team_players.append(name)
    print("Players on Team: {}".format(", ".join(team_players)))
    
    team_guardians = []
    for players in Teams[1]:
    	guardian = ','.join(players['guardians'])
    	team_guardians.append(guardian)
    print('\n'"Guardians on Team: {}".format(", ".join(team_guardians)))
        
        
def warrior_stats(Teams):
    total_players = len(Teams[2])
    total_experienced = len(Teams[2])
    total_inexperienced = len(Teams[2])
    warriors_average_height = average_height(Teams[2])
    
    print(f"""
    Team: Warriors Stats
    --------------------
    Total players: {total_players}
    Total experienced: {total_experienced}
    Total inexperienced: {total_inexperienced}
    Average height: {warriors_average_height}
    """)
    
    team_players = []
    for players in Teams[2]:
        name = players["name"]
        team_players.append(name)
    print("Players on Team: {}".format(", ".join(team_players)))
    
    team_guardians = []
    for players in Teams[2]:
    	guardian = ','.join(players['guardians'])
    	team_guardians.append(guardian)
    print('\n'"Guardians on Team: {}".format(", ".join(team_guardians)))
    

if __name__ == '__main__':
    clean_data(players_copy)
    experienced_players = [player for player in players_copy if player['experience'] == True]
    inexperienced_players = [player for player in players_copy if player['experience'] == False]
    
    balance_teams(Teams, experienced_players, inexperienced_players)
    menu()
    user_input()
    team_menu()
    panthers_stats(Teams)
    bandits_stats(Teams)
    warrior_stats(Teams)
    
