from bs4 import BeautifulSoup
import pandas as pd

file_path = "file.html" # Change the path to your html path

with open(file_path, 'r', encoding='utf-8') as file:
    page_content = file.read()

soup = BeautifulSoup(page_content, 'html.parser')

artists = []
releases = []
ratings = []

wishlisted_artists = []
wishlisted_releases = []

rows = soup.select('table.mbgen tr')

for row in rows[1:]:
    artist_elem = row.select_one('a.artist')
    release_elem = row.select_one('a.album')
    rating_elem = row.select_one('td.or_q_rating')

    artist = artist_elem.get_text(strip=True) if artist_elem else 'N/A'
    release = release_elem.get_text(strip=True) if release_elem else 'N/A'
    
    if artist == 'N/A' or release == 'N/A':
        continue
    
    if rating_elem and rating_elem.get_text(strip=True):
        rating = rating_elem.get_text(strip=True)
        artists.append(artist)
        releases.append(release)
        ratings.append(rating)
    else:
        wishlisted_artists.append(artist)
        wishlisted_releases.append(release)

data = pd.DataFrame({ # Rated Albums
    'Artist': artists,
    'Release': releases,
    'Rating': ratings
})

wishlisted_data = pd.DataFrame({ # Wishlisted albums
    'Artist': wishlisted_artists,
    'Release': wishlisted_releases
})

data.to_csv("music_data.csv", index=False)
wishlisted_data.to_csv("wishlisted_music_data.csv", index=False) # Commend this if you don't want wishlisted albums in csv
