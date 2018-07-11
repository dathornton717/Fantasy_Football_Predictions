import requests
from bs4 import BeautifulSoup
import csv
import os
import time

def make_full_team(name):
    name = name.strip()
    if name == 'Cardinals':
        return 'Arizona Cardinals'
    elif name == 'Falcons':
        return 'Atlanta Falcons'
    elif name == 'Ravens':
        return 'Baltimore Ravens'
    elif name == 'Bills':
        return 'Buffalo Bills'
    elif name == 'Panthers':
        return 'Carolina Panthers'
    elif name == 'Bears':
        return 'Chicago Bears'
    elif name == 'Bengals':
        return 'Cincinnati Bengals'
    elif name == 'Browns':
        return 'Cleveland Browns'
    elif name == 'Cowboys':
        return 'Dallas Cowboys'
    elif name == 'Broncos':
        return 'Denver Broncos'
    elif name == 'Lions':
        return 'Detroit Lions'
    elif name == 'Packers':
        return 'Green Bay Packers'
    elif name == 'Texans':
        return 'Houston Texans'
    elif name == 'Colts':
        return 'Indianapolis Colts'
    elif name == 'Jaguars':
        return 'Jacksonville Jaguars'
    elif name == 'Chiefs':
        return 'Kansas City Chiefs'
    elif name == 'Dolphins':
        return 'Miami Dolphins'
    elif name == 'Vikings':
        return 'Minnesota Vikings'
    elif name == 'Patriots':
        return 'New England Patriots'
    elif name == 'Saints':
        return 'New Orleans Saints'
    elif name == 'Giants':
        return 'New York Giants'
    elif name == 'Jets':
        return 'New York Jets'
    elif name == 'Raiders':
        return 'Oakland Raiders'
    elif name == 'Eagles':
        return 'Philadelphia Eagles'
    elif name == 'Steelers':
        return 'Pittsburgh Steelers'
    elif name == 'Chargers':
        return 'Los Angeles Chargers'
    elif name == '49ers':
        return 'San Francisco 49ers'
    elif name == 'Seahawks':
        return 'Seattle Seahawks'
    elif name == 'Rams':
        return 'Los Angeles Rams'
    elif name == 'Buccaneers':
        return 'Tampa Bay Buccaneers'
    elif name == 'Titans':
        return 'Tennessee Titans'
    elif name == 'Redskins':
        return 'Washington Redskins'

player_urls = ['https://www.cbssports.com/fantasy/football/stats/weeklyprojections/DST/season/avg/standard']

players = []
idx = 0

# the headers of the urls
player_stats = ['NAME', 'SITE', 'SACK', 'INTERCEPTIONS', 'FUM_REC', 'SAFETIES',
    'TD', 'TWO_PT_RETURN', 'RET_TD', 'PTS_ALLOW']

for player_url in player_urls:
    # open the url
    player_page = requests.get(player_url)
    player_html = player_page.text

    player_soup = BeautifulSoup(player_html, 'html.parser')

    # get the player table
    player_table = player_soup.find('table', attrs={'class':'data compact'})

    # get the player rows from the table
    player_rows = player_table.find_all('tr', attrs={'class':['row1', 'row2']})
    player_rows.pop(0)

    for player_row in player_rows:
        player_cols = player_row.find_all('td')

        player_name = ''

        for index, player_col in enumerate(player_cols):
            if index == 3 or index == 8 or index == 9:
                continue

            player_name = ''

            player_text = player_col.text
            if index == 0:
                comma_index = player_text.index(',')
                print player_text[1:comma_index]
                player_name = make_full_team(player_text[:comma_index])
                print player_name
                players.append({})
                players[idx]['NAME'] = player_name
                players[idx]['SITE'] = 'cbssports.com'
                continue

            header_index = index
            if index == 1 or index == 2 or index == 7:
                header_index = index + 2
            elif index == 4:
                header_index = index - 2
            elif index == 5:
                header_index = index + 1
            elif index == 6:
                header_index = index - 1

            players[idx][player_stats[header_index]] = player_text.strip()

            for stat in player_stats:
                if stat not in players[idx]:
                    players[idx][stat] = 0
        idx += 1
    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)

# # if you want to print the defenses
# #for player in players:
#     #for stat in player:
#         #print str(stat) + ' ' + player[stat]

# # write the quarterbacks out to a csv file
with open('../Server/src/main/resources/csv/cbs_def_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
