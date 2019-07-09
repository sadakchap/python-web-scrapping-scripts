from bs4 import BeautifulSoup
import requests
import csv

f = open('cms_scrap.csv', 'w')
csv_writer = csv.writer(f)
csv_writer.writerow(['Headline', 'Summary', 'Video Link'])

source = requests.get('https://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('article', class_=["post", "type-post"]):
    heading = article.h2.a.text
    pst_lnk = article.h2.a['href']
    smry = article.find('div', class_='entry-content').p.text
    try:
        vid = article.find('iframe', class_="youtube-player")['src']
        vid_id = vid.rsplit('?')[0].split('/')[4]
        yt_lk = f'https://www.youtube.com/watch?v={vid_id}'
    except Exception:
        yt_lk = None

    print(heading, smry, yt_lk, sep='\n')
    csv_writer.writerow([heading, smry, yt_lk])
    print('-' * 80)
    # print(pst_lnk)


f.close()
