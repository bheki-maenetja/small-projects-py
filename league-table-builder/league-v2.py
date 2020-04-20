from tabulate import tabulate

def create_teams():
    team_data = [dict().fromkeys(['name', 'team', 'pts','gd','gf','ga','w','d','l'], 0) for i in range(2)]
    for i in range(2):
        while True:
            try:
                team_name = input(f"Enter the name of your {['1st', '2nd'][i]} team (must be 4 characters or more): ").strip().lower()
                team_abbr = input(f"Enter a 3-letter abbreviation for your {['1st', '2nd'][i]} team: ").strip().upper()
                if len(team_name) < 3 or len(team_abbr) != 3: raise ValueError
            except ValueError:
                input("One or more of your inputs were invalid!!! >>>")
            else:
                break
        team_data[i]['name'], team_data[i]['team'] = team_name, team_abbr
    return team_data

def match_day(team_list, match_num):
    input(f"Matchday {match_num}: {team_list[0]['name'].capitalize()} vs {team_list[1]['name'].capitalize()} >>> ")
    scores = [0,0]
    for i in range(2):
        while True:
            try:
                team_score = abs(int(input(f"Enter the score for {team_list[i]['name'].capitalize()}: ")))
                scores[i] = team_score
            except ValueError:
                input("Enter a valid input!!! >>> ")
            else:
                break
    else:
        for t in team_list:
            i = team_list.index(t)
            t['gf'], t['ga'], t['gd'] = (t['gf'] + scores[i]), (t['ga'] + scores[i-1]), (t['gd'] + (scores[i] - scores[i-1]))
            if scores[i] > scores[i-1]:
                t['pts'], t['w'], team_list[i-1]['l'] = (t['pts'] + 3), (t['w'] + 1), team_list[i-1]['l'] + 1
        if scores[0] == scores[1]:
            team_list[0]['pts'], team_list[0]['d'] = (team_list[0]['pts'] + 1), (team_list[0]['d'] + 1)
            team_list[1]['pts'], team_list[1]['d'] = (team_list[1]['pts'] + 1), (team_list[1]['d'] + 1)
    input(f"Matchday {match_num} result: {team_list[0]['team']} {scores[0]} - {scores[1]} {team_list[1]['team']} >>> ")

def get_table(team_list):
    league_table = sorted(team_list, key=lambda x: x['pts'], reverse=True)
    league_table = [{a.upper():b for (a,b) in i.items() if a != 'name'} for i in league_table]
    output_table = tabulate(league_table, headers='keys', showindex=range(1,3))
    return output_table

def main():
    input("Welcome to LEAGUE BUILDER >>> ")
    input("Time to create your teams !!! >>> ")
    user_league = create_teams()
    while True:
        try:
            num_matches = abs(int(input("Enter the number that your teams will play: ")))
        except ValueError:
            input("Please enter a valid number >>> ")
        else:
            break
    for i in range(0, num_matches):
        match_day(user_league, i+1)
    print(get_table(user_league))

main()
