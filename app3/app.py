from flask import request, Flask
import json, socket
import computeEngine 

#import hashlib,random


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is backend  ! ' + str(socket.gethostname()) + ' \n'

@app.route("/compute", methods=["POST"])
def compute():
    hostName = socket.gethostname()

    bc = computeEngine.BackendCompute(hostName)
    random_joke = bc.get_a_joke()

    returnDictionary = {}
    returnDictionary["hostname"] = hostName
    returnDictionary["randomjoke"] = random_joke
    
    return json.dumps(returnDictionary,ensure_ascii=False)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
