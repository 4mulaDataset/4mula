# 4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features
The 4MuLA is a dataset built with music information extracted from the Brazilian portal [Vagalume](http://api.vagalume.com.br/docs/).
We are making available the small version of the dataset used for the experiments carried out on the paper along with a code snippet for reading.

This subset has a 11GB and can be downloaded [here](https://mega.nz/file/3K4lAQIA#HUsw27Iu-kCmSPOPmETTyIP7aVX224KPNMWyoR3TJdo).
The subset has the following features:
`musid_id, music_name, music_lang, lyric, art_name, art_id, main_genre, related_genre, related_art, related_music, art_rank, musicnn, melspectogram`

We also provide a file with only the metadata without any acoustic features, which can be downloaded [here](https://mega.nz/file/eWpyQKyT#7uTZQ9djcH3kF5zgHdVQ3nqGgp38TDWQpDur-guWZcE).


##### The dataset read
Reading the small dataset can be done using pandas.
```python
>>> import pandas as pd
>>> df = pd.read_parquet('4mula_small.parquet')
>>> df.columns
Index(['music_id', 'music_name', 'music_lang', 'music_lyric', 'art_id',
       'art_name', 'art_rank', 'main_genre', 'related_genre', 'related_art',
       'related_music', 'musicnn', 'melspectrogram'],
      dtype='object')

>>> df['music_id', 'music_name', 'music_lang', 'music_lyric'].head(5)
            music_id  music_name	             music_lang   music_lyric
0  3ade68b6gc207fda3  I've Got To See You Again     en       Line on your face don't bother me\nDown ...
1  3ade68b8g9410afa3  New Perspective               en       I feel the salty waves come in\nI feel  ...
2  3ade68b7gb67d7ea3  Renúncia                      pt-br    Hoje não existe nada mais entre nós  ...
3  3ade68b8gcd12d0b3  Good Form                     en       Eardrummers\nUh, uh, huh, uh, huh\nUh,  ...
4  3ade68b7g955b3ea3  Out Of Time                   en       You don't know what's going on\nYou've ...

>>> df['art_id', 'art_name', 'art_rank', 'main_genre', 'related_genre'].head(5)
   art_id             art_name             art_rank  main_genre        related_genre
0  3ade68b6gfd79eda3  Norah Jones          353       Jazz              ['Jazz', 'Blues', 'Soul Music', 'Country', 'Ro...
1  3ade68b6g2480fda3  Panic! At The Disco  154       Rock Alternativo  ['Rock Alternativo', 'Pop/Punk', 'Pop/Rock', '...
2  3ade68b5gef48eda3  Nelson Gonçalves     446       MPB               ['MPB', 'Velha Guarda', 'Romântico', 'Samba', ...
3  3ade68b7gc2b61ea3  Nicki Minaj          421       Rap               ['Rap', 'Pop', 'Hip Hop', 'R&B', 'Dance', 'Ele...
4  3ade68b6g28c9eda3  Rolling Stones       118       Classic Rock      ['Classic Rock', 'Rock', 'Blues', 'R&B', 'Hard...

>>> df['related_art', 'related_music'].head(5)
  related_art                                        related_music
0 [{'id': '3ade68b6g9a3beda3', 'name': 'Joss Sto...  [{'id': '3ade68b7gdddfcea3', 'name': 'Ten Phan...
1 [{'id': '3ade68b6gc5baeda3', 'name': 'Fall Out...  [{'id': '3ade68b7gc6144ea3', 'name': 'Wake Me ...
2 [{'id': '3ade68b5gf058eda3', 'name': 'Orlando ...  [{'id': '3ade68b6gbab1fda3', 'name': 'As Rosas...
3 [{'id': '3ade68b5g8d18eda3', 'name': 'Lil Wayn...                                                 []
4 [{'id': '3ade68b6g7d5aeda3', 'name': 'Mick Jag...  [{'id': '3ade68b7g9ae20ea3', 'name': 'Run Of T...

>>> df['musicnn', 'melspectrogram'].head(5)
   musicnn                            melspectrogram
0  ['piano','drums','slow']           [[136.96524, 135.869965, 118.730804, 133.62802...
1  ['rock','pop','guitar']            [[6.28145981, 1.50680351, 0.260610491, 0.17753...
2  ['male','classical','male vocal']  [[0.905277014, 0.33714968, 0.210445538, 0.1545...
3  ['techno','electronic','beat']     [[2.005826, 0.721350968, 0.2188458, 0.23778049...
4  ['guitar','vocal','drums']         [[0.200993568, 0.232473925, 0.227112547, 0.139...

```




#### Citing:

```
ACM Reference Format:Angelo Cesar Mendes da Silva, Diego Furtado Silva, and Ricardo Marcondes Marcacini. 2020. 4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features. In Brazilian Symposium on Multimedia and the Web (WebMedia ’20), November 30-December 4, 2020, São Luís, Brazil. ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3428658.34310891

```
or 
```
@inproceedings{4mula2020,
    month = {11},
    author = {Angelo Cesar Mendes da Silva and Diego Furtado Silva and Ricardo Marcondes Marcaini},
    booktitle = {Brazilian Symposium on Multimedia and the Web (WebMedia ’20)},
    title = {4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features},
    publisher = {ACM},
    pages = {4},
    year = {2020},
    url = {https://doi.org/10.1145/3428658.34310891},
    address={São Luís (Brazil)}
}
```

#### Updates

All changes are in [CHANGELOG](Changelog.md). 