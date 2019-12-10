##
## Sample Flask REST server
##

from flask import Flask, request, Response
import jsonpickle
from cassandra.cluster import Cluster


# Initialize the Flask application
app = Flask(__name__)

cluster = Cluster(['cassandra'],port=9042)
session = cluster.connect('iot')
BYMIN="minutelytelemetry"
BYHOUR="hourlytelemetry"
BYDAY="dailytelemetry"

# if buildingName == 'All':
# else:
#     query = "SELECT buildingId FROM buildinginfo where buildingname={} ALLOW FILTERING".format(buildingName)
#     buildings = session.execute(query)

@app.route('/iot/aggregate/byminute/<buildingId>', methods=['GET'])
def aggregateBymin(buildingId):
    query = "SELECT deviceid, devicename FROM deviceinfo where buildingid={} ALLOW FILTERING".format(buildingId)
    devices = session.execute(query)
    responses =[]
    for device in devices:
        query = "SELECT * FROM {} where deviceid={} ALLOW FILTERING".format(BYMIN, device.deviceid)
        print(query)
        queryResponse = session.execute(query)
        for response in queryResponse:
            resObject = {"buildingId" : buildingId, "deviceId":device.deviceid,  "count" : response.count, "max" : response.max , "min" : response.min, "mean": response.mean}
            responses.append(resObject)

    return Response(response=jsonpickle.encode(responses), status=200, mimetype="application/json")

@app.route('/iot/aggregate/byhour/<buildingId>', methods=['GET'])
def aggregateByhour(buildingId):
    query = "SELECT deviceid, devicename FROM deviceinfo where buildingid={} ALLOW FILTERING".format(buildingId)
    devices = session.execute(query)
    responses = []
    for device in devices:
        query = "SELECT * FROM {} where deviceid={} ALLOW FILTERING".format(BYHOUR, device.deviceid)
        print(query)
        queryResponse = session.execute(query)
        for response in queryResponse:
            resObject = {"buildingId": buildingId, "deviceId": device.deviceid, "count": response.count,
                         "max": response.max, "min": response.min, "mean": response.mean}
            responses.append(resObject)

    return Response(response=jsonpickle.encode(responses), status=200, mimetype="application/json")


@app.route('/iot/aggregate/byday/<buildingId>', methods=['GET'])
def aggregateByDay(buildingId):
    query = "SELECT deviceid, devicename FROM deviceinfo where buildingid={} ALLOW FILTERING".format(buildingId)
    devices = session.execute(query)
    responses =[]
    for device in devices:
        query = "SELECT * FROM {} where deviceid={} ALLOW FILTERING".format(BYDAY, device.deviceid)
        print(query)
        queryResponse = session.execute(query)
        for response in queryResponse:
            resObject = {"buildingId" : buildingId, "deviceId":device.deviceid,  "count" : response.count, "max" : response.max , "min" : response.min, "mean": response.mean}
            responses.append(resObject)

    return Response(response=jsonpickle.encode(responses), status=200, mimetype="application/json")

# route http posts to this method

# start flask app
app.run(host="0.0.0.0", port=5000)