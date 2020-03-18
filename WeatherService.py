from flask import Flask
from sense_hat import SenseHat
from SensorReadings import SensorReadings

app = Flask(__name__)

@app.route('/sensors')
def get_sensor_readings():
    return SensorReadings(sense_hat).getAsMap()