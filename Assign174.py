"""Create two classes that inherit from another class.

Each child should have at least two of their own attributes."""

class Book:
    title='Please neter a title'
    author=' '
    pgCount = int
    entryNum= 0

class Movie(Book):
    movie=''
    genre=''    minutes=0

class Audio(Book):
    minutes=0
    reader=''

