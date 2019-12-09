import requests
from bs4 import BeautifulSoup
import random
"""
url = "https://www.youtube.com/results?search_query=relex%2Fstudy+music"
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")

for all_mv in soup.select(".yt-lockup-video"):
    data = all_mv.select("a[rel='spf-prefetch']")
    # print(data[0].get("title"))
    print("https://www.youtube.com{}".format(data[0].get("href")))

"""
def link(url_link):
    result = ""
    count = 0
    rnd = random.randint(1,5)
    url = url_link
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    for all_mv in soup.select(".yt-lockup-video"):
        data = all_mv.select("a[rel='spf-prefetch']")
        if(count == rnd):
            result = "https://www.youtube.com{}".format(data[0].get("href"))
        count += 1   
        # print(data[0].get("title"))
        # print("https://www.youtube.com{}".format(data[0].get("href")))
    
    return result

def trending_video(url_link):
    result = ""
    count = 0
    url = url_link
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    for all_mv in soup.select(".yt-lockup-video"):
        data = all_mv.select("a")
        if(count <= 5):
            result += "https://www.youtube.com{}\n\n".format(data[0].get("href"))
            count += 1
    
    return result      