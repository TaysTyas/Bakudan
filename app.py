from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
# from sklearn from linear_model
app = Flask(__name__)
#Load model and dataset 
model = LinearRegression()
# model.fit(x,y)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from user
    data = request.get_json()
    gender = data['weight-height.csv']
    height = data['weight-height.csv']
    weight = data['weight-height.csv']

  # Use model to make prediction
    prediction = model.predict([[gender, height, weight]])

    return {'predicted_weight': prediction[0]}

@app.route('/Predictions')
def index():
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(debug=True)