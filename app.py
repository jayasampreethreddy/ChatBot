import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from tensorflow.keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json', encoding="utf8").read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    print("final result = ", result)
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    try:
        res = getResponse(ints, intents)
    except:
        print("An exception occured")
        res = "I can't answer this query. I am really sorry but this is out of my limitation"
    return res

from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def hello():
    return jsonify({"key" : "home page value"})

def decrypt(msg):
    string = msg
    new_string = string.replace("+", " ")
    return new_string

@app.route('/home/<name>') 
def hello_name(name):
    print(f"Received name: {name}")
    dec_msg = decrypt(name)
    response = chatbot_response(dec_msg)
    json_obj = jsonify({"top" : {"res" : response}})
    return json_obj

if __name__ == '__main__':
    app.run(debug=True)