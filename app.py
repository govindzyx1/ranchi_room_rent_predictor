import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    
    '''
    message=request.form.to_dict()# convert incoming immutable data to mutable
    area=message['place']
    print(message)
    if area=='harmu':
        area=0;
    elif area=='kanke':
        area=1;
    message['place']=area
    print(message)
    
    int_features = [int(x) for x in message.values()]
    print(int_features)
    
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    print(output)

    return render_template('index.html', prediction_text='Rent for above requirement Rs.{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
