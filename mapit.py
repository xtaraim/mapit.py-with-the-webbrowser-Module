#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.


#set up mapIt.py so that when you run it from the command line, like so...


C:\> mapit 870 Valencia St, San Francisco, CA 94110
# If you run the program by entering this into the command line...


mapit 870 Valencia St, San Francisco, CA 94110
... the sys.argv variable will contain this list value:


['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']
The address variable will contain the string '870 Valencia St, San Francisco, CA 94110'.
