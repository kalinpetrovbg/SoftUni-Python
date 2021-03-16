class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]
        self.counter = 0
        self.page = 0
        self.max = 0

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):

        if self.max == self.pages * 4:
            return "No more free spots"

        if self.counter == 4:
            self.page += 1
            self.counter = 0
        self.photos[self.page].append(label)
        self.counter += 1
        self.max += 1


        return f"{label} photo added successfully on page {self.page +1} " \
               f"slot {self.counter}"

    def display(self):
        rep = '-----------\n'
        for page in self.photos:
            rep += ' '.join(['[]' for _ in range(len(page))])
            rep += '\n-----------\n'
        return rep

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("party with friends"))
print(album.add_photo("first grade"))
print(album.add_photo("one more but not valid"))

print(album.display())
