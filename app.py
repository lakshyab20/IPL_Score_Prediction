# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Ridge Regression \odel
filename = 'ipl_score_pred_model_lr.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
#         Venue = request.form['venue']
#         if Venue == 'Kolkata':
#             temp_array = temp_array + [1,0,0,0,0,0,0,0]
#         elif Venue == 'Delhi':
#             temp_array = temp_array + [0,1,0,0,0,0,0,0]
#         elif Venue == 'Bangalore':
#             temp_array = temp_array + [0,0,1,0,0,0,0,0]
#         elif Venue == 'Chennai':
#             temp_array = temp_array + [0,0,0,1,0,0,0,0]
#         elif Venue == 'Hyderabad':
#             temp_array = temp_array + [0,0,0,0,1,0,0,0]
#         elif Venue == 'Jaipur':
#             temp_array = temp_array + [0,0,0,0,0,1,0,0]
#         elif Venue == 'Mumbai':
#             temp_array = temp_array + [0,0,0,0,0,0,1,0]
#         elif Venue == 'Mohali':
#             temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit =(10)-my_prediction, upper_limit =(-5)-my_prediction)



if __name__ == '__main__':
	app.run(debug=True)