#! /usr/bin/python
# Name: tryexcept.py
# Author: Chris
# Revision v1.0
# Description: Practicing using try except.


""" 
Doc String: 

Resource: https://runestone.academy/ns/books/published/fopp/Exceptions/Exercises.html 
"""


# If a blog post didn’t get any likes, a ‘Likes’ key should be added to that dictionary with a value of 0.

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, \
              {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

total_likes = 0

for post in blog_posts:
    try:
        total_likes = total_likes + post['Likes']
    except:
        post.update({'Likes': 0})


# The code below assigns the 5th letter of each word in food to the new list fifth.


food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []

for x in food:
    try:
        fifth.append(x[4])
    except:
        pass
