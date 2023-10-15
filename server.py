"""Module providing a server functionality for final project."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    ''' This function to detect emotion'''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return f"For the given statement, the system response is 'anger': {response['anger']},"\
            f" 'disgust': {response['disgust']}, 'fear': {response['fear']}, "\
            f"'joy': {response['joy']} and "\
            f" 'sadness': {response['sadness']}. "\
            f" The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
