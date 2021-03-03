class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = [*songs]
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        try:
            existing_song = [s for s in self.songs if s.name == song.name][0]
            return f"Song is already in the album."
        except IndexError:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."
        try:
            existing = [s for s in self.songs if s.name == song_name][0]
            self.songs.remove(existing)
            return f"Removed song {song_name} from album {self.name}."
        except IndexError:
            return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        res = f"Album {self.name}\n"
        for each in self.songs:
            res += f"== {each.get_info()}\n"
        return res
