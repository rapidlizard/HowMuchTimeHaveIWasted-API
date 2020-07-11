class User():

    def __init__(self, name: str, img: str, url: str, created: int, games: list, total_playtime: int):
        self.name = name
        self.img = img
        self.url = url
        self.created = created
        self.games = games
        self.total_playtime = total_playtime

    def to_json(self):
        return {
            'name': self.name,
            'img': self.img,
            'url': self.url,
            'created': self.created,
            'games': self.games,
            'total_playtime': self.total_playtime
        }
