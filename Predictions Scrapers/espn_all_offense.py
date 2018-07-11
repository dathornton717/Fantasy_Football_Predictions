import requests
from bs4 import BeautifulSoup
import csv
import os
import time

player_urls = ['http://games.espn.com/ffl/tools/projections?',
    'http://games.espn.com/ffl/tools/projections?&startIndex=40',
    'http://games.espn.com/ffl/tools/projections?&startIndex=80',
    'http://games.espn.com/ffl/tools/projections?&startIndex=120',
    'http://games.espn.com/ffl/tools/projections?&startIndex=160',
    'http://games.espn.com/ffl/tools/projections?&startIndex=200',
    'http://games.espn.com/ffl/tools/projections?&startIndex=240',
    'http://games.espn.com/ffl/tools/projections?&startIndex=280',
    'http://games.espn.com/ffl/tools/projections?&startIndex=320',
    'http://games.espn.com/ffl/tools/projections?&startIndex=360',
    'http://games.espn.com/ffl/tools/projections?&startIndex=400',
    'http://games.espn.com/ffl/tools/projections?&startIndex=440',
    'http://games.espn.com/ffl/tools/projections?&startIndex=480',
    'http://games.espn.com/ffl/tools/projections?&startIndex=520',
    'http://games.espn.com/ffl/tools/projections?&startIndex=560',
    'http://games.espn.com/ffl/tools/projections?&startIndex=600',
    'http://games.espn.com/ffl/tools/projections?&startIndex=640',
    'http://games.espn.com/ffl/tools/projections?&startIndex=680',
    'http://games.espn.com/ffl/tools/projections?&startIndex=720',
    'http://games.espn.com/ffl/tools/projections?&startIndex=760',
    'http://games.espn.com/ffl/tools/projections?&startIndex=800',
    'http://games.espn.com/ffl/tools/projections?&startIndex=840',
    'http://games.espn.com/ffl/tools/projections?&startIndex=880',
    'http://games.espn.com/ffl/tools/projections?&startIndex=920',
    'http://games.espn.com/ffl/tools/projections?&startIndex=960']

players = []
idx = 0

# the headers of the urls
player_stats = ['NAME', 'TEAM', 'SITE', 'POSITION', 'PASS_YARDS', 'PASS_TD',
    'INTERCEPTIONS', 'RUSH_YARDS', 'RUSH_TD', 'REC_YARDS', 'REC_TD', 'FUM_TD',
    'TWO_PT', 'FUM_LOST']

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

        player_name = ''

        for index, player_col in enumerate(player_cols):
            if (index == 0 or index == 2 or index == 6 or index == 9
                    or index == 12):
                continue

            player_text = player_col.text

            if index == 1:
                if 'D/ST' in player_text:
                    idx -= 1
                    break
                comma_idx = player_text.index(',')
                player_team = player_text[comma_idx + 2:]
                player_team = player_team[:3]
                player_team = player_team.strip()
                team_idx = player_text.index(player_team)
                position = player_text[team_idx + 3: team_idx + 7].strip()
                if position == 'K':
                    idx -= 1
                    break

            if 'K ' in player_text or 'DEF' in player_text:
                idx -= 1
                break

            if 'QB' in player_text:
                comma_idx = player_text.index(',')

                player_name = player_text[:comma_idx]
                players.append({})
                players[idx]['POSITION'] = 'QB'
            elif 'RB' in player_text:
                comma_idx = player_text.index(',')

                player_name = player_text[:comma_idx]
                players.append({})
                players[idx]['POSITION'] = 'RB'
            elif 'WR' in player_text:
                comma_idx = player_text.index(',')

                player_name = player_text[:comma_idx]
                players.append({})
                players[idx]['POSITION'] = 'WR'
            elif 'TE' in player_text:
                comma_idx = player_text.index(',')

                player_name = player_text[:comma_idx]
                players.append({})
                players[idx]['POSITION'] = 'TE'

            if index == 1:
                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')

                player_team = 'NFL'
                if ',' in player_text:
                    comma_idx = player_text.index(',')
                    player_team = player_text[comma_idx + 2:]
                    player_team = player_team[:3]
                    player_team = player_team.strip()
                    player_team = player_team.upper()

                players[idx]['NAME'] = player_name
                players[idx]['TEAM'] = player_team
                players[idx]['SITE'] = 'ESPN.com'
                continue;

            if player_text == '-':
                player_text = '0'

            header_index = index
            if index == 3 or index == 4 or index == 5:
                header_index = index + 1
            elif index == 10 or index == 11:
                header_index = index - 1

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
with open('../Server/src/main/resources/csv/espn_player_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
