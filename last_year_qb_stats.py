import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
qb_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=1&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=1&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

qbs = {}

# the headers of the urls
qb_stats = ['name', 'team', 'pass_yds', 'pass_td', 'int', 'rush_yds', 'rush_td',
    'rec_yds', 'rec_td', 'fum_td', 'two_pt', 'fum_lost']

for qb_url in qb_urls:
    # open the url
    qb_page = requests.get(qb_url)
    qb_html = qb_page.text

    qb_soup = BeautifulSoup(qb_html, 'html.parser')

    # get the player table
    qb_table = qb_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    qb_rows = qb_table.find_all('tr', attrs={'class':['odd', 'even']})

    for qb_row in qb_rows:
        qb_cols = qb_row.find_all('td')

        qb_name = ''

        for index, qb_col in enumerate(qb_cols):
            if index == 0 or index == 2 or index == 13:
                continue

            qb_text = qb_col.text

            if 'QB' in qb_text:
                qb_idx = qb_text.index('QB')

                view_video_idx = len(qb_text)
                if 'View Videos' in qb_text:
                    view_video_idx = qb_text.index('View Videos')

                qb_name = qb_text[:qb_idx - 1]

                qb_team = 'NFL'
                if '-' in qb_text:
                    qb_team = qb_text[qb_idx + 5:view_video_idx - 1]
                qbs[qb_name] = {}
                qbs[qb_name]['name'] = qb_name
                qbs[qb_name]['team'] = qb_team
                continue;

            if qb_text == '-':
                qb_text = '0'

            qbs[qb_name][qb_stats[index - 1]] = qb_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for qb in qbs:
#     #for stat in qb:
#         #print str(stat) + ' ' + qb[stat]

# write the quarterbacks out to a csv file
with open('qb_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = qb_stats, lineterminator=os.linesep)

    writer.writeheader()
    for qb in qbs:
        writer.writerow(qbs[qb])
