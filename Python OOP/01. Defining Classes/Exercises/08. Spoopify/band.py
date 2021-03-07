class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        try:
            existing_album = [a for a in self.albums if a.name == album.name][0]
            return f"Band {self.name} already has {album.name} in their library."
        except IndexError:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        try:
            current_album = [a for a in self.albums if a.name == album_name][0]
            if current_album.published:
                return f"Album has been published. It cannot be removed."
            self.albums.remove(current_album)
            return f"Album {album_name} has been removed."
        except IndexError:
            return f"Album {album_name} is not found."

    def details(self):
        res = f"Band {self.name}\n"
        for each in self.albums:
            res += f"{each.details()}\n"
        return res
