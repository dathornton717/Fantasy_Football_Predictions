import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
k_urls = ['http://fantasy.nfl.com/research/projections?position=7&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1',
    'http://fantasy.nfl.com/research/projections?offset=26&position=7&sort=projectedPts&statCategory=projectedStats&statSeason=2018&statType=seasonProjectedStats&statWeek=1']

ks = []

# the headers of the urls
k_stats = ['NAME', 'TEAM', 'SITE', 'PAT', 'TEENS', 'TWENTIES', 'THIRTIES', 'FORTIES',
    'FIFTIES']
idx = 0

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
            if index == 1 or index == 2 or index == 9:
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
                ks.append({})
                ks[idx]['NAME'] = k_name
                ks[idx]['TEAM'] = k_team
                ks[idx]['SITE'] = 'NFL.com'
                continue;

            if k_text == '-':
                k_text = '0'

            ks[idx][k_stats[index]] = k_text.strip()
        idx += 1

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for k in ks:
#     #for stat in k:
#         #print str(stat) + ' ' + k[stat]

# write the quarterbacks out to a csv file
with open('../Server/src/main/resources/nfl_k_stats_2018_2019.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = k_stats, lineterminator=os.linesep)

    writer.writeheader()
    for k in ks:
        writer.writerow(k)
