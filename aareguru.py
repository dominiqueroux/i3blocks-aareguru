#!/bin/python3

import os
from pyaare.pyaare import PyAare

# Set Bern as the default city, if there is none specified
default_city = "Bern"
default_threshold = 18.0

# Get the environment variables from i3blocks config
aare_city = os.environ.get('aare_city')
aare_threshold = os.environ.get('aare_threshold')

# Ensure a city is set (otherwise pyare will crash)
if aare_city is None:
    aare_city = default_city

if aare_threshold is None:
    aare_threshold = default_threshold


# Get the Aare temperature
aare = PyAare(city = aare_city)
temp = aare.tempC

# Decide if a jump into the Aare is encouraged or not
if temp < float(aare_threshold):
    color = '#FFFFFF'
    fulltext = "<span font='FontAwesome'>\uf773</span>" + " "
else:
    color = '#64C8FA'
    fulltext = "<span font='FontAwesome'>\uf5c4</span>" + " "

form =  '<span color="{}">{}°</span>'
fulltext += form.format(color,temp)

print(fulltext)
print(fulltext)
