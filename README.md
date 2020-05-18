# 4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features
The 4MuLA is a dataset built with music information extracted from the Brazilian portal [Vagalume] (http://api.vagalume.com.br/docs/).
We are making available the small version of the dataset used for the experiments carried out on the paper along with a code snippet for reading.

This subset has a 5GB compress and 24GB after uncompressing and can be downloaded here LINK.
The subset has the following attributes:
`musid_id, music_name, music_lang, lyric, art_name, art_id, main_genre, related_genre, related_art, related_music, art_rank, musicnn, melspectogram`

We also provide a file with only the metadata without any acoustic features, which can be downloaded here.

All dataset change will write in the file `CHANGELOG`. 

PS.: We will make the complete dataset available after the paper evaluation process, because the storage service may disclose the name of the paper's authors.


Requirements to code run:
[python3.7](https://www.python.org/downloads/release/python-370/)
[pipenv](https://pypi.org/project/pipenv/)

All libs are in Pipfile. To instal them and active to enviroment using `pipenv run && pipenv shell` 
