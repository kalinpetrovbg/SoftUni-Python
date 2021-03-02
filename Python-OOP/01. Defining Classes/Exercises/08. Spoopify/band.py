class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f'Band {self.name} already has {album.name} in their library.'
        self.albums.append(album)
        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name):
        if album_name not in [a.name for a in self.albums]:
            return f'Album {album_name} is not found.'
        a = [a for a in self.albums if a.name == album_name][0]
        if a.published:
            return 'Album has been published. It cannot be removed.'
        self.albums.remove(a)
        return f'Album {album_name} has been removed.'

    def details(self):
        result = f'Band {self.name}\n'
        for album in self.albums:
            result += album.details()
        return result

