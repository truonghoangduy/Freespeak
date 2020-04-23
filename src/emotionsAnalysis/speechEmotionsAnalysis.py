import soundfile, librosa, joblib, os
import numpy as np
import matplotlib.pyplot as plt

from pydub.utils import make_chunks
from pydub import AudioSegment

import logging

def custom_file(audio_name, test_size = 0.2):
    logging.info('starting speechEmotionsAnalysis')
    #load emotions recognition model
    model = joblib.load('emotionsAnalysis\\resources\\emotions_model.pkl')
    logging.info('emotions_model loaded')

    myaudio = AudioSegment.from_file(audio_name, "wav")
    logging.info('wav audio loaded')

    chunk_length_ms = 3000
    chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of three secs
    logging.info('chunks created')
    # creating a new folder in resources if not already exists
    current_path = os.getcwd()
    new_path = os.path.join(current_path, "emotionsAnalysis\\resources\\wav_chunks")
    if(not os.path.isdir(new_path)):
        os.mkdir(new_path)

    y = []
    #Export all of the individual chunks as wav files
    for i, chunk in enumerate(chunks):
        file = "emotionsAnalysis\\resources\\wav_chunks\\chunk{0}.wav".format(i)
        logging.info("exporting" + file)
        chunk.export(file, format="wav")
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        y.append(feature)
        os.remove(file)
    logging.info('feature extraction done')
    y_pred = model.predict(y)
    logging.info('prediction done')
    plot_pie_chart(y_pred)

def plot_pie_chart(pred):
    logging.info('start plotting speechEmotions')
    labels = np.unique(pred)
    emotionToColorMap = {
    "happy": '#ff9999',
    "neutral": '#66b3ff',
    "fearful": '#ffcc99',
    "calm": '#99ff99'
    }

    sizes = []
    colors = []
    for i in range(len(labels)):
        color_counter = 0
        for j in range(len(pred)):
            if labels[i] ==  pred[j]:
                color_counter += 1
        sizes.append(color_counter)
        colors.append(emotionToColorMap.get(labels[i]))

    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90)
    for text in texts:
        text.set_color('grey')
        for autotext in autotexts:
            autotext.set_color('grey')# Equal aspect ratio ensures that pie is drawn as a circle

    ax1.axis('equal')
    plt.tight_layout()
    plt.legend(labels=labels)
    plt.savefig('outputFiles\\speechEmotionsChart.png')
    generateComment(sizes, labels)
    plt.cla()
    plt.clf()
    logging.info('plotting speechEmotions done')

def generateComment(sizes, labels):
    indexMaxVal = findallIndx(sizes)
    occuringEmotions = "We detected these emotions in your voice:\n"
    emotions = ""
    for i in range(len(labels)):
        if(sizes[i] != 0):
            emotions += "-" + labels[i] + "\n"
    occuringEmotions += emotions + "\n"
    fearfulIndex = 0
    for i in range(0, len(labels)):
        if labels[i] == "fearful":
            fearfulIndex = i
            break
    if "fearful" in labels:
        if fearfulIndex in indexMaxVal:
            occuringEmotions += (
                "\nFear was one of the most common emotions during your speaking.\n"
                "Here are some tips for better presenting voice:\n"
                "1.If you're new to public speaking, try to start small, find a few friends or family members to practice on and just build up.\n"
                "2.The size of the audience is not that important. The most important thing is your knowledge of the topic about which\n"
                "you are presenting. If you know it really well you'll get more confidence and this is really important! The ability to connect\n"
                "with your audience comes from having the confidence and you won't get lost during a presentation.\n"
                "3.Don't just to memorize word for word of your entire speech, you have to understand it from the beginning until the end.\n"
                "4.The most fearful moment is awaiting your presentation. Just think about a perfect ending and throw bad thoughts away!:)")
        else:
            occuringEmotions +=  (
                "\nWe detected some fear, but it was not one of the emotions that occurred the most.\n"
                "Maybe you have some sections, where you still don't feel confident in.\n"
                "Try practicing your 'weak spots' extensively because confidence is key!\n"
                "You could write down some hints on a small card to fall back on, but try not to memorize your speech word by word!\n"
                "Understanding your topic thoroughly can give you that extra confidence boost that you need!\n")

    if "happy" in labels:
        occuringEmotions += (
            "\nGood job! Your voice sounded happy!\n"
            "A happy voice can trick yourself to be more motivated for your presentation.\n"
            "Happiness will make you seem more likeable for your audience and you will have more fun presenting!\n")

    if "calm" in labels:
        occuringEmotions += (
            "\nYour voice was calm. That's great!\n"
            "A calm voice makes it easy for your audience to understand you.\n"
            "Also, you will seem confident with a calm voice.\n"
            "However, remember to mix up the emotions, so your audience doesn't get bored!\n")
    else:
        occuringEmotions += (
            "\We didn't record your voice being calm. You can sound calmer if you speak slowly.\n"
            "Cour voice will have more power and authority and your listeners will have an opportunity\n"
            "to absorb and reflect on what you're saying. Powerful people speak slowly, enunciate clearly, and express themselves with confidence.\n")

    occuringEmotions += comment()

    saveToText(occuringEmotions)

def comment():
    occuringEmotions = (
        "\nRemember to speak slowly during your presentation. When you speak rapidly, your pitch increases and you sound more fearful."
        "A loud, confident and slow speaking voice will lead you to a powerful and moving speech!\n"
        "Also, the power of your speech is contained in the silences that you create as you speak. Put more pauses in your speaking to create more effect.\n"
        "And last but not least don't forget to drink and to eat before presenting! Energy is essential for good speaking and voice projection!\n")
    return occuringEmotions

def saveToText(string):
    text_file = open("outputFiles\\speechEmotionsTippsAndAdvices.txt", "w")
    text_file.write(string)
    text_file.close()

def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        X = sound_file.read(dtype="float32")
        sample_rate=sound_file.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))
        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
            result=np.hstack((result, chroma))
        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
            result=np.hstack((result, mel))
    return result

def findallIndx(sizes):
    maxVal = -1
    positionsMaxVal = []
    for i in range(len(sizes)):
        if maxVal <= sizes[i]:
            maxVal = sizes[i]
            positionsMaxVal.append(i)
    return positionsMaxVal
