import requests
from bs4 import BeautifulSoup
import csv
import os
import time

player_urls = ['http://fantasy.nfl.com/research/projections?position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=26&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=51&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=76&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=101&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=126&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=151&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=176&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=201&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=226&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=251&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=276&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=301&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=326&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=351&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=376&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=401&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=426&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=451&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=476&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=501&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=526&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=551&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=576&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=601&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=626&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=651&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=676&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=701&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=726&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=751&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=776&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=801&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=826&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=851&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=876&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=901&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=926&position=O&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1']

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
    player_table = player_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    player_rows = player_table.find_all('tr', attrs={'class':['odd', 'even']})

    for player_row in player_rows:
        player_cols = player_row.find_all('td')

        player_name = ''

        for index, player_col in enumerate(player_cols):
            if index == 1 or index == 2 or index == 13:
                continue

            player_text = player_col.text

            if 'QB' in player_text:
                player_idx = player_text.index('QB')

                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'QB'
            elif 'RB' in player_text:
                player_idx = player_text.index('RB')

                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'RB'
            elif 'WR' in player_text:
                player_idx = player_text.index('WR')

                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'WR'
            elif 'TE' in player_text:
                player_idx = player_text.index('TE')

                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'TE'

            if index == 0:
                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')

                player_team = 'NFL'
                if ' - ' in player_text:
                    player_team = player_text[player_idx + 5:view_video_idx - 1]
                if ' IR' in player_team:
                    player_team = player_team.replace(' IR', '')
                if ' SUS' in player_team:
                    player_team = player_team.replace(' SUS', '')
                if ' View News' in player_team:
                    player_team = player_team.replace(' View News', '')

                players[idx]['NAME'] = player_name
                players[idx]['TEAM'] = player_team
                players[idx]['SITE'] = 'NFL.com'
                continue;

            if player_text == '-':
                player_text = '0'

            players[idx][player_stats[index + 1]] = player_text.strip()

        idx += 1

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for player in players:
#     #for stat in player:
#         #print str(stat) + ' ' + player[stat]

# write the quarterbacks out to a csv file
with open('../Server/src/main/resources/csv/nfl_player_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
