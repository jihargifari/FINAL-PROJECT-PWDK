from flask import Flask, render_template, request 
import joblib
import pandas as pd

app = Flask(__name__)
data_ecommerce = pd.read_csv("MODULE 3\FINAL PROJECT\dashboard\E-commerce_data_clean.csv")

@app.route('/')
def home():     
    return render_template('home.html')

@app.route('/dataset', methods=['POST', 'GET'])
def dataset():
    return render_template('dataset.html', tables = [data_ecommerce.to_html(classes='data', index=False)])

@app.route('/clustervisualization', methods=['POST', 'GET'])
def clustervisualization():
    return render_template('cluster_vis.html')

@app.route("/prediction", methods=['POST', 'GET'])
def prediction():
    return render_template("prediction.html")

@app.route('/prediction_result', methods=['POST', 'GET'])
def prediction_result():
    input = request.form
    
    if request.method == "POST":
        input = request.form
        prediksi = model.predict([[
            float(input['Quantity']), float(input['UnitPrice']),  float(input['TotalCost']),
            float(input['Hours']),  float(input['Days']), float(input['DayOfMonth']),  
            float(input['Months']),  float(input['Cluster_Group 1']), float(input['Cluster_Group 2']), 
            float(input['Cluster_Group 3']), float(input['Cluster_Group 4'])
        ]])[0]
        if prediksi == 0 :
            prediksi = "This order is NOT going to be Cancelled, Keep it up!"
        elif prediksi == 1: 
            prediksi = "This Order is going to be Cancelled, be prepared" 
        return render_template('prediction_result.html', data = input, pred = prediksi)

if __name__ == '__main__' :
    model = joblib.load(r'C:\Users\HP.LAPTOP-5BTBEJFV\Documents\data science\MODULE 3\FINAL PROJECT\model_final_1')
    app.run(debug=True)


        # if input['cluster'] == 1 :
        #     data['Cluster_Group 1'] = 1
        #     data['Cluster_Group 2'] = 0
        #     data['Cluster_Group 3'] = 0
        #     data['Cluster_Group 4'] = 0
        # elif input['cluster'] == 2 :
        #     data['Cluster_Group 1'] = 0
        #     data['Cluster_Group 2'] = 1
        #     data['Cluster_Group 3'] = 0
        #     data['Cluster_Group 4'] = 0
        # elif input['cluster'] == 3 :
        #     data['Cluster_Group 1'] = 0
        #     data['Cluster_Group 2'] = 0
        #     data['Cluster_Group 3'] = 1
        #     data['Cluster_Group 4'] = 0
        # elif input['cluster'] == 4 :
        #     data['Cluster_Group 1'] = 0
        #     data['Cluster_Group 2'] = 0
        #     data['Cluster_Group 3'] = 0
        #     data['Cluster_Group 4'] = 1