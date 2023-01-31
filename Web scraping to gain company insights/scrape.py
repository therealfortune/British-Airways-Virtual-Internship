from bs4 import BeautifulSoup
import requests 
import re
import csv 
import time

url = 'https://www.airlinequality.com/lounge-reviews/british-airways/?sortby=post_date%3ADesc&pagesize=10'
f = requests.get(url).text 

soup = BeautifulSoup(f, 'html.parser')

csv_file = open('LoungeA.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rating', 'Name', 'Date', 'Country', 'A', 'B', 'C', 'D', 'E', 'Recommended'])

for article in soup.find_all('article'):
    rating = article.find('div', itemprop = 'reviewRating')
    if rating is not None:
        rating = article.find('div', itemprop = 'reviewRating').text
        rating = rating.strip()
    else: 
        continue

    he3 = article.h3
    if he3 is not None:
        he3 = article.h3.text
    else:
        continue
    name = article.h3.find('span', itemprop = 'name').text
    date = article.h3.time.text
    try:
        country = re.search('\(([^)]+)', he3).group(1)
    except AttributeError:
        country = None
    labels = article.find('div', class_ = 'tc_mobile').text
    header = article.find('div', class_ = 'tc_mobile')

    table = header.table
    check  = header.table.find('td', class_ = 'type_of_traveller')
    verified = header.em
    if verified is not None:
        verified = header.em.text
    else:
        continue
    try:
        try:
            recommended = seats.find('td', class_='review-value rating-yes').text
        except:
            recommended = seats.find('td', class_='review-value rating-no').text
    except AttributeError:
        recommended = None
    

    labels = article.find('div', class_='tc_mobile')
    seats = labels 
    if seats is not None:
        table = labels.find('table', class_='review-ratings')
    else:
        continue

    seats = labels.find('table', class_='review-ratings')
    
    a = []
    count = 0
    for tr in seats.find_all('tr'):
        td = tr.find('td', class_='review-value')
        if td is not None:
            td = tr.find('td', class_='review-value').text
            a.append(td)
        else:
            continue
        count += 1
    if count == 5:
        A = a[0]
        B = a[1]
        C = a[2]
        D = a[3]
        E = a[4]

        csv_writer.writerow([rating, name, date, country, A, B, C, D, E,recommended ])

        # print('Rating: ', rating)
        # print('Name: ', name)
        # print('Date', date)
        # print('Country: ', country)
        # print('A :', A)
        # print('B', B)
        # print('C', C)
        # print('D', D)
        # print('E', E)


    elif count == 6:
        A = a[0]
        B = a[1]
        C = a[2]
        D = a[3]
        E = a[4]
        csv_writer.writerow([rating, name, date, country, A, B, C, D, E,recommended])

        # print('Rating: ', rating)
        # print('Name: ', name)
        # print('Date', date)
        # print('Country: ', country)
        # print('A :', A)
        # print('B', B)
        # print('C', C)
        # print('D', D)
        # print('E', E)
    # print()

csv_file.close()

