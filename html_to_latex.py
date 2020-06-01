import requests
import os
import string
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
        book.write('\\documentclass[letterpaper, 12pt, twoside]{book}\n')
        book.write('\\usepackage[english]{babel}\n')
        book.write('\\usepackage[utf8]{inputenc}\n')
        # book.write('\\usepackage{tabto}\n')
        book.write('\\usepackage[nomarginpar, margin=1in]{geometry}\n')
        book.write('\\usepackage{indentfirst}\n\n')
        book.write('\\title{Mother of Learning}\n')
        book.write('\\author{nobody103}\n\n')
        book.write('\\setlength{\\parindent}{2em}\n')
        book.write('\\setlength{\\parskip}{.5em}\n')
        book.write('\\renewcommand{\\baselinestretch}{1.6}\n\n')
        book.write('\\begin{document}\n\n')
        book.write('\\maketitle\n\n')

        for i in range(len(urls)):
            print('Converting Chapter ' + str(i + 1))
            book.write('\\section*{\\centering Chapter ' + str(i + 1) + '}\n')
            book.write('\\markboth{Chapter }{' + str(i + 1) + '}\n\n')
            req = requests.get(urls[i], headers)
            soup = BeautifulSoup(req.content, 'html.parser')
            html_input = soup.find_all('p')
            # bolded_words = html_input.html.find_all('strong')
            # if len(bolded_words) > 1:
            #     for i in range(len(bolded_words)):
            #         bolded_words[i].string = '\\textbf{' + bolded_words[i].text + '}'
            # italic_words = html_input.html.find_all('em')
           
            for line in html_input:
                for i in range(1, len(line.text)):
                    if i % 120 == 0:
                        # this is just to make the tex file have less issues
                        # with overflow as i manually enter a whitespace
                        # this might be causing me problems where words have a
                        # random space. to fix this, probably change the '\n'
                        # to just \n
                        book.write('\n')

                    # current eror checkking only handles open and close quotes
                    # this feature should later be expnanded to also handle
                    # special expressions for latex bc characters like &
                    # are reserved
                    if line.text[i-1] == '\"':
                        # print(line.text[i], line.text[i] == ' ')
                        if line.text[i] == ' ':
                            book.write('\"')
                        else:
                            book.write('``')
                        continue
                    book.write(line.text[i-1])
                # process each line here
                # text = convert2latex(line)
                book.write('\n\n')
                # book.write(line.text + '\n\n\n')
        book.write('\\end{document}\n\n')


mol_html()
