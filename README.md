# 4MuLA: A Multitask, Multimodal, and Multilingual Dataset of Music Lyrics and Audio Features

<div style="text-align: justify"> 
We present a new benchmark dataset of songs with structured information to be applied in various machine learning tasks. 
The data comes from a Brazilian portal <a href="http://api.vagalume.com.br/docs/">Vagalume</a> focused on lyrics information, but contain several other annotations provided by their users.  
Our dataset, called 4MuLA (Multitask, Multimodal, and Multilingual Music Lyrics and Audio features dataset), includes features extracted from 96,458 songs distributed by 15,310 artists in 76 genres. 
In particular, our dataset contains latin music genres that are often overlooked in other benchmark datasets. 
For each track, we make available various acoustic features, extracted tags, and lyrics in English, Portuguese, or Spanish. 
With these features, researchers can use our dataset for, at least, lyrics-, audio- or multimodal-based genre classification, music and artist similarity, and popularity regression. 
Moreover, we can perform cross- or multilingual text analysis on lyrics, such as discourse analysis or measuring the differences between emotion transmitted by audio and lyrics. 
</div>


#### Datasets and subsets:
- 4MuLA Large 
  - 96,458 songs distributed by 15,310 artists in 76 genres
  - All music are organized by acoustic features in individual folders
- 4MuLA Small 
  - 9,661 songs distributed by 491 artists in 51 genres
  - Music of **Top 500** artists and only melspectrogram as acoustic feature
- 4MuLA Tiny  
  - 1,988 songs distributed by 93 artists in 27 genres
  - Music of **Top 100** artists and only melspectrogram as acoustic feature

#### Download 
Its possible run the download part of dataset to use specific features. 
In the [features](features) folder, all subsets are organized per features with the **same samples** in each part.
The musics in `mfcc_part_1.parquet` are also the same musics in `chromagram_part_1.parquet`, `tonnetz_part_1.parquet`, `melspectrogram_part_1.parquet` and `tempogram_part_1.parquet`. 
The same idea is present in parts 2, 3, 4...
----
- ##### 4MuLA Large ~ 490 GB
    - [Download](https://drive.google.com/drive/folders/11PdCvT-tgOpgefg8F_VCCBMjzuYgERXe?usp=sharing) (hosted in Google
      Drive)
    - Download individual acoustic features with metadata
        - [Chromagram](features/chromagram.md) ~ 11GB
        - [MFCC](features/mfcc.md) ~ 12GB
        - [Melspectrogram](features/melspectrogram.md) ~ 91GB
        - [Tempogram](features/tempogram.md) ~ 364GB
        - [Tonnetz](features/tonnetz.md) ~ 12GB

     - Acoustic Features
        <table style="width:100%">
          <tr>
            <td>
                <ul>
                    <li>Chromagram</li>
                    <li>Melspectrogram</li>
                    <li>MFCC</li>
                    <li>Tempogram</li>
                    <li>Tonnetz</li>          
                </ul>
             </td>
          </tr>
        </table>
     
     - Metadata
        <table style="width:100%">

          <tr>
            <td>
                <ul>
                  <li>Music Id</li>
                  <li>Music Name</li>
                  <li>Music Language</li>
                  <li>Music Lyrics</li>
                </ul></td>
            <td>                
                <ul>
                  <li>Artist Id</li>
                  <li>Artist Name</li>
                  <li>Artist Rank</li>
                  <li>Main Genre (artist genre)</li>
                </ul>              
            </td>
            <td>                
                <ul>
                    <li>Related Genre</li>
                    <li>Related Artist</li>
                    <li>Related Music</li>
                    <li>Musicnn tags</li>
                 </ul>
              </td>
          </tr>

        </table>

----
- ##### 4MuLA Large - **Only Metadata** ~ 80 MB
    - [Download](https://drive.google.com/file/d/1FqkdsCn4J2MbGLCTNiwSyzanQs2EsQaj/view?usp=sharing) (hosted in Google
      Drive)     
     - Metadata
        <table style="width:100%">

          <tr>
            <td>
                <ul>
                  <li>Music Id</li>
                  <li>Music Name</li>
                  <li>Music Language</li>
                  <li>Music Lyrics</li>
                </ul></td>
            <td>                
                <ul>
                  <li>Artist Id</li>
                  <li>Artist Name</li>
                  <li>Artist Rank</li>
                  <li>Main Genre (artist genre)</li>
                </ul>              
            </td>
            <td>                
                <ul>
                    <li>Related Genre</li>
                    <li>Related Artist</li>
                    <li>Related Music</li>
                    <li>Musicnn tags</li>
                 </ul>
              </td>
          </tr>

        </table>
----
- ##### 4MuLA Small ~ 11 GB
    - [Download](https://drive.google.com/drive/folders/14q9cCOyQlxQg-UJZQezLebEONvfiFXDe?usp=sharing) (hosted in Google
      Drive)
    - <a href="https://doi.org/10.5281/zenodo.4636802"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.4636802.svg" alt="DOI"></a> (
      hosted in Zenodo)
     - Acoustic Features
        <table style="width:100%">
          <tr>
            <td>
                <ul>                    
                    <li>Melspectrogram</li>                              
                </ul>
             </td>
          </tr>
        </table>
     
     - Metadata
        <table style="width:100%">

          <tr>
            <td>
                <ul>
                  <li>Music Id</li>
                  <li>Music Name</li>
                  <li>Music Language</li>
                  <li>Music Lyrics</li>
                </ul></td>
            <td>                
                <ul>
                  <li>Artist Id</li>
                  <li>Artist Name</li>
                  <li>Artist Rank</li>
                  <li>Main Genre (artist genre)</li>
                </ul>              
            </td>
            <td>                
                <ul>
                    <li>Related Genre</li>
                    <li>Related Artist</li>
                    <li>Related Music</li>
                    <li>Musicnn tags</li>
                 </ul>
              </td>
          </tr>

        </table>
----
- ##### 4MuLA Tiny ~ 2 GB
    - [Download](https://drive.google.com/drive/folders/1Wv9ETxEJCbPDMZv4y1-AP0e-EBoGke8F?usp=sharing) (hosted in Google
      Drive)
    - <a href="https://zenodo.org/record/4585498"><img src="https://zenodo.org/badge/DOI/10.1145/3428658.3431089.svg" alt="DOI"></a> (
      hosted in Zenodo)
     - Acoustic Features
        <table style="width:100%;border:0;">
          <tr>
            <td>
                <ul>                    
                    <li>Melspectrogram</li>                  
                </ul>
             </td>
          </tr>
        </table>
     
     - Metadata
        <table style="width:100%;border:0">

          <tr>
            <td>
                <ul>
                  <li>Music Id</li>
                  <li>Music Name</li>
                  <li>Music Language</li>
                  <li>Music Lyrics</li>
                </ul></td>
            <td>                
                <ul>
                  <li>Artist Id</li>
                  <li>Artist Name</li>
                  <li>Artist Rank</li>
                  <li>Main Genre (artist genre)</li>
                </ul>              
            </td>
            <td>                
                <ul>
                    <li>Related Genre</li>
                    <li>Related Artist</li>
                    <li>Related Music</li>
                    <li>Musicnn tags</li>
                 </ul>
              </td>
          </tr>

        </table>
----


#### Requirements
All files have the `parquet` format. To read, is necessary install a engine. 
We use `pyarrow` and `fastparquet`. You can install only one using:
```pip install pyarrow``` or ```pip install fastparquet``` 

#### How to use
To read the dataset, we use the function `read_parquet` existent in `Pandas` package. A example:

```python
>>> import pandas as pd
>>> df = pd.read_parquet('4mula_small.parquet')
>>> df.columns
Index(['music_id', 'music_name', 'music_lang', 'music_lyrics', 'art_id',
       'art_name', 'art_rank', 'main_genre', 'related_genre', 'related_art',
       'related_music', 'musicnn_tags', 'melspectrogram'],
      dtype='object')

>>> df['music_id', 'music_name', 'music_lang', 'music_lyrics'].head(5)
            music_id  music_name	             music_lang   music_lyrics
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

>>> df['musicnn_tags', 'melspectrogram'].head(5)
   musicnn_tags                       melspectrogram
0  ['piano','drums','slow']           [[136.96524, 135.869965, 118.730804, 133.62802...
1  ['rock','pop','guitar']            [[6.28145981, 1.50680351, 0.260610491, 0.17753...
2  ['male','classical','male vocal']  [[0.905277014, 0.33714968, 0.210445538, 0.1545...
3  ['techno','electronic','beat']     [[2.005826, 0.721350968, 0.2188458, 0.23778049...
4  ['guitar','vocal','drums']         [[0.200993568, 0.232473925, 0.227112547, 0.139...

```


#### Snippets:

Some code used in experiments are available in [snippets](snippets) folder.

#### Citing:

```
ACM Reference Format:Angelo Cesar Mendes da Silva, Diego Furtado Silva, and Ricardo Marcondes Marcacini.
2020. 4MuLA: A Multitask, Multimodal, and Multilingual Dataset 
of Music Lyrics and Audio Features. In Brazilian Symposium on Multimedia 
and the Web (WebMedia ’20), November 30-December 4, 2020, São Luís, Brazil. 
ACM, New York, NY, USA, 4 pages. https://doi.org/10.1145/3428658.34310891

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
    url = {https://dl.acm.org/doi/abs/10.1145/3428658.3431089},
    address={São Luís (Brazil)}
}
```

#### Releases

All updates, as new features or fixed bugs, are reported in [CHANGELOG](Changelog.md). 
 
