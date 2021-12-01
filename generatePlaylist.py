import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth
from fuzzywuzzy import fuzz
from getTracksFromAmazon import get_song_list

client_id = "ADD YOUR CLIENT ID"
client_secret = "ADD YOUR SECRET TOKEN"
user_id = "ADD YOUR USER-ID ie SPOTIFY USERNAME"
scope = "playlist-modify-public"

token = util.prompt_for_user_token(username=user_id, scope=scope, client_id=client_id,
                                   client_secret=client_secret, redirect_uri='http://localhost:8080/')
sp = spotipy.Spotify(auth=token)


def create_playlist(playlist_name, desc):
    sp.user_playlist_create(user=user_id, name=playlist_name, description=desc)


def getTrackIDs(titles):
    track_ids = []

    for i in range(len(titles)):
        results = sp.search(q={titles[i]}, limit=5, type='track')

        if results['tracks']['total'] == 0:
            continue

        else:
            for j in range(len(results['tracks']['items'])):

                if fuzz.partial_ratio(results['tracks']['items'][j]['name'], titles[i]) > 90:
                    track_ids.append(results['tracks']['items'][j]['id'])
                    break
                else:
                    continue

    return track_ids


def getPlaylistID(username, playlist_name):
    playlist_id = ''
    playlists = sp.user_playlists(username)
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            playlist_id = playlist['id']
    return playlist_id


def add_all_tracks_to_playlist(username, playlist_id, track_ids):
    sp.user_playlist_add_tracks(username, playlist_id, track_ids)


playlist_name = "Rock Vibe"
desc = "A collection of classic rock songs"
amazon_url = "https://music.amazon.in/user-playlists/553f5b219e5345b0a39e99fd1d5547c7i8n0?marketplaceId=A3K6Y4MI8GDYMT&musicTerritory=IN&ref=dm_sh_DsftgjigplrRqvvgzgnIFlw3u"

song_list = get_song_list(amazon_url)
print(len(song_list))

track_ids = getTrackIDs(titles=song_list)

playlist_id = getPlaylistID(user_id,playlist_name)

add_all_tracks_to_playlist(username=user_id,playlist_id=playlist_id,track_ids=track_ids)
