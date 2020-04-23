# Freespeak
Hi, this is our super duper presentation trainer!
Public speaking is nowadays a common task in our daily life performed by every type of individual in every kind of domain possible, such as presentations and seminars by students or pitches by innovators. However, this type of task requires skill and cannot be mastered by everyone with ease. Furthermore, the fear of public speaking is very common and sometimes hard to overcome. Nonetheless, it is part of our education and our work life and therefore inevitable.
That is where our presentation trainer comes in!
The trainer is an application that helps people with difficulties in public speaking and overcome their fear by providing sophisticated training as a preparation for their incoming presentation. It records speech and movements of the speaker in a video and analyses his/her speak pattern. Graphs representing the speaker's patterns will be given at the end along with tips of improvements.

#### Features:
- Records voice and video
- Analysis of speaking speed
- Analysis of facial expressions
- Analysis of speech emotions
- Analysis of text emotions

#### Prerequisites:
One important thing is to properly install Python, since our program uses Tensorflow that has some [requirements](https://www.tensorflow.org/install/pip):
- Install Python 3.7(64 Bit) from [here](https://www.python.org/downloads/windows/)
- Install and upgrade pip:
```
python get-pip.py
python -m pip install --upgrade pip
```
If you already have Python and pip installed, check their versions with
```
python --version
pip --version
```
and make sure that your Python version is 3.5 – 3.7 and your pip version is at least 19.0 or later.

Now setup the Google Cloud SDK with this [manual](https://cloud.google.com/sdk/docs/downloads-interactive) and install those Python Google libraries using pip:
```
pip install --upgrade google-api-python-client
pip install google-cloud
pip install google-cloud-speech
pip install google-cloud-language
```

Finally setup the remaining Python-packages by running the command
```
pip install -r requirements.txt
```
from the folder this text file is located in, install pyaudio by following the instruction [here](https://stackoverflow.com/questions/54998028/how-do-i-install-pyaudio-on-python-3-7) and set the PATH environment variable for GOOGLE_APPLICATION_CREDENTIALS with this [instruction](https://cloud.google.com/natural-language/docs/quickstart)

When everything is installed, change your directory to **src** and run the program:
```
cd src
python main.py
```

To start recording, push the **Start Recording** button:
![](/images/startRecording.png)

At the left bottom corner you will see a timer which shows for how long the audio and video are being recorded
![](/images/timer.png)

To stop recording, push the **Stop Recording** button:
![](/images/stopRecording.png)

After pushing the **Stop Recording** button, our program starts to analyze your emotions, speaking speed and body language.
You can look up the analyze results by pushing the **Analyze Results** button:
![](/images/analyzeResults.png)

At the top you can see the different categories we analyzed during your presentation,
![](/images/categories.png)

and on the left side you can switch between the plotted graphs and tips given to you based on your behaviour pattern.
![](/images/example1.png)

#### External Sources:
- https://github.com/victordibia/handtracking
- https://github.com/alvinwan/hand-tracking-pong
- https://github.com/atulapra/Emotion-detection
- https://data-flair.training/blogs/python-mini-project-speech-emotion-recognition/


##### Made by t4kum1, sutedalm, mpospelova