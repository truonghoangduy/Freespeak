from scipy import stats
import matplotlib.pyplot as plt2
import numpy as np
import seaborn as sns 
import csv
import sys
import os

def visualiser(path):
    data = csv.DictReader(open(path+'\\emotions.csv'), delimiter=',')
    realtime = []
    emotions = []

    fearful = []
    happy = []
    sad = []
    angry = []
    surprised = []
    disgusted = []
    neutral = []

    emotions = []


    for d in data:
        realtime.append(float(d['Time']))
        emotions.append(str(d['Emotions']))

    for i in range(0,len(realtime)):
        if (emotions[i] == 'Fearful'):
            fearful.append(realtime[i]-realtime[0])
        elif (emotions[i] == 'Happy'):
            happy.append(realtime[i]-realtime[0])
        elif (emotions[i] == 'Sad'):
            sad.append(realtime[i]-realtime[0])
        elif (emotions[i] == 'Angry'):
            angry.append(realtime[i]-realtime[0])
        elif (emotions[i] == 'Neutral'):
            neutral.append(realtime[i]-realtime[0])
        elif (emotions[i] == 'Disgusted'):
            disgusted.append(realtime[i]-realtime[0])        
        else:
            surprised.append(realtime[i]-realtime[0])

    emotionList = [surprised,happy,sad,fearful,angry,neutral,disgusted]
    emList = []
    lines = [3,2,1,0,-1,-2,-3]
    markers = ['o','v','^','h','s','P','X'] 
    if len(realtime) == 0 :
        xmin, xmax = 0, 10
    else:
        xmin, xmax = 0, max(realtime) - min(realtime)


    plt2.xlim(xmin,xmax)
    for e,m,l in zip(emotionList,markers,lines):
        ys = []
        for i in range(0,len(e)):
            ys.append(l)
        emList.append(plt2.scatter(e,ys,marker = m))
        plt2.plot([xmin,xmax],[l,l],'k-',alpha=0.3)   
     
    #plt2.legend(tuple(emList),('Surprised','Happy','Sad','Fearful','Angry','Neutral','Disgusted'))
    plt2.yticks(lines,['Surprised','Happy','Sad','Fearful','Angry','Neutral','Disgusted'])
    plt2.xlabel('Time in seconds')
    plt2.title('Shown emotions over time')
    plt2.subplots_adjust(left=0.15, bottom=0.1, right=0.9, top=0.9)
    plt2.savefig(path + '\emotionsPlot.png')
    plt2.clf()
    plt2.cla()

