import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
rb_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=2&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=51&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=76&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=101&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=126&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=151&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=176&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=201&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=226&position=2&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

rbs = {}

# the headers of the urls
rb_stats = ['NAME', 'TEAM', 'PASS_YARDS', 'PASS_TD', 'INTERCEPTIONS',
    'RUSH_YARDS', 'RUSH_TD', 'REC_YARDS', 'REC_TD', 'FUM_TD', 'TWO_PT',
    'FUM_LOST']

for rb_url in rb_urls:
    # open the url
    rb_page = requests.get(rb_url)
    rb_html = rb_page.text

    rb_soup = BeautifulSoup(rb_html, 'html.parser')

    # get the player table
    rb_table = rb_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    rb_rows = rb_table.find_all('tr', attrs={'class':['odd', 'even']})

    for rb_row in rb_rows:
        rb_cols = rb_row.find_all('td')

        rb_name = ''

        for index, rb_col in enumerate(rb_cols):
            if index == 0 or index == 2 or index == 13:
                continue

            rb_text = rb_col.text

            if 'RB' in rb_text:
                rb_idx = rb_text.index('RB')

                view_video_idx = len(rb_text)
                if 'View Videos' in rb_text:
                    view_video_idx = rb_text.index('View Videos')

                rb_name = rb_text[:rb_idx - 1]

                rb_team = 'NFL'
                if '-' in rb_text:
                    rb_team = rb_text[rb_idx + 5:view_video_idx - 1]
                rbs[rb_name] = {}
                rbs[rb_name]['NAME'] = rb_name
                rbs[rb_name]['TEAM'] = rb_team
                continue;

            if rb_text == '-':
                rb_text = '0'

            rbs[rb_name][rb_stats[index - 1]] = rb_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for rb in rbs:
#     #for stat in rb:
#         #print str(stat) + ' ' + rb[stat]

# write the quarterbacks out to a csv file
with open('rb_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = rb_stats, lineterminator=os.linesep)

    writer.writeheader()
    for rb in rbs:
        writer.writerow(rbs[rb])
