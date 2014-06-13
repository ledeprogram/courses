#
# BABY QUAKEBOT!
#
# https://source.opennews.org/en-US/articles/how-break-news-while-you-sleep/
#
#
# This is a python file, so you're going to run them from the 
# command line by going to the folder it's in and running this terminal
# command...
#
#   python eq_homework.py
#
# Then a little magic will happen! Unfortunately, to make a lot of magic
# happen you'll need to fill in the functions below.
# 

# The info that comes from USGS looks something like this:

earthquake = {
  'rms': '1.85', 
  'updated': '2014-06-11T05:22:21.596Z', 
  'type': 'earthquake', 
  'magType': 'mwp', 
  'longitude': '-136.6561', 
  'gap': '48', 
  'depth': '10', 
  'dmin': '0.811', 
  'mag': '5.7', 
  'time': '2014-06-04T11:58:58.200Z', 
  'latitude': '59.0001', 
  'place': '73km WSW of Haines, Alaska', 
  'net': 'us', 
  'nst': '', 
  'id': 'usc000rauc'}
  
# We're going to break it into pieces and see if we can make a nice little version of Quakebot.

# If there was an earthquake, it might say this
#
#   There was a big earthquake Monday morning a ways away from Haines, Alaska
#
# But what if it was huge, or tiny, or just medium-sized? Or not near Haines at all?
# Let's see what we can do using functions to make this magic happen.


# PROBLEM 1:
# Let's make the print statement reflect the size of the earthquake
#
# Write a function that describes each earthquake using a scale similar to the
# one at the link below.
#
# Hint: You'll use if statements
#
# http://www.sdgs.usd.edu/publications/maps/earthquakes/images/RichterScale.gif

def earthquake_size(richter_measurement):
    return "large"
    
    
# PROBLEM 2:
# Let's make the print statement reflect the depth of the earthquake
#
# Make a function that describes each earthquake using a depth according to
# the information at the linke below
#
# http://earthquake.usgs.gov/learn/topics/seismology/determining_depth.php
#
# Hint: You'll use if statements, and be careful about types!


def earthquake_depth(depth):
    return "shallow"
    
    
# PROBLEM 3:
# Let's make the print statement reflect the location the earthquake
# happened by
# 
# Use regular expressions to extract the location from the argument location_string
# *or* research the 'split' function and see if it can be of use if you pass
# it a certain special separator

def earthquake_location(location_string):
    return "Haines, Alaska"


# PROBLEM 4:
# Let's make the print statement reflect the distance between the earthquake
# and the city
#
# You'll want to use several different categories, ie 'nearby', 
# 'far away from', and 'nowhere near'
#
# Hint: You'll use regular expressions to extract the kilometers from location_string,
# then use if statements on the result
#

def earthquake_distance(location_string):
    return "near"

# PROBLEM 5 & 6:
#
# Don't worry about these two functions yet.
#
#

def earthquake_day(time_string):
    return "Monday"

def earthquake_time(time_string):
    return "morning"

print "There was a " + earthquake_size(1.1) + \
        ", " + earthquake_depth('0.1') + \
        " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_day('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_distance("73km WSW of Haines, Alaska") + \
        " " + earthquake_location("73km WSW of Haines, Alaska")

print "There was a " + earthquake_size(8.7) + \
        ", " + earthquake_depth('98.22') + \
        " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_distance("238km N of Tobelo, Indonesia") + \
        " " + earthquake_location("238km N of Tobelo, Indonesia")

print "There was a " + earthquake_size(3.3) + \
        ", " + earthquake_depth('344.32') + \
        " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_distance("10km NE of Medford, Oklahoma") + \
        " " + earthquake_location("10km NE of Medford, Oklahoma")

print "There was a " + earthquake_size(6.1) + \
        ", " + earthquake_depth(5.289) + \
        " earthquake " + earthquake_day('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_time('2014-06-04T11:58:58.200Z') + \
        " " + earthquake_distance("91km NE of Miches, Dominican Republic") + \
        " " + earthquake_location("91km NE of Miches, Dominican Republic")
