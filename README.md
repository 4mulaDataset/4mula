# 4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features
The 4MuLA is a dataset built with music information extracted from the Brazilian portal [Vagalume](http://api.vagalume.com.br/docs/).
We are making available the small version of the dataset used for the experiments carried out on the paper along with a code snippet for reading.

This subset has a 8GB compress and 24GB after uncompressing and can be downloaded [here](https://mega.nz/file/nSAmTYhB#us-BHkE8FlFF5WABQs0IeGxNWC_B2aF9TvLuiXkbCgI).
The subset has the following attributes:
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

>>> df.head(5)
            music_id  ...                                     melspectrogram
0  3ade68b6gc207fda3  ...  [[136.96524, 135.869965, 118.730804, 133.62802...
1  3ade68b8g9410afa3  ...  [[6.28145981, 1.50680351, 0.260610491, 0.17753...
2  3ade68b7gb67d7ea3  ...  [[0.905277014, 0.33714968, 0.210445538, 0.1545...
3  3ade68b8gcd12d0b3  ...  [[2.005826, 0.721350968, 0.2188458, 0.23778049...
4  3ade68b7g955b3ea3  ...  [[0.200993568, 0.232473925, 0.227112547, 0.139...
[5 rows x 13 columns]

>>> df.tail(5)
               music_id  ...                                     melspectrogram
9656  3ade68b7g32d24ea3  ...  [[0.0110503314, 0.0309154801, 0.0707755387, 0....
9657  3ade68b6g41bceda3  ...  [[0.222000927, 0.255416274, 0.31317386, 0.1523...
9658  3ade68b8g452cd0b3  ...  [[2.67068839, 0.666260242, 0.015704168, 0.0085...
9659  3ade68b8gb72ad0b3  ...  [[32.5476112, 7.8087039, 0.145487651, 0.636182...
9660  3ade68b8g6d81bfa3  ...  [[0.116672575, 0.234225765, 0.358113676, 0.271...
[5 rows x 13 columns]

```

All dataset changes will write in the file `CHANGELOG`. 

PS.: We will make the complete dataset and code available after the paper evaluation process, because the storage service may disclose the name of the paper's authors, which is denied in the blind review process.

