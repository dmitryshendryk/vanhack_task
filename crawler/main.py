from flask import Flask 
from flask_restful import Resource, Api
from flask import request
from crawler import AnalyzeParser
from flask import abort


app = Flask(__name__)

@app.route('/api/ping', methods=['GET'])
def ping():
    return {"ping":"pong"}, 200

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q')
    parser = AnalyzeParser()
    text_links = parser.run_parser(5, query)
    return text_links 

@app.errorhandler(404)
def page_not_found(error):
    return {"Error":"Page not found"}, 404


if __name__ == '__main__':
    app.run(debug=True)