from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)


try:
    model = joblib.load('sarima.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Set model to None if loading fails

try:
    df_train = pd.read_csv('df_train.csv', index_col='MONAT', parse_dates=True)
    print("Training data loaded successfully.")
except Exception as e:
    print(f"Error loading training data: {e}")
    df_train = None  # Set df_train to None if loading fails

@app.route('/')
def index():
    return jsonify(message="Root endpoint hit"), 200

@app.route('/invocations', methods=['POST'])
def invocations():
    # Ensure that global variables are accessible
    global model, df_train
    data = request.get_json()
    print("Invocation endpoint hit")
    print(f"Received data: {data}")
    
    year = data['year']
    month = data['month']
    try:
       
        target_date = pd.Timestamp(year=year, month=month, day=1)
        last_known_date = df_train.index[-1]
        steps_to_forecast = (target_date.year - last_known_date.year) * 12 + target_date.month - last_known_date.month

        
        if steps_to_forecast > 0:
            prediction = model.get_forecast(steps=steps_to_forecast).predicted_mean.iloc[-1]
        else:
            # If the target date is in the past or present, use historical data
            prediction = df_train.loc[target_date.strftime('%Y-%m-%d')]['WERT'] if target_date in df_train.index else "Unknown date"

    except Exception as e:
        print(f"Error during prediction: {e}")
        prediction = str(e)

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)



