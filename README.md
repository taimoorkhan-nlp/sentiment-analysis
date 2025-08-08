# Sentiment Analysis (English and Deutsch)

## Description
Sentiment analysis is an important natural language processing. The method analyzes texts in English or Deutsch to determine its polarity as positive, negative and neutral. For sentiment analysis of English text it uses 1. [SentiStrength](https://github.com/zhunhung/Python-SentiStrength), 2. [VADER](https://pypi.org/project/vaderSentiment/), 3. [TextBlob](https://textblob.readthedocs.io/en/dev/), and 4. [SentiWordNet](https://www.nltk.org/api/nltk.corpus.reader.sentiwordnet.html). While for Deutsch text analysis it uses 1. [SentiStrength_de](https://github.com/OFAI/SentiStrength_DE) 2. [GerVADER](https://github.com/KarstenAMF/GerVADER), and 3. [TextBlobDE](https://github.com/markuskiller/textblob-de)   

## Use Cases
Analyze sentiments of the social media posts, customer reviews, or other user content.

## Input Data

The method reads input as text file. The sample data files for English and Deutsch are `data/input_text_en` and `data/input_text_de`.

| Text |
|:----:|
| I absolutely loved the performance — it was breathtaking from start to finish! |
| The movie was enjoyable, though a bit slow in parts. |
| The package arrived on Tuesday as expected. |
| I was slightly disappointed with the quality of the material. |
| That was the worst experience I’ve ever had — completely unacceptable! |

## Output Data

|Text	| SentiStrength	| VADER	| TextBlob	| SentiWordNet |
|:-----:|:-------------:|:-----:|:---------:|:------------:|
| I absolutely loved the performance â€” it was breathtaking from start to finish!	| {'pos': 5, 'neg': -1, 'neu': 1}	| {'neg': 0.0, 'neu': 0.595, 'pos': 0.405, 'compound': 0.8169}	| {'polarity': 0.85, 'subjectivity': 0.9}	| {'pos': 0.625, 'neg': 0.0}|
| The movie was enjoyable, though a bit slow in parts.	| {'pos': 3, 'neg': -1, 'neu': 1}	| {'neg': 0.0, 'neu': 0.756, 'pos': 0.244, 'compound': 0.4404}	| {'polarity': 0.09999999999999998, 'subjectivity': 0.5} |	{'pos': 0.5, 'neg': 0.375} |
| The package arrived on Tuesday as expected.	| {'pos': 1, 'neg': -1, 'neu': 0}	| {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}	| {'polarity': -0.1, 'subjectivity': 0.4}	| {'pos': 0.0, 'neg': 0.0} |
| I was slightly disappointed with the quality of the material.	| {'pos': 1, 'neg': -2, 'neu': -1}	| {'neg': 0.238, 'neu': 0.762, 'pos': 0.0, 'compound': -0.4228}	| {'polarity': -0.75, 'subjectivity': 0.75}	| {'pos': 0.375, 'neg': 0.5} |
| That was the worst experience I â€™ve ever had â€” completely unacceptable!	| {'pos': 1, 'neg': -5, 'neu': -1}	| {'neg': 0.411, 'neu': 0.589, 'pos': 0.0, 'compound': -0.8264}	| {'polarity': -0.4375, 'subjectivity': 0.7}	| {'pos': 0.75, 'neg': 1.5} |

## Hardware Requirements

The method runs on a small virtual machine provided by a cloud computing company (2 x86 CPU cores, 4 GB RAM, 40GB HDD).

## Environment Setup

Run the following command to setup with the virtual environment.

`pip install -r requirements.txt`

## How to Use

Run the following command to perform sentiment analysis on English texts and Deutsch texts from the `data/` input files.

`python main.py`

## Contact Details
For queries, please contact <taimoor.khan@gesis.org>
