# Movie data registration report for a movie theater
    #### Video Demo:  <https://youtu.be/5Td2qCI47O4>
    #### Description:

    This Python project is a movie management application that allows you to add, store and export movie data. Below I provide you with a summary of its main functionalities:

    Film Representation:

    The Movie class is used to represent a movie, with attributes such as title, director, year, genre, and duration. Objects of the Movie class are stored in a list (movies).

    Program Functionality:

    Add a new movie: The add_movie() function prompts the user to enter a movie's data and then adds it to the movies list. Export to CSV: The export_csv() function saves movie data to a CSV file (by default called movies.csv). This file contains information about movies in a tabular format. Export to an SQLite database: The export_sql() function saves movie data to an SQLite database (movies.db by default). If the movies table does not exist, it creates it and then inserts each movie from the movies list into the database.

    Menu Interface:

    The menu() function provides a simple console interface where the user can:

    Add a new movie (option 1).

    Export the data to a CSV file (option 2).

    Export the data to a SQL database (option 3).

    Exit the program (option 4).

    The program remains in a loop until the user chooses to exit.
    
    In summary, this project allows users to manage a movie catalog, manually adding data and exporting it to both a CSV file and an SQLite database,
    making it easy to store and consult the information.
