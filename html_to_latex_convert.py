import requests
import lxml.html
from lxml import etree
from io import StringIO, BytesIO

def html2latex(html_input):
    result = []
    for curr_element in html_input:
        print(curr_element)