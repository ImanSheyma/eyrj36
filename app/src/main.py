import os
from flask import Flask
from database import init_db
from views import views
import errors

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.register_error_handler(404, errors.page_not_found)
app.secret_key = os.getenv('KEY')
init_db(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0')