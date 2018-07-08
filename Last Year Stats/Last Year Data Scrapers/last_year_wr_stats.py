import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
wr_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=3&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
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

wrs = {}

# the headers of the urls
wr_stats = ['NAME', 'TEAM', 'PASS_YARDS', 'PASS_TD', 'INTERCEPTIONS',
    'RUSH_YARDS', 'RUSH_TD', 'REC_YARDS', 'REC_TD', 'FUM_TD', 'TWO_PT',
    'FUM_LOST']

for wr_url in wr_urls:
    # open the url
    wr_page = requests.get(wr_url)
    wr_html = wr_page.text

    wr_soup = BeautifulSoup(wr_html, 'html.parser')

    # get the player table
    wr_table = wr_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    wr_rows = wr_table.find_all('tr', attrs={'class':['odd', 'even']})

    for wr_row in wr_rows:
        wr_cols = wr_row.find_all('td')

        wr_name = ''

        for index, wr_col in enumerate(wr_cols):
            if index == 0 or index == 2 or index == 13:
                continue

            wr_text = wr_col.text

            if 'WR' in wr_text:
                wr_idx = wr_text.index('WR')

                view_video_idx = len(wr_text)
                if 'View Videos' in wr_text:
                    view_video_idx = wr_text.index('View Videos')

                wr_name = wr_text[:wr_idx - 1]

                wr_team = 'NFL'
                if '-' in wr_text:
                    wr_team = wr_text[wr_idx + 5:view_video_idx - 1]
                wrs[wr_name] = {}
                wrs[wr_name]['name'] = wr_name
                wrs[wr_name]['team'] = wr_team
                continue;

            if wr_text == '-':
                wr_text = '0'

            wrs[wr_name][wr_stats[index - 1]] = wr_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for wr in wrs:
#     #for stat in wr:
#         #print str(stat) + ' ' + wr[stat]

# write the quarterbacks out to a csv file
with open('wr_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = wr_stats, lineterminator=os.linesep)

    writer.writeheader()
    for wr in wrs:
        writer.writerow(wrs[wr])
