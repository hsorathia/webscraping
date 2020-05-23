import requests, os
from bs4 import BeautifulSoup
from generate_urls import mol_links


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


def mol_html():
    urls = mol_links()
    path = os.getcwd() + '/books/mother_of_learning'
    if not os.path.exists(path):
        os.makedirs(path)

    for i in range(len(urls)):
        req = requests.get(urls[i], headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        html_input = soup.find_all('p')
        with open(os.path.join(path, 'chapter_' + str(i + 1) + '.tex'), 'w+') as chapter:
            chapter.write('\\documents{article}\n\\usepackage[utf8]{inputenc}\n\n')
            chapter.write('\\title{Mother of Learning - Chapter ' + str(i + 1) +' }\n')
            chapter.write('\\author{nobody103}\n\n\\begin{document}\n\\maketitle\n')
            for line in html_input:
                # process each line here
            chapter.write('\n\\end{document}')


mol_html()
