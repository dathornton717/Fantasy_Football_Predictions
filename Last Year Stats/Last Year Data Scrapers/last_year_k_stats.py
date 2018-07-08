import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
k_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=7&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=7&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

ks = {}

# the headers of the urls
k_stats = ['NAME', 'TEAM', 'PAT', 'TEENS', 'TWENTIES', 'THIRTIES', 'FORTIES',
    'FIFTIES']

for k_url in k_urls:
    # open the url
    k_page = requests.get(k_url)
    k_html = k_page.text

    k_soup = BeautifulSoup(k_html, 'html.parser')

    # get the player table
    k_table = k_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    k_rows = k_table.find_all('tr', attrs={'class':['odd', 'even']})

    for k_row in k_rows:
        k_cols = k_row.find_all('td')

        k_name = ''

        for index, k_col in enumerate(k_cols):
            if index == 0 or index == 2 or index == 9:
                continue

            k_text = k_col.text

            if 'K ' in k_text:
                k_idx = k_text.index('K ')

                view_video_idx = len(k_text)
                if 'View Videos' in k_text:
                    view_video_idx = k_text.index('View Videos')

                k_name = k_text[:k_idx - 1]

                k_team = 'NFL'
                if '-' in k_text:
                    k_team = k_text[k_idx + 4:view_video_idx - 1]
                ks[k_name] = {}
                ks[k_name]['name'] = k_name
                ks[k_name]['team'] = k_team
                continue;

            if k_text == '-':
                k_text = '0'

            ks[k_name][k_stats[index - 1]] = k_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for k in ks:
#     #for stat in k:
#         #print str(stat) + ' ' + k[stat]

# write the quarterbacks out to a csv file
with open('k_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = k_stats, lineterminator=os.linesep)

    writer.writeheader()
    for k in ks:
        writer.writerow(ks[k])
