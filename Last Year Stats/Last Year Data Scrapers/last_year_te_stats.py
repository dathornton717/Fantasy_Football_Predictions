import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
te_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=4&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=126&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=151&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=176&position=4&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

tes = {}

# the headers of the urls
te_stats = ['NAME', 'TEAM', 'PASS_YARDS', 'PASS_TD', 'INTERCEPTIONS',
    'RUSH_YARDS', 'RUSH_TD', 'REC_YARDS', 'REC_TD', 'FUM_TD', 'TWO_PT',
    'FUM_LOST']

for te_url in te_urls:
    # open the url
    te_page = requests.get(te_url)
    te_html = te_page.text

    te_soup = BeautifulSoup(te_html, 'html.parser')

    # get the player table
    te_table = te_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    te_rows = te_table.find_all('tr', attrs={'class':['odd', 'even']})

    for te_row in te_rows:
        te_cols = te_row.find_all('td')

        te_name = ''

        for index, te_col in enumerate(te_cols):
            if index == 0 or index == 2 or index == 13:
                continue

            te_text = te_col.text

            if 'TE' in te_text:
                te_idx = te_text.index('TE')

                view_video_idx = len(te_text)
                if 'View Videos' in te_text:
                    view_video_idx = te_text.index('View Videos')

                te_name = te_text[:te_idx - 1]

                te_team = 'NFL'
                if '-' in te_text:
                    te_team = te_text[te_idx + 5:view_video_idx - 1]
                tes[te_name] = {}
                tes[te_name]['NAME'] = te_name
                tes[te_name]['TEAM'] = te_team
                continue;

            if te_text == '-':
                te_text = '0'

            tes[te_name][te_stats[index - 1]] = te_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for te in tes:
#     #for stat in te:
#         #print str(stat) + ' ' + te[stat]

# write the quarterbacks out to a csv file
with open('te_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = te_stats, lineterminator=os.linesep)

    writer.writeheader()
    for te in tes:
        writer.writerow(tes[te])
