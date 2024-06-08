class Song:
  count = 0  # Class attribute to track song creation count
  genres = []  # Class attribute to store unique genres
  artists = []  # Class attribute to store unique artists
  genre_count = {}  # Class attribute to store genre count

  def __init__(self, name, artist, genre):
    self.name = name
    self.artist = artist
    self.genre = genre
    

    # Increment song count and add to class attributes
    Song.add_song_to_count()
    Song.add_to_genres(genre)
    Song.add_to_artists(artist)
    Song.add_to_genre_count(genre)

  @classmethod
  def add_song_to_count(cls):
    cls.count += 1

  @classmethod
  def add_to_genres(cls, genre):
    if genre not in cls.genres:
      cls.genres.append(genre)

  @classmethod
  def add_to_artists(cls, artist):
    if artist not in cls.artists:
      cls.artists.append(artist)

  @classmethod
  def add_to_genre_count(cls, genre):
    cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
