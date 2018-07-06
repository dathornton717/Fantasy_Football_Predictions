import urllib2
from bs4 import BeautifulSoup
import csv
import os

# urls to scrape from
qb_urls = ['http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/41',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/81']

qbs = []

# the headers of the urls
qb_stats = ['name', 'team', 'comp', 'att', 'pct', 'yds', 'yds/a', 'long', 'td', 'int', 'sack', 'rate', 'yds/g']
qb_index = 0

for qb_url in qb_urls:
    # open url
    qb_page = urllib2.urlopen(qb_url)

    qb_soup = BeautifulSoup(qb_page, 'html.parser')

    # get the player table
    qb_table = qb_soup.find('table', attrs={'class':'tablehead'})

    # get the player rows from the table
    qb_rows = qb_table.find_all('tr', attrs={'class':['oddrow', 'evenrow']})

    for qb_row in qb_rows:
        qbs.append({})
        qb_cols = qb_row.find_all('td')

        increment = True
        for index, qb_col in enumerate(qb_cols):
            # ignore the rank
            if index == 0:
                continue

            qb_text = qb_col.text

            # ignore if the player is not a quarterback
            if 'QB' not in qb_text and index == 1:
                qbs = qbs[:-1]
                increment = False
                break
            elif 'QB' in qb_text:
                qb_text = qb_text[:-4]

            # add to the quarterback array
            qbs[qb_index][qb_stats[index - 1]] = qb_text.strip()
        if increment:
            qb_index += 1

# if you want to print the quarterbacks
#for qb in qbs:
    #for stat in qb:
        #print str(stat) + ' ' + qb[stat]

# write the quarterbacks out to a csv file
with open('qb_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = qb_stats, lineterminator=os.linesep)

    writer.writeheader()
    for qb in qbs:
        writer.writerow(qb)
