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

player_urls = ['http://games.espn.com/ffl/tools/projections?&slotCategoryId=16']

players = []
idx = 0

# the headers of the urls
player_stats = ['NAME', 'SITE', 'SACK', 'INTERCEPTIONS', 'FUM_REC', 'SAFETIES', 'TD',
    'TWO_PT_RETURN', 'RET_TD', 'PTS_ALLOW']

for player_url in player_urls:
    # open the url
    player_page = requests.get(player_url)
    player_html = player_page.text

    player_soup = BeautifulSoup(player_html, 'html.parser')

    # get the player table
    player_table = player_soup.find('table', attrs={'class':'playerTableTable'})

    # get the player rows from the table
    player_rows = player_table.find_all('tr', attrs={'class':'pncPlayerRow'})

    for player_row in player_rows:
        player_cols = player_row.find_all('td')

        for index, player_col in enumerate(player_cols):
            if index == 0 or index == 2 or index == 4 or index == 9:
                continue

            player_text = player_col.text

            if index == 1:
                d_idx = player_text.index('D/ST')
                player_name = player_text[:d_idx - 1]
                player_name = make_full_team(player_name)
                players.append({})
                players[idx]['NAME'] = player_name
                players[idx]['SITE'] = 'ESPN.com'
                continue;

            if player_text == '-':
                player_text = '0'

            if index == 7:
                temp_td = float(player_text.strip())
                continue
            elif index == 8:
                temp_td += float(player_text.strip())
                players[idx]['TD'] = str(temp_td)
                continue

            header_index = index
            if index == 3 or index == 5:
                header_index = index - 1
            elif index == 6:
                header_index = index - 3

            players[idx][player_stats[header_index]] = player_text.strip()

            for stat in player_stats:
                if stat not in players[idx]:
                    players[idx][stat] = 0

        idx += 1

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for player in players:
#     #for stat in player:
#         #print str(stat) + ' ' + player[stat]

# write the quarterbacks out to a csv file
with open('../Server/src/main/resources/csv/espn_def_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
