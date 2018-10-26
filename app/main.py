from flask import Flask
import time
from flask import request
from logging.handlers import RotatingFileHandler
import json
from math import pow, sqrt, log, sin
from logging.config import dictConfig    

dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s.%(funcName)s Line %(lineno)s: %(message)s',
        }},
        'handlers': {'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'active.log',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['file']
        }
    })

app = Flask(__name__)


def sum_of_digits(key):
    key = str(key)
    summa = 0
    for k in key:
        if str.isdigit(k):
            summa += int(k)
    print(summa)
    return summa

def is_in(user_id):
    if sum_of_digits(user_id) == 33:
        return True
    else:
        return False


def calculate(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):
	try:
		return pow(3.141592653589793, d1 * d2) * sqrt(2.0 * d3) - 1.0 / sin(d4) +log(d3 + d5) - d9 / d10 * sqrt(d7 / d8) - d2 * d7
	except Exception:
		return -1e30

@app.route("/get_value/<user_id>/")
def get_value(user_id):
	try:
		if is_in(user_id):
			d1 = request.args.get('d1', default=2, type=float)
			d2 = request.args.get('d2', default=2, type=float)
			d3 = request.args.get('d3', default=2, type=float)
			d4 = request.args.get('d4', default=2, type=float)
			d5 = request.args.get('d5', default=2, type=float)
			d6 = request.args.get('d6', default=2, type=float)
			d7 = request.args.get('d7', default=2, type=float)
			d8 = request.args.get('d8', default=2, type=float)
			d9 = request.args.get('d9', default=2, type=float)
			d10 = request.args.get('d10', default=2, type=float)

			time.sleep(1)

			params  = {"d1": d1, "d2": d2, "d3": d3, "d4": d4, "d5": d5, 
					   "d6": d6, "d7": d7, "d8": d8, "d9": d9, "d10": d10}

			value = calculate(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10)

			r = {}
			r["request"] = params
			r["response"] = value

			r = json.dumps(r)

			app.logger.error("user_id: {}, response: {}".format(user_id, r))
			return r
		else:
			return "Invalid Key. Contact @pavel via slack to get api key"
	except Exception as e:
		return "Unexpected Error. The creator is dummy, contact him and tell what you think about him via slack @pavel \n:{}".format(str(e))

@app.route("/get_stat/")
def get_stat():
    return str(users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80, threaded=True)
