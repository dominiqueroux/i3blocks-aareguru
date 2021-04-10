#!/bin/python3

import os
from pyaare.pyaare import PyAare

# Set Bern as the default city, if there is none specified
default_city = "Bern"
default_threshold = 18.0

# Get the environment variables from i3blocks config
aare_city = os.environ.get('aare_city')
aare_threshold = os.environ.get('aare_threshold')

# Check if a mouse button was pressed
block_button = os.environ['BLOCK_BUTTON'] if 'BLOCK_BUTTON' in os.environ else None
block_button = int(block_button) if block_button else None

# Ensure a city is set (otherwise pyare will crash)
if aare_city is None:
    aare_city = default_city

if aare_threshold is None:
    aare_threshold = default_threshold

aare = PyAare(city = aare_city)
if block_button == 3:
    # Get forecast temperature
    temp = aare.tempC2h
else:
    # Get the Aare temperature
    temp = aare.tempC

if block_button == 2:
    # Get the flow and the corresponding text
    flow = aare.flow
    flow_text = aare.flowText

# Decide if a jump into the Aare is encouraged or not
if temp < float(aare_threshold):
    color = '#FFFFFF'
    fulltext = "<span font='FontAwesome'>\uf773</span> "
else:
    color = '#64C8FA'
    fulltext = "<span font='FontAwesome'>\uf5c4</span> "

if block_button == 3:
    fulltext += "<span>2h:</span> "

if block_button == 2:
    form =  '<span>{} m³/s: {}</span>'
    fulltext += form.format(flow,flow_text)
else:
    form =  '<span color="{}">{}°</span>'
    fulltext += form.format(color,temp)


print(fulltext)
print(fulltext)
