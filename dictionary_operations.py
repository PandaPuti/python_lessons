albums = {
    "Thriller": "1982-11-30",
    "Back in Black": "1980-07-25",
    "The Dark Side of the Moon": "1973-03-01",
    "The Bodyguard": "1992-11-17",
    "Rumours": "1977-02-04",
    "Saturday Night Fever": "1977-11-15",
    "Elton John - Greatest Hits": "1974-11-08",
    "Led Zeppelin IV": "1971-11-08",
    "Bad": "1987-08-31",
    "Jagged Little Pill": "1995-06-13",
    "Come On Over": "1997-11-04",
    "Sgt. Pepper's Lonely Hearts Club Band": "1967-05-26",
    "Falling into You": "1996-03-11",
    "Hotel California": "1976-12-08",
    "Dirty Dancing": "1987-08-21",
    "21": "2011-01-24",
    "Let's Talk About Love": "1997-11-14",
    "1": "2000-11-13",
    "Dangerous": "1991-11-26",
    "The Immaculate Collection": "1990-11-09"
}

def check_in_album(song):
  return song in albums
isInAlbum = check_in_album("Dirty Dancing")
answer =  'is' if isInAlbum else 'is not'
print(f"Dirty Dancing {answer} in the album")

def songs_in_album():
    return albums.keys()

def release_dates():
    return albums.values()
songs = songs_in_album()
songs = list(songs)
dates = list(release_dates())

print(f"the songs in the list: \n {songs}\n")
print(f"the release dates of the songs in the list: \n {dates}")
