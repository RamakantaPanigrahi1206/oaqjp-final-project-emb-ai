from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")

def emo_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emo_dect = response['emotion_scores']
    return "For the given statement, the system response is \
    'anger': {} , \
    'disgust': {} , \
    'fear': {} , \
    'joy': {}, \
    'sadness': {} .\
    The dominant emotion is {} . \
    ".format(emo_dect['anger'], emo_dect['disgust'], emo_dect['fear'], emo_dect['joy'], emo_dect['sadness'], emo_dect['dominant_emotion'] )

@app.route("/")
def render_index_page():
    '''
    '''
    return render_template("index.html")

if __name__=="__main__":
    ''' this exucutes the app on localhost:5000'''
    app.run(host="0.0.0.0", port=5000)
