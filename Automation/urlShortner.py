"""
Example input : https://www.youtube.com/watch?v=4rURry0UFB8
"""

import pyshorteners

link = input("\nEnter your link : ")

short = pyshorteners.Shortener()
x = short.tinyurl.short(link)

print("\nShorted link is : "+x)