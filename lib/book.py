#!/usr/bin/env python3

class Book: # create a class called Book
  def __init__(self, title, author): # runs automatically when a new instance of class is created
    self.title = title # saves the book's title
    self.author = author # saves the book's author
    self.page_count = 0 # starts the book at zero pages