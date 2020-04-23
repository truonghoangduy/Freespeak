#import argparse
import matplotlib.pyplot as plt
import math

from emotionsAnalysis.sentimentAnalysis import analyze
from emotionsAnalysis.speechEmotionsAnalysis import custom_file

import logging

#  -------------------------------Analyzes text emotions-------------------------------
def analyze_text_emotions(file_name):
    logging.info('start textEmotionExplanation')
    annotations = analyze(file_name)
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    # if magnitude == 0 and score == 0:
    #     print("NO TEXT WAS DETECTED, COULD NOT CREATE GRAPH FOR TEXT EMOTIONS ANALYSIS")
    #     return False

    result = 'Overall Sentiment: positivity of {} with strength of {}'.format(
        score, magnitude) + "\n"
    string = ""

    if score > 0 and magnitude >= 5:
        string += "Your speech text shows positive emotions and is very emotional. That means that your speech text is overall really positive."
    elif score > 0 and magnitude < 5:
        string += "Your speech text shows positive emotions, but is not really emotional. That means that your speech text has a few positive emotions."
    elif score < 0 and magnitude < 5:
        string += "Your speech text shows negative emotions, but is not really emotional. That means that your speech text has a few negative emotions."
    elif score < 0 and magnitude >= 5:
        string += "Your speech text shows negative emotions and is very emotional. That means that your speech text is overall really negative"
    elif score == 0 and magnitude < 5:
        string += "Your speech text is not emotional at all, it is very neutral."
    elif score == 0 and magnitude >= 5:
        string += "Your speech shows equally distributed positive and negative emotions."

    with open("outputFiles\\textEmotionsExplanation.txt", "w") as text_file:
        text_file.write(result + string)
        logging.info('textEmotionsExplanation done')

    plot_text_emotions_graph(magnitude, score)
    # return True

def plot_text_emotions_graph(magnitude, score):
    logging.info('start plotting textEmotions')
    x = ['magnitude', 'score']
    values = [magnitude, score]
    scale = 1
    if magnitude >= 10:
        scale = math.floor(magnitude / 10) + 1

    if magnitude < 1:
        scale = 0.5

    x_pos = [scale*0, scale*1]
    ax = plt.gca()

    plt.barh(x_pos, values, 0.3*scale, color=['#2300A8', '#00A658'], alpha=0.5)
    plt.title("Text emotions analysis", y=1.6)
    plt.yticks(x_pos, x)

    ax.set_aspect('equal')
    ax.grid(True, which='both', alpha=0.4)

    #removing top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axvline(x=0, color='black', alpha=0.7)

    scoreScale = -1*scale
    magnitudeScale = -1.5*scale
    if magnitude < 1:
        scoreScale += 0.1
        magnitudeScale += 0.1

    plt.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9)
    plt.savefig('outputFiles\\textEmotions.png')
    logging.info('plotting textEmotions done')
#  -------------------------------Analyzes text emotions-------------------------------


def analyze_audio_emotions(audio_file_name):
    custom_file(audio_file_name)
