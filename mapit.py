import webbrowser, sys

sys.argv

# If address passed as command line arguments
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = ''

webbrowser.open('https://www.google.com/maps/place/' + address)
