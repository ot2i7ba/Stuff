## favorites
A simple PHP script which stores URLs submitted via bookmarklet. The URLs are stored in a text file, not in a database. By using a lockfile it tries to intercept write errors of the text file by multiple requests. Duplicate entries are intercepted as far as possible. Requests are limited as far as possible and clickjacking is prevented by means of X-Frame-Option-Headers. The script serves me in combination with the bookmarklet as a quick note possibility to read web pages later.

## pinkungfu
A Python script that generates possible PIN combinations based on user input and writes them to a text file. The output file can be splitted if desired. The generated text files can be imported into forensic software from Cellebrite to be used for bruteforce methods.
