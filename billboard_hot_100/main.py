import os 
from os import name
import requests
from bs4 import BeautifulSoup
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID =  os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']

date = input(
    'Which year would you like to travel to? Type the date in YYYY-MM-DD format: \n')

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')
song_title = soup.find_all(
    name='h3', id='title-of-a-story', class_='u-letter-spacing-0021')

titles = [title.getText().strip() for title in song_title]
top_titles = [] # names of 100 songs
for title in titles:
    if title != 'Songwriter(s):' and title != 'Producer(s):' and title != 'Imprint/Promotion Label:':
        top_titles.append(title)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope='playlist-modify-private', 
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    show_dialog=True,
    cache_path='token.txt'
    ))
user_id = sp.current_user()["id"]

song_uris = []
year = date.split('-')[0]

for song in top_titles:
    result = sp.search(type='track', q=f"track:{song} year:{year}")
    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except: 
        print(f'Sorry, {song} does not exist on Spotify. It has been skipped.')

playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False, collaborative=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
