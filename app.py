import constants
import copy
import random


def print_team_players(players, team):
    roster = []
    for index, player in enumerate(players):
        if player['team'] == team:
            roster.append(player['name'])

    return ', '.join(roster)


def print_player_gaurdians(players, team):
    gaurdians = []
    for index, player in enumerate(players):
        if player['team'] == team:
            gaurdians.append(player['guardians'])

    return ', '.join(', '.join(gaurdians).split(' and '))


def count_team_players(players, team):
    count = 0
    for index, player in enumerate(players):
        if player['team'] == team:
            count += 1
    return count


def cal_total_experience(players, team):
    count = 0
    for index, player in enumerate(players):
        if player['team'] == team:
            if player['experience'] is True:
                count += 1
    return count


def cal_total_inexperience(players, team):
    count = 0
    for index, player in enumerate(players):
        if player['team'] == team:
            if player['experience'] is False:
                count += 1
    return count


def cal_average_height(players, team):
    heights = []
    for index, player in enumerate(players):
        if player['team'] == team:
            heights.append(int(player['height']))

    return sum(heights)/len(heights)


def clean_data(players):

    for index, player in enumerate(players):
        measurement, unit = player['height'].split(' ')
        player['height'] = int(measurement)

        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


def balance_teams(players, teams):
    num_players_team = len(players) / len(teams)
    team_assignment = teams * int(num_players_team)
    experience_list = []
    inexperience_list = []
    players_list = []

    for index, player in enumerate(players):
        if player['experience'] is True:
            experience_list.append(player['name'])
        else:
            inexperience_list.append(player['name'])

    players_list.extend(random.sample(experience_list, len(experience_list)))
    players_list.extend(random.sample(
        inexperience_list, len(inexperience_list)))

    for l_index, reference in enumerate(players_list):
        # print(l_index, reference, players_list[l_index])
        for index, player in enumerate(players):
            if player['name'] == reference:
                player['team'] = team_assignment[l_index]
                # print(players[index])
                break
            else:
                continue


def select_option():
    print()
    print("BASKETBALL TEAM STATS TOOL \n")
    print("---- MENU ----\n")
    print("Here are the choices:")
    print("\t 1) Display Team Stats")
    print("\t 2) Quit \n")

    while True:
        try:
            action = int(input("Enter an option > "))
            if action not in range(1, 3):
                raise ValueError("The selected number is out of range")
        except ValueError as err:
            print(f"We ran into an issue: '{err}'. Please try again.")
        else:
            if action == 2:
                print()
                print("----------")
                print("Thanks for using the Basketball team stats tool")
                print("----------\n")
                exit()
            else:
                return action
                break


def select_team(teams):
    print()
    print("\t 1) Panthers")
    print("\t 2) Bandits")
    print("\t 3) Warriors \n")

    while True:
        try:
            team_option = int(input("Enter an option > "))
            if team_option not in range(1, len(teams) + 1):
                raise ValueError("The selected number is out of range")
        except ValueError as err:
            print(f"We ran into an issue: '{err}'. Please try again.")
        else:
            return team_option
            break


def print_stats(players, teams, team_option):
    print()
    team = teams[team_option-1]
    print(f"Team: {teams[team_option-1]} Stats")
    print("--------------------")
    print(f"Total players: {count_team_players(players, team)}")
    print(f"Total experience: {cal_total_experience(players, team)}")
    print(f"Total inexperienced: {cal_total_inexperience(players, team)}")
    print(f"Average height: {cal_average_height(players, team)}")
    print()
    print("Players on Team:")
    print('\t', print_team_players(players, team))
    print("Gaurdians:")
    print('\t', print_player_gaurdians(players, team))
    print()


def tool(teams, players):
    select_option()
    team_option = select_team(teams)
    print_stats(players, teams, team_option)


def main():
    teams_copy = copy.deepcopy(constants.TEAMS)
    players_copy = copy.deepcopy(constants.PLAYERS)
    clean_data(players_copy)
    balance_teams(players_copy, teams_copy)

    while True:
        tool(teams_copy, players_copy)
        input("Press ENTER to continue...")


if __name__ == "__main__":
    main()