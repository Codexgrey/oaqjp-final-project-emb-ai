''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze == "":
        return "Invalid text! Please try again!"

    res = emotion_detector(text_to_analyze)
    anger = res["anger"]
    disgust = res["disgust"]
    fear = res["fear"]
    joy = res["joy"]
    sadness = res["sadness"]

     # score dictionary
    scores = {
        'anger' : anger,
        'disgust' : disgust,
        'fear' : fear,
        'joy' : joy,
        'sadness' : sadness
    }
    
    # get name of dominant emotion
    dominant_emotion = max(scores, key=scores.get)

    # check if dominant emotion is none
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # return output 
    return f"""
    For the given statement, the system response is 'anger' : {scores['anger']}, 
    'disgust' : {scores['disgust']}, 'fear" : {scores['fear']}, 
    'joy' : {scores['joy']}, 'sadness' : {scores['sadness']}.
    The dominant emotion is {dominant_emotion}.
    """

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)