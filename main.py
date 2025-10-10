import setup_nltk  
from sentiments_analysis import (get_sentiments_sentistrength, get_sentiments_vader, 
                                 get_sentiments_textblob, get_sentiments_sentiwordnet)
import pandas as pd

def sentiment_analysis(sentences, lang):
    results = {
        'Text': [], 'SentiStrength' : [], 'VADER' : [], 'TextBlob' : []
        }
    if lang == 'en':
        results['SentiWordNet'] = []
            
    results['Text'] = sentences
    for sentence in sentences:
        results['SentiStrength'].append(get_sentiments_sentistrength(sentence, lang, mode='trinary')) #mode=dual/scale/binary/trinary
        results['VADER'].append(get_sentiments_vader(sentence, lang))
        results['TextBlob'].append(get_sentiments_textblob(sentence, lang))
        if lang == 'en':
            results['SentiWordNet'].append(get_sentiments_sentiwordnet(sentence, lang))
    return results

def main():
    
    
    with open('data/input_text_en.txt') as f:
        sentences = f.read().split('\n')
    results_en = sentiment_analysis(sentences, 'en')

    with open('data/input_text_de.txt') as f:
        sentences = f.read().split('\n')
    results_de = sentiment_analysis(sentences, 'de')
    
    df_sentiments_en = pd.DataFrame(results_en)
    df_sentiments_de = pd.DataFrame(results_de)
    df_sentiments_en.to_csv('data/output_sentiments_en.tsv', sep='\t', index = False)
    df_sentiments_de.to_csv('data/output_sentiments_de.tsv', sep='\t', index = False)

if __name__ == "__main__":
    main()

