from flask import Flask
from flask_restful import Api
# import route that will serve housing predictions
from predictprices import predictprices

# instantiate flask server
app = Flask(__name__)
api = Api(app)

api.add_resource(predictprices, '/house')

if __name__ == '__main__':
    app.run(debug=True)

