class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: '{self.movies}'"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: '{self.movies}'"

comedy_exp = Comedy()
print(comedy_exp.add_movie('Большой куш'))

drama_exp = Drama()
print (drama_exp.add_movie('Оружейный барон'))
