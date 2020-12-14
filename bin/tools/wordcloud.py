import sentencecloud
from PIL import Image
import numpy as np


def createWordCloud(csvpath):
    list_of_sentences = readCSV(csvpath)
    freq = strengthFrequency(30, list_of_sentences)
    mask = chooseMask(list_of_sentences)

    wordcloud = sentencecloud.WordCloud(width=1000, height=1000,
                                        background_color='black',
                                        min_font_size=20,
                                        max_font_size=400,
                                        mask=mask).generate(freq)

    return wordcloud


def readCSV(csvpath):
    a_file = open(csvpath, "r")
    list_of_sentences = [(line.strip()) for line in a_file]
    a_file.close()

    return list_of_sentences


def strengthFrequency(count, list_of_sentences):
    strength_frequency = {}
    iter_num = 0
    for sentence in list_of_sentences:
        iter_num += 1
        strength_frequency[sentence] = count
        count = 22 if iter_num == 1 else 12 if iter_num == 2 else 7 if iter_num == 3 else 4 if iter_num == 4 else 7 - iter_num
        if count < 2:
            count = 1

    return strength_frequency


def chooseMask(list_of_sentences):
    length = len(list_of_sentences)
    maskname = 'jetfighter.jpg' if length > 25 else 'diamond.jpg' if length > 20 else 'oval.jpg'\
        if length > 15 else 'triangle.jpg'
    custom_mask = np.array(Image.open(maskname))

    return custom_mask
