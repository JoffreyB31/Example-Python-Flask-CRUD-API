import logging
from logging.handlers import RotatingFileHandler

import connexion
from flask import render_template
from flask_cors import CORS

LOG_PATH = './logs/app.log'

# Application instance
app = connexion.App(__name__, specification_dir='./')
CORS(app.app)
app.add_api('swagger.yml')

# Logging
log_handler = RotatingFileHandler(
    LOG_PATH, mode='a', maxBytes=100 * 1024 * 1024, backupCount=10, encoding=None, delay=False)
log_handler.setLevel(logging.INFO)
app.app.logger.addHandler(log_handler)
app.app.logger.setLevel(logging.DEBUG)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL localhost:5000/
    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
