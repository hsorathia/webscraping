import requests
import os
from links import links
# print(type(links[0]))
# zero = links[0]
# print(zero)
# print(zero.find("data-episodeURL"))
ok_chars = {':', '/', '.', '-'}
links_and_titles = []
print(links[0])
for link in links:
    # find the start index
    idx_begin = link.find("data-episodeURL=")
    
    # find the beginning of the actual link
    idx = link.find("https", idx_begin)
    curr_link = ''
    # keep iterating through and grab the entire link
    while link[idx] != ">":
        # we want chars, digits, and some special chars like /-
        if link[idx].isalpha() or link[idx].isdigit() or link[idx] in ok_chars:
            curr_link += link[idx]
        idx += 1

    # find the beginning of the title
    idx = link.find("<div>", idx)
    curr_title = ''
    idx += 4
    while link[idx] != "\\":
        if link[idx] == ' ':
            curr_title += '-'
        elif link[idx].isalpha() or link[idx].isdigit():
            curr_title += link[idx]
        idx += 1
    links_and_titles.append((curr_title, curr_link))

print(links_and_titles[0])
# # print(links_and_titles)

for title, url in links_and_titles:
    r = requests.get(url, allow_redirects=True)
    dirname = os.getcwd() + '/mp4/'
    mp4_title = os.path.join(dirname,  title + ".mp4")
    # if not os.path.exists(mp4_title):
    #     os.makedirs(mp4_title)
    with open(mp4_title, "wb") as f:
        f.write(r.content)
