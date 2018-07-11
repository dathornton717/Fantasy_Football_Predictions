import requests
from bs4 import BeautifulSoup
import csv
import os
import time

player_urls = ['https://www.cbssports.com/fantasy/football/stats/weeklyprojections/K/season/avg/standard']

players = []
idx = 0

# the headers of the urls
player_stats = ['NAME', 'TEAM', 'SITE', 'PAT', 'TEENS', 'TWENTIES', 'THIRTIES', 'FORTIES',
    'FIFTIES']

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
            if index == 2 or index == 4:
                continue

            player_name = ''

            player_text = player_col.text
            if index == 0:
                comma_index = player_text.index(',')
                player_name = player_text[:comma_index]
                player_team = player_text[comma_index + 2:]
                players.append({})
                players[idx]['NAME'] = player_name
                players[idx]['TEAM'] = player_team
                players[idx]['SITE'] = 'cbssports.com'
                continue

            header_index = index
            if index == 1:
                header_index = index + 5

            players[idx][player_stats[header_index]] = player_text.strip()

            for stat in player_stats:
                if stat not in players[idx]:
                    players[idx][stat] = 0
        idx += 1
    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)

# # if you want to print the wide receivers
# #for player in players:
#     #for stat in player:
#         #print str(stat) + ' ' + player[stat]

# # write the quarterbacks out to a csv file
with open('../Server/src/main/resources/csv/cbs_k_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = player_stats, lineterminator=os.linesep)

    writer.writeheader()
    for player in players:
        writer.writerow(player)
