import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections

def find_duplicates_map(data):
    dups = collections.defaultdict(list)
    for index, item in enumerate(data):
        dups[item].append(index)
    return dups

def filter_data(data, time):
    dups = find_duplicates_map(data)
    result = []
    for index, item in enumerate(data):
        repetitions = dups[item]
        if index-1 in repetitions or index+1 in repetitions:
            string = time[index] + "," + item
            result.append(string)
    return result

def keep_duplicates():
    filtered = []
    with open('outputFiles\\emotions.csv', 'r') as f:
        temp = [line.strip() for line in f]
        data = []
        time = []
        for index, item in enumerate(temp):
            arr = item.split(",")
            time.append(arr[0])
            data.append(arr[1])

        comment()
        if len(time) == 1 and len(data) == 1:
            print("NO FACE DETECTED. COULD NOT CREATE FACIAL EXPRESSIONS GRAPH.")
            return False

        filtered = filter_data(data, time)
        f.flush()

    with open('outputFiles\\emotions.csv', 'w', newline='') as fd:
        fd.write("Time,Emotions\n")
        for s in filtered:
            fd.write(s+"\n")
        fd.flush()

    plotChart()
    return True

def plotChart():
    df = pd.read_csv("outputFiles\\emotions.csv")
    emotions = df['Emotions']

    labels = np.unique(emotions)
    emotionTocolorMap = {
    "Happy": '#ff9999',
    "Neutral": '#66b3ff',
    "Fearful": '#ffcc99',
    "Angry": '#99ff99',
    "Disgusted": '#ccebc4',
    "Sad": '#fdb462',
    "Surprised": '#fa81ff'
    }

    sizes = []
    colors = []
    for i in range(len(labels)):
        color_counter = 0
        for j in range(len(emotions)):
            if labels[i] ==  emotions[j]:
                color_counter += 1
        sizes.append(color_counter)
        colors.append(emotionTocolorMap.get(labels[i]))

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, colors = colors, autopct='%1.1f%%', startangle=90)
    for text in texts:
        text.set_color('grey')
        for autotext in autotexts:
            autotext.set_color('grey') # Equal aspect ratio ensures that pie is drawn as a circle

    ax1.axis('equal')
    plt.tight_layout()
    plt.legend(labels=labels)
    plt.savefig('outputFiles\\facialEmotionsChart.png')
    plt.cla()
    plt.clf()

def comment():
    string = (
        "The movements of your eyes, mouth, and facial muscles can build a connection with your audience.\n"
        "Alternatively, they can undermine your every word. Eye focus is the most important element in this process.\n"
        "Effective presenters engage one person at a time, focusing long enough to complete a natural phrase and watch it sink in for a moment.\n"
        "The other elements of facial expression can convey the feelings of the presenter, anything from passion for the subject, to depth of concern for the audience.\n"
        "Unfortunately, under the pressure of delivering a group presentation, many people lose their facial expression.\n"
        "Their faces solidify into a grim, stone statue, a thin straight line where the lips meet.\n"
        "Try to unfreeze your face right from the start. For example, when you greet the audience, smile!\n"
        "You won't want to smile throughout the entire presentation, but at least at the appropriate moments.\n"
        "It's only on rare occasions that you may need to be somber and serious throughout.\n"
        "Use your facial expressions as a tool to underline your content!"
    )
    text_file = open("outputFiles\\facialExpressionsAdvices.txt", "w")
    text_file.write(string)
    text_file.close()
