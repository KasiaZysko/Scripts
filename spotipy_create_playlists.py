import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_tracks():
    URL = "https://www.billboard.com/charts/hot-100/"
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get(URL + date)
    soup = BeautifulSoup(response.text, "html.parser")
    music = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
    music_artist = soup.find_all(name="span", class_="a-no-trucate")
    music_titles = [m.text.strip() for m in music]
    music_artists = [a.text.strip().split()[0] for a in music_artist]
    music_tracks = []
    for n in range(0, len(music_artists)-1):
        music_tracks.append(f"{music_titles[n]} {music_artists[n]}")
    return date, date.split("-")[0],  music_tracks


def spotify_auth():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=os.environ["SPOTIPY_REDIRECT_URI"],
        client_id=os.environ["SPOTIPY_CLIENT_ID"],
        client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
        show_dialog=True,
        cache_path="token.txt"))
    user_id = sp.current_user()["id"]
    return sp, user_id


def create_playlist():
    date, year, music_tracks = get_tracks()
    sp, user_id = spotify_auth()

    song_uris = []

    for song in music_tracks:
        result = sp.search(q=f"track: {song} year: {year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            continue

    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


if __name__ == '__main__':
    create_playlist()
