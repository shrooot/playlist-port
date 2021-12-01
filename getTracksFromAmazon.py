from bs4 import BeautifulSoup
import requests

def get_song_list(url):
    page = requests.get(url)
    html_doc = page.content
    soup = BeautifulSoup(html_doc, 'html.parser')

    music_links = soup.findAll("div", {"class": "col1"})

    song_titles = []
    for link in music_links:
            song_title = link.findChild("music-link")['title']
            # print(song_title)
            song_titles.append(song_title)
    return song_titles


playlist_url = "https://music.amazon.in/user-playlists/553f5b219e5345b0a39e99fd1d5547c7i8n0?marketplaceId=A3K6Y4MI8GDYMT&musicTerritory=IN&ref=dm_sh_DsftgjigplrRqvvgzgnIFlw3u"

# print(music_links.findChild("music-link")['title'])
# with open("songs.txt", 'w') as file:
#     for link in music_links:
#         song_title = link.findChild("music-link")['title']
#         print(song_title)
#         file.write(song_title + '\n')
# file.close()
        

