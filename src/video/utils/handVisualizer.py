from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
import seaborn as sns
import os, statistics, math, sys, csv

def visualiser(path):
    data = csv.DictReader(open(path+'\\handPositions.csv'), delimiter=',')
    xCoords = []
    yCoords = []
    for d in data:
        xCoords.append(int(d['x']))
        yCoords.append(int(d['y']))

    string = standardDeviation(xCoords, yCoords)
    if len(xCoords) == 0 or len(yCoords) == 0:
        print("NO HANDS WERE TRACKED. COULD NOT CREATE HAND VISUALIZER GRAPH.")
        return False

    gestureAdvicer(string)
    xMax = 802
    yMax = 539

    x, y = np.mgrid[0:xMax:100j, 0:yMax:100j]
    positions = np.vstack([x.ravel(), y.ravel()])
    values = np.vstack([xCoords, yCoords])

    z = np.sum(values)
    if np.isnan(z) or np.isinf(z):
        print("COULD NOT DETECT ANY HAND MOVEMENTS")
        return False



    kernel = stats.gaussian_kde(values)
    f = np.reshape(kernel(positions).T, x.shape)

    plt.xlim(0,xMax)
    plt.ylim(0,yMax)
    plt.imshow(np.rot90(f), cmap='jet', extent=[0, xMax, 0, yMax])
    plt.scatter(xCoords,yCoords,alpha=0.3)
    plt.gca().set_ylim(plt.gca().get_ylim()[::-1])
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    plt.title('Hand positions')
    # plt.subplots_adjust(left=0.01, bottom=0, right=0.99, top=1)

    plt.savefig(path + '\\handposPlot.png')
    plt.cla()
    plt.clf()
    return True

def standardDeviation(x, y):
    if len(x) < 2 or len(y) < 2:
        return ""
    # standard deviation of x and y histogram
    xStdev = statistics.stdev(x)
    # yStdev = statistics.stdev(y)

    #average standard deviation
    # avgStdDev = math.sqrt(xStdev**2 + yStdev**2)
    string = ""
    if xStdev < 50: # 50 is an outcome of long long long testing
        string += (
            "As you can see in the plot, you moved your hands only a little and they mostly stayed in the same spot.\n"
            "This is might make you look stiff and shy for the audience, they may quickly lose their interest in your presentation!\n"
            "Try to move a little more, but don't exaggerate your movements. And don't forget to practice in front of a mirror or your friends and family.\n")
    elif xStdev > 60:
        string += (
            "As you can see in the plot, you moved your hands a lot, they appeared in really many places.\n"
            "While your hands are a great tool to underline your speech, you have to know when and how to use them.\n"
            "Be careful to not exaggerate your hand movement, as this could make you look stressed or hectic.\n")
    else:
        string += "Good job! Your hand movements seemed balanced.\n"

    return string

def gestureAdvicer(anotherString):
    string = "\nWhen a speaker communicates with his audience, it's not only limited to the 'words', it's a combination of words,\n"
    string += "voice emotions, and body language. Moving your hands during public speaking makes it easier for you to have an easy flow of information.\n"
    string += "Using your hands as a story telling tool is how you can best explain yourself in personal and professional scenarios. Gesture makes your speech\n"
    string += "more compelling, trustworthy, interesting, and help the listeners to connect better. They can often help to emphasize certain points of your speech\nand strengthen your public speaking message.\n"
    string += "\nSome tips for better hands movements:\n"
    string += "-Don't force hand gestures that don't feel natural! Your audience most likely will be distracted by your hands. Practice new movements before getting on stage!\n"
    string += "-One of the most easiest gestures to add is visualizing numbers. If you have some examples lined up, visualize the numbers of the examples with your fingers!\n"
    string += "-Using open palms is also a great way to put audience in comfort. Humans around the world use open palm gestures to demonstrate lack of threat.\n"
    string += "-Don't move your hands too much, or else the audience will be distracted. Define a zone where you will move your hands.\n"
    string += "-Also, don't forget to relax! You don't have to ove your hands constantly!\n"
    string += "-Your gestures are a second language that communicates powerful messages to your audience. Practice them before getting on stage!\n"

    text_file = open("outputFiles\\handGesturesAdvicer.txt", "w")
    text_file.write(anotherString + string)
    text_file.close()


if __name__ == "__main__":
    visualiser('outputFiles')
