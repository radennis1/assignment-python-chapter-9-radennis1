from pathlib import Path
import json
import sqlite3

"""
Watch Mosh's video 9.8. You will need to install
DB Browser for SQLlite and learn how to create a table
"""


# Chapter 9.8- Working with a SQLite Database
print("\n9.8- Working with a SQLite Database" + "-" * 20)

# Another way to loop through a list of dictionaries. Important for Chapter 9.8 Databases
# a json file is a text files formated similar to a python dictionary
# Ryan Dennis
movies = json.loads(Path("movies.json").read_text())
print(movies)
for movie in movies:
    print(movie.values())

"""
Notes:
movies is a list of dictionaries, which were formerly in the json file
A dictionary is a list of key:value pairs.
A key is like a label name or variable name and a value is the value of the key.
Each row in the list is one dictionary object representing data about a movie
movie.values() returns only the values of a dictionary object,
the keys are ignored.
The for loop loops through each row in the list.
Therefore, each row of dictionary values is printed
"""

"""
How to write to a Sqlite3 database
create a connection to a database. If database doesn't exist, it will be created.
If you get an error 'sqlite3.OperationalError.No Such Table: Movies.'
follow Mosh's video on how to create a table using DB Browser for SQLite
print("Writing data")
"""

db_name = "db.sqlite3"
with sqlite3.connect(db_name) as conn:
    # format INSERT INTO with column names. Use ? marks for value placeholders
    sql_command = "INSERT INTO Movies (Id, Title, Year) VALUES (?, ?, ?)"
    # Loop through each row in list
    for movie in movies:
        # movies is a list of dictionaries previously read from a json file
        # movie is a dictionary
        # movie.values() returns dictionary values for a row in the list
        # must convert movie.values() to a tuple on line 53.
        # A tuple is like a list but cannot be mutated after creation
        movie_values = tuple(movie.values())
        # conn.execute() knows to replace the question marks in the
        # INSERT INTO statement with values from tuple(movies.value())
        conn.execute(sql_command, movie_values)
    # Save the changes to the database. Notice the indentation is outside
    # the for loop but inside with block
    conn.commit()
    print("Data written to the database")

    """
    Notes:
    1. If you get the error 'sqlite3.IntegrityError: UNIQUE constraint failed: Movies.Id'
    That's ok. It means you attempted to insert the same data multiple times.
    Continue with the next tasks.
    2. VERY IMPORTANT FOR FUTURE ASSIGNMENT:
    conn.execute(sql_command, values) requires a list or tuple as the values argument
    In this example, if movies was already a list or list of tuples,
    you would not need to convert movie to a tuple on line 53
    Because movie is a dictionary, we have to convert movie.values() to a tuple or a list
    on line 53 prior to conn.execute().
    Why is movie a dictionary, because movies is a list of dictionaries. Movies was created
    earlier by reading a json file. And a json file is a dictionary of key:value pairs.
    """
