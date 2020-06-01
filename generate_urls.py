# returns list_of_urls which is a list of urls. one url per chapter of mol
def mol_links():
    list_of_urls = []
    # url for the first chapter of mother of learning
    base_url = 'https://www.fictionpress.com/s/2961893/1/Mother-of-Learning'
    # there are 108 chapters in mother of learning
    chapter_numbers = 108
    for i in range(1, chapter_numbers + 1):
        link = base_url[:39] + str(i) + base_url[40:]
        list_of_urls.append(link)
    return list_of_urls
