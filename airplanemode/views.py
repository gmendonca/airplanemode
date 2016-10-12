from airplanemode import app
from core import airplanehub

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/lowest_prices')
def lowest_prices():
    lf = airplanehub.LowestFare('FLN','SAO','2016-11-11','2016-11-14')
    return lf.find()
