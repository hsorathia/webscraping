from urllib.request import Request, urlopen
import time


def grab_page(url):

    # Make the http request for the resource
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(req)

    # Read the response body to a variable

    html = response.read()

    # Create a unique token for filename
    ts = time.time()

    # Generate a string for the filename
    filename = "scrape" + str(ts) + ".html"

    # Write html as a file to disk
    # f = open(filename, "w")
    with open(filename, 'w') as f:
        f.write(html.decode('utf-8'))


grab_page('https://muslimcentral.com/audio/jamal-zarabozo/')
