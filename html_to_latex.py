import requests
import os
from bs4 import BeautifulSoup
from generate_urls import mol_links


headers = requests.utils.default_headers()
headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})


def mol_html():
    urls = mol_links()
    path = os.getcwd() + '/books/mother_of_learning'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(os.path.join(path, 'MotherOfLearning.tex'), 'w+') as book:
        book.write('\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\n')
        book.write('\\title{Mother of Learning}\n')
        book.write('\\author{nobody103}\n\n\\begin{document}\n\\maketitle\n\n')
        for i in range(len(urls)):
            book.write('\n\\section{Chapter ' + str(i + 1) + '}\n\n\n')
            req = requests.get(urls[i], headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            html_input = soup.find_all('p')
            # bolded_words = html_input.html.find_all('strong')
            # if len(bolded_words) > 1:
            #     for i in range(len(bolded_words)):
            #         bolded_words[i].string = '\\textbf{' + bolded_words[i].text + '}'
            # italic_words = html_input.html.find_all('em')

            for line in html_input:
                # process each line here
                # text = convert2latex(line)
                book.write(line.text + '\n\n')
                # book.write(line.text + '\n\n\n')
        book.write('\n\\end{document}')


# def convert2latex(element):
    # if len(element) > 1:
    #     convert2latex(element)
    # print(element.tag)
    # return element.text


mol_html()
