class StreamUser:
    def __init__(self, name, games, played_hours = 0):
        self.name = name
        self.games = games
        self.played_hours= played_hours
        
    def play(self, game, hours):
        if game in self.games:
            self.played_hours += hours
            return "{} is playing {}".format(self.name, game)
        else :
            return "{} is not in library".format(game)
    
    def buy_game(self, game):
        if game in self.games:
            return "{} is already in your library".format(game)
        else:
            self.games.append(game)
            return "{} bought {}".format(self.name, game)
    
    def stats(self):
        return "{} has {} games. Total play time: {}".format(self.name,len(self.games),self.played_hours)

user =  StreamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.stats())