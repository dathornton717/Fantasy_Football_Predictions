import urllib2
from bs4 import BeautifulSoup
import csv
import os

qb_urls = ['http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/41',
    'http://www.espn.com/nfl/statistics/player/_/stat/passing/sort/passingYards/qualified/false/count/81']

qbs = []
qb_stats = ['name', 'team', 'comp', 'att', 'pct', 'yds', 'yds/a', 'long', 'td', 'int', 'sack', 'rate', 'yds/g']
qb_index = 0

for qb_url in qb_urls:
    qb_page = urllib2.urlopen(qb_url)
    qb_soup = BeautifulSoup(qb_page, 'html.parser')
    qb_table = qb_soup.find('table', attrs={'class':'tablehead'})
    qb_rows = qb_table.find_all('tr', attrs={'class':['oddrow', 'evenrow']})

    for qb_row in qb_rows:

        qbs.append({})
        qb_cols = qb_row.find_all('td')

        for index, qb_col in enumerate(qb_cols):
            if index == 0:
                continue

            qb_text = qb_col.text

            if ', ' in qb_text:
                comma_idx = qb_text.find(', ')
                qb_text = qb_text[:comma_idx]
            qbs[qb_index][qb_stats[index - 1]] = qb_text.strip()
        qb_index += 1

for qb in qbs:
    for stat in qb:
        print str(stat) + ' ' + qb[stat]

with open('qb_stats_2017_2018.csv', 'wb') as file:
    writer = csv.DictWriter(file, fieldnames = qb_stats, lineterminator=os.linesep)

    writer.writeheader()
    for qb in qbs:
        writer.writerow(qb)
