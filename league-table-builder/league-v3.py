from tabulate import tabulate
from natural import number
from random import shuffle

def create_teams(num_teams):
    team_data = [dict.fromkeys(['name','team','p','pts','gd','gf','ga','w','d','l'], 0) for i in range(num_teams)]
    for i in range(num_teams):
        while True:
            try:
                team_name = input(f"Enter the name of your {number.ordinal(i+1)} team (must be 4 characters or more): ")
                team_abbr = input(f"Enter a 3-letter abbreviation for your {number.ordinal(i+1)} team: ").upper()
                if team_name in [i['name'] for i in team_data] or team_abbr in [i['team'] for i in team_data]: raise ValueError
                if len(team_name) < 4 or len(team_abbr) != 3: raise ZeroDivisionError
                team_data[i]['name'], team_data[i]['team'] = team_name, team_abbr
            except ValueError:
                input("One or more inputs already exist >>> ")
            except ZeroDivisionError:
                input("One or more inputs are invalid >>> ")
            else:
                break
    return team_data

def create_matches(team_list, multiplier):
    if multiplier == 2:
        combos = [f"{a['team']}-{b['team']}" for a in team_list for b in team_list if a['team'] != b['team']]
    else:
        combos = [f"{a['team']}-{b['team']}" for a in team_list for b in team_list[team_list.index(a):] if a['team'] != b['team']] * multiplier
    shuffle(combos)
    return combos

def match_day(team_list, matches):
    for i in range(len(matches)):
        t1 = [x for x in team_list if x['team'] == matches[i][:3]][0]
        t2 = [x for x in team_list if x['team'] == matches[i][4:]][0]
        input(f"Mathday {i+1}: {t1['name'].title()} vs {t2['name'].title()} >>> ")
        while True:
            try:
                s1 = abs(int(input(f"Enter the score for {t1['name']}: ")))
                s2 = abs(int(input(f"Enter the score for {t2['name']}: ")))
            except ValueError:
                input("One or more inputs are invalid >>> ")
            else:
                break
        t1['p'], t2['p'] = t1['p'] + 1, t2['p'] + 1
        t1['gd'], t1['gf'], t1['ga'] = t1['gd'] + (s1 - s2), t1['gf'] + s1, t1['ga'] + s2
        t2['gd'], t2['gf'], t2['ga'] = t2['gd'] + (s2 - s1), t2['gf'] + s2, t2['ga'] + s1
        if s1 > s2:
            t1['pts'], t1['w'], t2['l'] = t1['pts'] + 3, t1['w'] + 1, t2['l'] + 1
        elif s1 < s2:
            t2['pts'], t2['w'], t1['l'] = t2['pts'] + 3, t2['w'] + 1, t1['l'] + 1
        else:
            t1['pts'], t2['pts'], t1['d'], t2['d'] = t1['pts'] + 1, t2['pts'] + 1, t1['d'] + 1, t2['d'] + 1
        input(f"Matchday {i+1} result: {t1['team']} {s1} - {s2} {t2['team']} >>> ")

def print_table(team_list):
    league_table = [{a.upper():b for a,b in i.items() if a != 'name'} for i in team_list]
    league_table.sort(key=lambda x: x['PTS'], reverse=True)
    output_table = tabulate(league_table, headers='keys', showindex=range(1, len(league_table) + 1))
    print(output_table)

def main():
    input("Welcome to LEAGUE BUILDER >>> ")
    while True:
        try:
            num_teams = abs(int(input("Enter the number of teams that will play in your league: ")))
            num_fixtures = abs(int(input("Enter the number of times you want your teams to play eachother: ")))
        except ValueError:
            input("One or more inputs were invalid >>> ")
        else:
            break
    input("Time to create your teams >>> ")
    league = create_teams(num_teams)
    fixtures = create_matches(league, num_fixtures)
    input(f"There will be a total of {len(fixtures)} matches\nLet's get started >>> ")
    match_day(league, fixtures)
    print_table(league)

main()
