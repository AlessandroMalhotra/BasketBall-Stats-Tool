from constants import PLAYERS

from collections import OrderedDict

import copy

# Make a copy of the PLAYERS list.
players_copy = copy.deepcopy(PLAYERS)
Teams = [[], [], []]


# Clean up the data so the experiene is either 'True' or 'False' and height is solely a integer value.
def clean_data(players_copy):
    for player in players_copy:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['height'] = int(player['height'].strip('inches'))
        player['guardians'] = player['guardians'].split('and')


# Balance the players accross three teams with equal amount of experienced and inexperienced.
def balance_teams(Teams, experienced, inexperienced):
    Teams[0].extend(experienced[:3])
    Teams[0].extend(inexperienced[:3])
    Teams[1].extend(experienced[3:6])
    Teams[1].extend(experienced[3:6])
    Teams[2].extend(experienced[6:9])
    Teams[2].extend(experienced[6:9])


# Displays the main menu.
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
    return user_attempt


# Ask user for input of 1 or 2 which will then display either team stats or quit the appication.
def user_input():
    user_input = None 
    while user_input != '1' and user_input != '2':
        user_input = input('Enter 1 or 2:  ')             
    return user_input


# If the user selects 1 it will display menu of the three teams and prompt the user to enter a number between 1-3 to show the stats of a team.
def team_menu():
    teams = ['Panthers', 'Bandits', 'Warriors']
    
    choice = None
    
    while choice != 'q':
        print('\n Enter q to return back to main menu.')
        for index, team in enumerate(teams, 1):
            print(f"\n{index}.{team}")
        
        choice = input("Enter a option between 1 and 3: ").lower().strip()
    
        if choice in stats_menu:
            stats_menu[choice]()


# This calculates average height of the teams 
def average_height(team):
    height = 0
    for player in team:
        height += player['height']
    average_height = height / len(team)
    return round(average_height)


# Displays panthers team stats 
def panthers_stats():
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
    enters = exit()
    

# Displays bandits stats
def bandits_stats():
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
    enters = exit()


# Display warrior stats
def warrior_stats():
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
    enters = exit()

# If user selects quit then this will prompt user to press enter and the app will quit
def exit():
    input("\nPress 'ENTER' to continue  ").lower().strip()
 

if __name__ == '__main__':
    clean_data(players_copy)
    experienced_players = [player for player in players_copy if player['experience'] == True]
    inexperienced_players = [player for player in players_copy if player['experience'] == False]
    stats_menu = OrderedDict([('1', panthers_stats), ('2', bandits_stats), ('3', warrior_stats)])
    
    balance_teams(Teams, experienced_players, inexperienced_players)
    choice = menu()
    while choice != '2':
        team_menu()
        choice = menu()
    print('Goodbye!')
