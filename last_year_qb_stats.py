import requests
from bs4 import BeautifulSoup
import csv
import os
import time

# urls to scrape from
qb_pass_urls = ['http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/41',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/81']

qb_rush_urls = ['http://www.espn.com/nfl/statistics/player/_/stat/rushing/qualified/false',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/41',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/81',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/121',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/161',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/201',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/241',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/281',
    'http://www.espn.com/nfl/statistics/player/_/stat/rushing/sort/rushingYards/qualified/false/count/321']

qbs = {}

# the headers of the urls
qb_stats = ['name', 'team', 'comp', 'pass_att', 'pct', 'pass_yds', 'pass_yds/a',
    'pass_long', 'pass_td', 'int', 'sack', 'rate', 'pass_yds/g', 'rush_att',
    'rush_yds', 'rush_yds/a', 'rush_long', 'rush_20+', 'rush_td', 'rush_yds/g',
    'fum', '1dn']
qb_pass_index = 0

for qb_pass_url in qb_pass_urls:
    # open url
    qb_pass_page = requests.get(qb_pass_url)
    qb_pass_html = qb_pass_page.text

    qb_pass_soup = BeautifulSoup(qb_pass_html, 'html.parser')

    # get the player table
    qb_table = qb_pass_soup.find('table', attrs={'class':'tablehead'})

    # get the player rows from the table
    qb_pass_rows = qb_table.find_all('tr', attrs={'class':['oddrow', 'evenrow']})

    for qb_pass_row in qb_pass_rows:
        qb_pass_cols = qb_pass_row.find_all('td')

        qb_name = ''

        for index, qb_pass_col in enumerate(qb_pass_cols):
            # ignore the rank
            if index == 0:
                continue

            qb_pass_text = qb_pass_col.text

            # ignore if the player is not a quarterback
            if 'QB' not in qb_pass_text and index == 1:
                break
            elif 'QB' in qb_pass_text:
                qb_pass_text = qb_pass_text[:-4]
                qb_name = qb_pass_text

            if index == 1:
                qbs[qb_pass_text] = {}

            # add to the quarterback array
            qbs[qb_name][qb_stats[index - 1]] = qb_pass_text.replace(',', '').strip()
    # sleep for 5 seconds
    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)

for qb_rush_url in qb_rush_urls:
    qb_rush_page = requests.get(qb_rush_url)
    qb_rush_html = qb_rush_page.text

    qb_rush_soup = BeautifulSoup(qb_rush_html, 'html.parser')
    qb_rush_table = qb_rush_soup.find('table', attrs={'class':'tablehead'})

    qb_rush_rows = qb_rush_table.find_all('tr', attrs={'class':['oddrow', 'evenrow']})

    for qb_rush_row in qb_rush_rows:
        qb_rush_cols = qb_rush_row.find_all('td')

        qb_name = ''

        for index, qb_rush_col in enumerate(qb_rush_cols):
            print str(index) + ' ' + qb_rush_col.text
            if index == 0:
                continue

            qb_rush_text = qb_rush_col.text

            if 'QB' not in qb_rush_text and index == 1:
                break
            elif 'QB' in qb_rush_text:
                qb_rush_text = qb_rush_text[:-4]
                qb_name = qb_rush_text

            if qb_name != '' and qb_name not in qbs:
                qbs[qb_name] = {}
                qbs[qb_name][qb_stats[0]] = qb_name
            if index == 1:
                continue

            if index == 2 and qb_stats[index - 1] not in qbs[qb_name]:
                qbs[qb_name][qb_stats[1]] = qb_rush_text.strip()

            if index == 2:
                continue

            print qb_name + ' ' + ' ' + str(index) + ' ' + qb_stats[index + 10]
            qbs[qb_name][qb_stats[index + 10]] = qb_rush_text.replace(',', '').strip()

    # sleep for 5 seconds
    print 'Done page of parsing. Sleeping for 5 seconds...'
    time.sleep(5)

for qb in qbs:
    for qb_stat in qb_stats:
        if qb_stat not in qbs[qb]:
            qbs[qb][qb_stat] = 0

# if you want to print the quarterbacks
#for qb in qbs:
    #for stat in qb:
        #print str(stat) + ' ' + qb[stat]

# write the quarterbacks out to a csv file
with open('qb_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = qb_stats, lineterminator=os.linesep)

    writer.writeheader()
    for qb in qbs:
        writer.writerow(qbs[qb])
