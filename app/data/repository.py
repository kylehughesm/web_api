from abc import ABC, abstractmethod

class TrackRepository(ABC):
    def __init__(self): pass

    @abstractmethod 
    def get_tracks(self): pass

class GenreRepository(ABC):
    def __init__(self): pass

class AlbumRepository(ABC):
    def __init__(self): pass

    @abstractmethod
    def create(self, title, artist_id): pass
