import tkinter as tk
import json

class Movie:

    def __init__(self, movieName, movieDirector, movieActor, moviePublishDate):
        self.movieName = movieName
        self.movieDirector = movieDirector
        self.movieActor = movieActor
        self.moviePublishDate = moviePublishDate

class MovieLibrary:

    def __init__(self, db_file="movie_database.json"):
        self.db_file = db_file
        self.load_database()

    def load_database(self):
        try:
            with open(self.db_file, "r") as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            self.movies = []

    def save_database(self):
        with open(self.db_file, "w") as file:
            json.dump(self.movies, file)

    def addMovie(self, movie):
        self.movies.append(movie.__dict__)
        self.save_database()

    def deleteMovie(self, movie):
        if movie not in self.movies:
            print("There is no such a movie")
        else:
            self.movies.remove(movie)
            self.save_database()
            print(f"{movie['movieName']} removed from your library")

    def findMovie(self, movieName):
        for movie in self.movies:
            if movie['movieName'] == movieName:
                print(f"{movie['movieName']} exists in your library")
                return movie
        print("Movie not found!")
        return None

    def listMovies(self):
        if self.movies:
            return [Movie(**movie) for movie in self.movies]
        else:
            print("Your movie library is empty!")
            return []

class MovieApp:

    def __init__(self, master):
        self.master = master
        master.title("Movie Library")

        self.library = MovieLibrary()

        self.label = tk.Label(master, text="Welcome to Movie Library")
        self.label.pack()

        self.add_label = tk.Label(master, text="Enter movie details:")
        self.add_label.pack()

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.director_label = tk.Label(master, text="Director:")
        self.director_label.pack()
        self.director_entry = tk.Entry(master)
        self.director_entry.pack()

        self.actor_label = tk.Label(master, text="Actor(s):")
        self.actor_label.pack()
        self.actor_entry = tk.Entry(master)
        self.actor_entry.pack()

        self.publish_label = tk.Label(master, text="Publish Date:")
        self.publish_label.pack()
        self.publish_entry = tk.Entry(master)
        self.publish_entry.pack()

        self.add_button = tk.Button(master, text="Add Movie", command=self.add_movie)
        self.add_button.pack()

        self.delete_label = tk.Label(master, text="Enter movie name to delete:")
        self.delete_label.pack()
        self.delete_entry = tk.Entry(master)
        self.delete_entry.pack()
        self.delete_button = tk.Button(master, text="Delete Movie", command=self.delete_movie)
        self.delete_button.pack()

        self.list_button = tk.Button(master, text="List Movies", command=self.list_movies)
        self.list_button.pack()

        self.find_label = tk.Label(master, text="Enter movie name to find:")
        self.find_label.pack()
        self.find_entry = tk.Entry(master)
        self.find_entry.pack()
        self.find_button = tk.Button(master, text="Find Movie", command=self.find_movie)
        self.find_button.pack()

        master.geometry("600x400")

    def add_movie(self):
        movieName = self.name_entry.get()
        movieDirector = self.director_entry.get()
        movieActor = self.actor_entry.get().split(',')
        moviePublishDate = self.publish_entry.get()
        movie = Movie(movieName, movieDirector, movieActor, moviePublishDate)
        self.library.addMovie(movie)

    def delete_movie(self):
        movieName = self.delete_entry.get()
        movie = self.library.findMovie(movieName)
        if movie:
            self.library.deleteMovie(movie)

    def list_movies(self):
        print("Movie Library:")
        for movie in self.library.listMovies():
            print(f"Movie Name: {movie.movieName}, Director: {movie.movieDirector}, Actor: {movie.movieActor}, Published Date: {movie.moviePublishDate}\n")

    def find_movie(self):
        movieName = self.find_entry.get()
        self.library.findMovie(movieName)


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
