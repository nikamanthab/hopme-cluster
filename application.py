from flask import Flask
from flask import request
import json
from cluster import Cluster
app = Flask(__name__)

cl = Cluster()

@app.route('/sendData',methods = ['GET'])
def getting():
    return "yoyo" 

@app.route('/sendData',methods = ['POST'])
def club():
    print(request.json)
    reqdict = request.json
    print(reqdict["lat_long"],reqdict["n_teams"])
    
    #send data to the class
    cl.sendCoordandTeam(reqdict["lat_long"],int(reqdict["n_teams"]))

    #fit
    cl.fit()

    res = {}
    #get centroids
    res["center"] = cl.getCentroids().tolist()

    #get classes
    res["classes"] = cl.getClasses().tolist()

    print(res)
    return json.dumps(res)
