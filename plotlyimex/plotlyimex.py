# Copyright (c) 2023 ot2i7ba
# https://github.com/ot2i7ba/
# This code is licensed under the MIT License (see LICENSE for details).

"""
Imports a CSV file to generate an interactive map using plotly.
"""

import pandas as pd
import plotly.express as px
import plotly.io as pio
import os

# Ask user for CSV file name and add '.csv' file extension if missing
csv_file = input("Input csv filename (enter for 'import.csv'): ")
if csv_file == '':
    csv_file = 'import.csv'
else:
    if not csv_file.endswith('.csv'):
        csv_file += '.csv'

# Check if the file is a CSV file
if not os.path.isfile(csv_file):
    print("Error: The file '" + csv_file + "' could not be found.")
elif not os.path.splitext(csv_file)[1] == '.csv':
    print("Error: The file '" + csv_file + "' is not a CSV file.")
else:
    # Import CSV file
    df = pd.read_csv(csv_file)

    # Create map using scatter plot
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                            zoom=3)

    '''
    # Create map using density plot
    fig = px.density_mapbox(df, lat="latitude", lon="longitude", hover_name="id",
                            hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                            zoom=3)

    # Create map using lines plot
    fig = px.line_geo(df, lat="latitude", lon="longitude", hover_name="id",
                      hover_data=["userId", "lastSeenAt", "speed", "direction", "source"],
                      projection="orthographic")
    '''

    fig.update_layout(mapbox_style="open-street-map", height=1080, width=1920)
    #fig.update_layout(mapbox_style="carto-darkmatter", height=1080, width=1920)

    # Scale the height and width to 90%
    # fig.update_layout(height=0.9*fig.layout.height, width=0.9*fig.layout.width)

    # Automatically set the name of the exported file to the name of the imported file, if the user has entered a name
    html_file = input("Output html filename (enter for input filename): ")
    if html_file == '':
        html_file = os.path.splitext(csv_file)[0] + '.html'
    elif not html_file.endswith('.html'):
        html_file += '.html'

    # Display or save plot
    pio.show(fig)
    pio.write_html(fig, file=html_file)
    
