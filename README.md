# project01
GitHub Project 1, Team 03

Project 01 for the Tec de Monterrey Data Analysis Bootcamp

Python scripts that take data from the Spotify and Genius APIs, as well as multiple libraries in order to create an analysis of the most popular songs from 2019 to 2022, according to the respective Spotify Playlists. This information is then processed and used to create a statistical analysis, with scatter and bar plots, as well as linear regression plots.

NOTE: Run the code in the following order:

The first script, spotify_and_features.ipynb, uses the following libraries:
from dotenv import load_dotenv
import pandas as pd
import csv
import os
import base64
import requests
from requests import post, get
from scipy.stats import linregress
import json
import matplotlib.pyplot as plt
from pprint import pprint

As well as data from the ids.py file, containing the client ids for the Spotify API, in order to create dataframes for all of the Top Songs playlists from 2019 to 2022. It takes their IDs and uses them to request the Audio Features, musical descriptors for all songs in those playlists. It merges all the songs' Audio Features into a DataFrame and exports is as a csv file, spotify_and_features.csv

The next file, lyrics.ipynb, takes the following libraries:
import pandas as pd
import requests
import json
import csv
from ids import id
from ids import secret
from ids import genius_token
import numpy as np
from pathlib import Path
import lyricsgenius

And the previously created csv file in order to request the songs' lyrics to the Genius API, and stores the results in an array. A Bag of Words is created, an then it's cleaned, leaving out pronouns, expressions, articles, and other words that are not relevant for the analysis. Then the number of words, as well as the lyrics for every song are appended to the previous Data Frame, containing the songs's Audio Features, and it's exported as the FINAL csv, as well as exporting the words_in_songs and the wordclouds csvs in order to make a Word Cloud representation of the lyrics.

Finally, the statistical_analysis.ipynb file uses the following libraries:
from pathlib import Path
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

As well as all previoulsy created csv files in order to make an analysis of Audio Features and song lyrics. The Audio Feature Analysis is mainly done through scatter plots and linear regression plots, with the r and p values being the most important ones. Then, we also make a pie chart showing the distribution of languages in our songs, as well as bar charts for the most common words in the whole of the songs. We also perform statistical analysis of Mean, Mode, Median, Variance and STD on the words, and finally create a Word Cloud to represent the most used words overall.

The main files for this project; spotify_and_features.ipynb, lyrics.ipynb and statistical_analysis.ipynb, as well as ids.py reside within the Final Codes directory, which itself contains an output directory, that has the csv files used for transmiting the data from file to file. On the level of the FinalCodes directory there's also the Tests Directory, which contains multiple .ipynb and .py files used for testing in the development of the final codes.


References for the development of the project are:

https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html
https://www.kaggle.com/code/minhbtnguyen/songs-similarities-by-lyrics-scraping-and-analysis
https://medium.com/mlearning-ai/wordclouds-with-python-c287887acc8b
https://github.com/m3redithw/data-science-visualizations/blob/main/WordClouds/wordclouds.ipynb
https://github.com/m3redithw/data-science-visualizations/blob/main/WordClouds/prepare.py 
https://github.com/amandotzip/groovydata
https://www.w3schools.com/python/python_regex.asp
https://www.knowledgehut.com/blog/programming/concatenate-strings-python#what-is-concatenation-in-python?%C2%A0 
