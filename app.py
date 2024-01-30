from flask import Flask, request
from utils import py_dictionary

app = Flask(__name__)

@app.route("/")
def index():
    search = request.args.get("search", "")
    
    res = py_dictionary.search_dictionary(search)

    return {
        "Search": search,
        "Definition": res
    }
    
