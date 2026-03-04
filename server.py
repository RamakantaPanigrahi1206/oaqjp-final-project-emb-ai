'''
Emotion detection module.

This module sends text to the Watson Emotion API
and returns detected emotion scores along with
the dominant emotion.
'''
# import FLask, render_template, request, emotion_detection
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    ''' This code receive data from HTML '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emo_dect = response['emotion_scores']
    if emo_dect['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return (
    f"For the given statement, the system response is "
    f"{ {k: emo_dect[k] for k in ['anger','disgust','fear','joy','sadness']} }. "
    f"The dominant emotion is {emo_dect['dominant_emotion']}."
    )
@app.route("/")
def render_index_page():
    '''
    this function initiate the rendering
    '''
    return render_template("index.html")
if __name__=="__main__":
    # this exucutes the app on localhost:5000
    app.run(host="0.0.0.0", port=5000)
