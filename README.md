# favorites [PHP] [&#8594;](favorites)
A simple PHP script which stores URLs submitted via bookmarklet. The URLs are stored in a text file, not in a database. By using a lockfile it tries to intercept write errors of the text file by multiple requests. Duplicate entries are intercepted as far as possible. Requests are limited as far as possible and clickjacking is prevented by means of X-Frame-Option-Headers. The script serves me in combination with the bookmarklet as a quick note possibility to read web pages later.

# pinkungfu [Python] [&#8594;](pinkungfu)
A Python script that generates possible PIN combinations based on user input and writes them to a text file. The output file can be splitted if desired. The generated text files can be imported into forensic software such as from Cellebrite to be used for bruteforce methods.

# plotlyimex [Python] [&#8594;](plotlyimex)
The script imports a CSV file to display position data in an interactive map using plotly. The map is displayed by OpenStreetMap and saved in HTML format. The generated HTML file opens automatically. The user can specify a filename of the import and/or export file if desired.
