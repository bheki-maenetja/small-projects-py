from tabulate import tabulate

def create_teams():
    all_teams = dict()
    for i in range(2):
        while True:
            try:
                team_name = input("Enter a team name: ").lower().strip()
                1/len(team_name)
            except ZeroDivisionError:
                input("You need to enter a team name >>> ")
            else:
                break
        all_teams[team_name] = dict().fromkeys(['pts', 'gd', 'gf', 'ga', 'w', 'd', 'l'], 0)
    return all_teams

def get_table(team_dic):
    league_table = []
    for name in team_dic:
        team_record = list(team_dic[name].values())
        team_record.insert(0, name[0:3].upper())
        league_table.append(team_record)
    league_table.sort(key=lambda x: x[1], reverse=True)
    league_table = tabulate(league_table, headers=['TEAM', 'PTS', 'GD', 'GF', 'GA', 'W', 'D', 'L'], showindex=range(1,3))
    return league_table

def match_day(team_dic, match_num):
    scores = [0,0]
    teams = list(team_dic.keys())
    team1, team2 = team_dic[teams[0]], team_dic[teams[1]]
    input(f"Matchday {match_num}: {teams[0].capitalize()} vs {teams[1].capitalize()} >>> ")
    for t in teams:
        while True:
            try:
                scores[teams.index(t)] = int(input(f"Enter the score for {t.capitalize()}: "))
            except ValueError:
                input("You need to enter a number >>> ")
            else:
                break
    input(f"Matchday {match_num} result: {teams[0][0:3].upper()} {scores[0]} - {scores[1]} {teams[1][0:3].upper()} >>> ")
    team1['gf'], team1['ga'], team1['gd'] = team1['gf'] + scores[0], team1['ga'] + scores[1], team1['gd'] + (scores[0] - scores[1])
    team2['gf'], team2['ga'], team2['gd'] = team2['gf'] + scores[1], team2['ga'] + scores[0], team2['gd'] + (scores[1] - scores[0])
    if scores[0] > scores[1]:
        team1['pts'], team1['w'] = team1['pts'] + 3, team1['w'] + 1
        team2['l'] += 1
    elif scores[0] < scores[1]:
        team2['pts'], team2['w'] = team2['pts'] + 3, team2['w'] + 1
        team1['l'] += 1
    else:
        team1['pts'], team1['d'] = team1['pts'] + 1, team1['d'] + 1
        team2['pts'], team2['d'] = team2['pts'] + 1, team2['d'] + 1

def main():
    input("Welcome to LEAGUE BUILDER!!! >>> ")
    while True:
        try:
            num_matches = abs(int(input("Enter the number of matches that your teams will play: ")))
            1/num_matches
        except (ValueError, ZeroDivisionError):
            input("Please enter a valid number")
        else:
            break
    input("Create your teams >>> ")
    teams = create_teams()
    for i in range(0, num_matches):
        match_day(teams, i + 1)
    print(get_table(teams))

main()
