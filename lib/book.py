#!/usr/bin/env python3

class Book: # create a class called Book
  def __init__(self, title, author): # runs automatically when a new instance of class is created
    self.title = title # saves the book's title
    self.author = author # saves the book's author
    self.page_count = 0 # starts the book at zero pages
    
  @property # creates new property named page_count
  def page_count(self):
    return self._page_count
  
  @page_count.setter # checks values before saving to page_count property
  def page_count(self, value):
    if not isinstance(value, int) or value < 0: # checks whether value is a non-negative integer 
      raise TypeError("Page count must be a non-negative integer") # rejects invalid values
    self._page_count = value # stores the validated value in a private attribute called _page_count
    
  def turn_page(self):
    self.page_count += 1