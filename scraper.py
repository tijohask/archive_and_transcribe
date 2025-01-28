from bs4 import BeautifulSoup
import requests
import time

def make_rumble_request(channel, page_num, allow_redirects=True):
    request_url = f"{channel}?page={page_num}"
    return requests.get(
        request_url,
        headers={
            "Host": "rumble.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1"
        }
    )



def get_next_vid_link(channel):
    i = 1
    while True:
        req = make_rumble_request(channel, i)
        if req.status_code > 299:
            print(req.status_code)
            break
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        all_divs = soup.find_all('div', class_="videostream__footer")
        for div in all_divs:
            if ('videostream__footer--live' in div['class']):
                continue
            datetime = div.address.div.span.time['datetime']
            title = div.a.h3.string.strip()
            link = channel + div.a['href']
            json = {
                'datetime' : datetime,
                'title'    : title,
                'link'     : link,
            }
            yield json
        i = i + 1
