# HTML SCRIPTS

Some cute little scripts to download things that I care about from the internet.


## Activate the venv

```
source venv/bin/activate
```

## To install the packages

install the pip packages using

```
pip install -r requirements.txt
```
then you can run the programs.

1. Molscrape: responsible for grabbing then converting the web serial "Mother of Learning" into LaTeX 
  - Run through html_to_latex.py
1. Qalam: downloading podcasts from qalam
  - run through run.py `python3 qalam/run.py`

## save new requirements
make sure you're in the virtual env

```
venv/bin/python3 -m pip freeze > requirements.txt
```
