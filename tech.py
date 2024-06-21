from flask import Flask, request, jsonify
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import speech_recognition as sr
import nltk
from transformers import pipeline
import mysql.connector
# Ensure you have downloaded the NLTK data required
nltk.download('punkt')
app = Flask(__name__)
# Load the question answering model from transformers
qa_pipeline = pipeline("question-answering")

# importing required libraries


# creating database
#cursorObject.execute("CREATE DATABASE geeks4geeks")
@app.route('/upload', methods=['GET','POST'])
def upload_audio():

     
    dataBase = mysql.connector.connect(
    host ='127.0.0.1',
    user ="root",
    passwd ="12345678",
    database ="test"
    )
 
# preparing a cursor object
    cursor = dataBase.cursor()

#Retrieving single row
    sql = '''SELECT * from product'''

#Executing the query
    cursor.execute(sql)

#Fetching 1st row from the table
    result = cursor.fetchone();
    print(result)

#Fetching 1st row from the table
    result = cursor.fetchall();
    print(result)

#Closing the connection
    dataBase.close()
 
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)
    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("Recognized Text: ", text)
        context = "hello how are you! Currently the time is 12:00PM"
        answer = qa_pipeline(question=text, context=context)
        return jsonify({"recognized_text": text, "answer": answer['answer']}), 200
    except sr.UnknownValueError:
        return jsonify({"error": "Google Web Speech could not understand audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Could not request results from Google Web Speech service; {e}"}), 500
if __name__ == '__main__':
    app.run(debug=True)