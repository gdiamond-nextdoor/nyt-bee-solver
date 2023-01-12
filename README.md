# new york times spelling bee helper
this app uses a dictionary i found online to spit out potential words. nyt uses a custom dictionary so they aren't all matches, and there are probably some missing words. When i used this, I went down the list and attempted the words that seemed legit, and this got me to genius and got me a couple pangrams.

## if you're not a coder
you should have poetry installed already if you're a nextdoor developer. if you're not a developer, and you went as far as cloning this repo, congrats so far! try using this command to install poetry
```
# for macs, from https://python-poetry.org/docs/
curl -sSL https://install.python-poetry.org | python3 -
```

## running the script
```
# install dependencies, makes sure we have access to color in the terminal window
poetry install

poetry run solve -c {center letter} -o {other letters}`
```

## results
you should expect to see results like
```
>poetry run solve -c o -o thrpag
Non-pangrams
0 agao
1 aggro
2 agog
...

pangrams
0 orthograph
1 photograph
2 photograt
...
```

### where did the dictionary come from?
https://github.com/dwyl/english-words/blob/master/words_dictionary.json