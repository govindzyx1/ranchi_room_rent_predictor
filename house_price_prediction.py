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
    message = request.get_json(force=True)#naik doesnt take data in json foramt thats why we have to add id column
    
    area=message['place']
    print(message)
    if area=='harmu':
        area=0;
    elif area=='kanke':
        area=1;
    message['place']=area
    message={'rooms':2,'garden':1, 'washroom':2, 'place':1}
   

    int_features = [int(x) for x in message.values()]
    final_features = [np.array(int_features)]
   
    
    prediction = model.predict(final_features)

    output = round(prediction[0], 3)# upto 3 decimal places

    return render_template('index.html', prediction_text='Rent of house should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
