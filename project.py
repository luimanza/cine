import csv
import sqlite3

# Class to represent a movie
class Movie:
    def __init__(self, title, director, year, genre, duration):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.director} - {self.genre} - {self.duration} min"

# Array to store the movies
movies = []

# Function to add a movie
def add_movie():
    title = input("Movie title: ")
    director = input("Director: ")
    year = int(input("Release year: "))
    genre = input("Genre: ")
    duration = int(input("Duration (minutes): "))

    new_movie = Movie(title, director, year, genre, duration)
    movies.append(new_movie)
    print("\nMovie added successfully.\n")

# Function to export movies to a CSV file
def export_csv(file_name='movies.csv'):
    with open(file_name, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Director', 'Year', 'Genre', 'Duration'])
        for movie in movies:
            writer.writerow([movie.title, movie.director, movie.year, movie.genre, movie.duration])
    print(f"\nData exported to {file_name} successfully.\n")

# Function to export movies to a SQLite database
def export_sql(database_name='movies.db'):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            director TEXT,
            year INTEGER,
            genre TEXT,
            duration INTEGER
        )
    ''')

    # Insert movie data
    for movie in movies:
        cursor.execute('''
            INSERT INTO movies (title, director, year, genre, duration)
            VALUES (?, ?, ?, ?, ?)
        ''', (movie.title, movie.director, movie.year, movie.genre, movie.duration))

    connection.commit()
    connection.close()
    print(f"\nData exported to the database {database_name} successfully.\n")

# Function to initialize the database (could create tables or set up other elements)
def initialize_database(database_name='movies.db'):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            director TEXT,
            year INTEGER,
            genre TEXT,
            duration INTEGER
        )
    ''')
    connection.commit()
    connection.close()
    print(f"\nDatabase {database_name} initialized successfully.\n")

# Function to load movies from a CSV file
def load_movies_from_csv(file_name='movies.csv'):
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                movies.append(Movie(row['Title'], row['Director'], int(row['Year']), row['Genre'], int(row['Duration'])))
        print(f"\nMovies loaded from {file_name} successfully.\n")
    except FileNotFoundError:
        print(f"\nFile {file_name} not found. No movies loaded.\n")

# Function to run the main menu
def run_menu():
    while True:
        print("\n=== Movie Management ===")
        print("1. Add a new movie")
        print("2. Export data to CSV")
        print("3. Export data to SQL")
        print("4. Exit")

        option = input("Select an option: ")

        if option == '1':
            add_movie()
        elif option == '2':
            export_csv()
        elif option == '3':
            export_sql()
        elif option == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid option, please try again.")

# Main function to coordinate program flow
def main():
    initialize_database()  # Initialize the database, ensuring the table exists
    load_movies_from_csv() # Load existing movies from CSV (if present)
    run_menu()             # Run the main menu

# Run the main function if the script is the main program
if __name__ == "__main__":
    main()
