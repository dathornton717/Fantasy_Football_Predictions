import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
def_urls = ['http://fantasy.nfl.com/research/scoringleaders?position=8&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1',
    'http://fantasy.nfl.com/research/scoringleaders?offset=26&position=8&sort=pts&statCategory=stats&statSeason=2017&statType=seasonStats&statWeek=1']

defs = {}

# the headers of the urls
def_stats = ['NAME', 'SACK', 'INTERCEPTIONS', 'FUM_REC', 'SAFETIES', 'TD',
    'TWO_PT_RETURN', 'RET_TD', 'PTS_ALLOW']

for def_url in def_urls:
    # open the url
    def_page = requests.get(def_url)
    def_html = def_page.text

    def_soup = BeautifulSoup(def_html, 'html.parser')

    # get the player table
    def_table = def_soup.find('table', attrs={'class':'tableType-player'})

    # get the player rows from the table
    def_rows = def_table.find_all('tr', attrs={'class':['odd', 'even']})

    for def_row in def_rows:
        def_cols = def_row.find_all('td')

        def_name = ''

        for index, def_col in enumerate(def_cols):
            if index == 0 or index == 2 or index == 11:
                continue

            def_text = def_col.text

            if 'DEF' in def_text:
                def_idx = def_text.index('DEF')

                view_video_idx = len(def_text)
                if 'View Videos' in def_text:
                    view_video_idx = def_text.index('View Videos')

                def_name = def_text[:def_idx - 1]

                defs[def_name] = {}
                defs[def_name]['name'] = def_name
                continue;

            if def_text == '-':
                def_text = '0'

            defs[def_name][def_stats[index - 2]] = def_text.strip()

    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)


# # if you want to print the quarterbacks
# #for def1 in defs:
#     #for stat in def1:
#         #print str(stat) + ' ' + def1[stat]

# write the quarterbacks out to a csv file
with open('def_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = def_stats, lineterminator=os.linesep)

    writer.writeheader()
    for def1 in defs:
        writer.writerow(defs[def1])
