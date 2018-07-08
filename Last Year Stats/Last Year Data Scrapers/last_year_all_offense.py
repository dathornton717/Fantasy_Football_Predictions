import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
player_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=1&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?position=2&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=126&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=151&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=176&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=201&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=226&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?position=4&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=126&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=151&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=176&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?position=3&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=126&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=151&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=176&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=201&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=226&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=251&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=276&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=301&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=326&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=351&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=376&position=3&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

players = []
idx = 0

# the headers of the urls
player_stats = ['NAME', 'TEAM', 'POSITION', 'PASS_YARDS', 'PASS_TD',
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
            if index == 0 or index == 2 or index == 13:
                continue

            player_text = player_col.text

            if 'QB' in player_text:
                player_idx = player_text.index('QB')

                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')
                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'QB'
            elif 'RB' in player_text:
                player_idx = player_text.index('RB')

                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')
                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'RB'
            elif 'WR' in player_text:
                player_idx = player_text.index('WR')

                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')
                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'WR'
            elif 'TE' in player_text:
                player_idx = player_text.index('TE')

                view_video_idx = len(player_text)
                if 'View Videos' in player_text:
                    view_video_idx = player_text.index('View Videos')
                player_name = player_text[:player_idx - 1]
                players.append({})
                players[idx]['POSITION'] = 'TE'

            if index == 1:
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
                continue;

            if player_text == '-':
                player_text = '0'

            players[idx][player_stats[index]] = player_text.strip()

        idx += 1

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for player in players:
#     #for stat in player:
#         #print str(stat) + ' ' + player[stat]

# write the quarterbacks out to a csv file
with open('player_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
