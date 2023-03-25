import requests
import time
from flask import Flask, jsonify
app = Flask(__name__)
USGS_API_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"
EMSC_API_URL = "https://www.seismicportal.eu/fdsnws/event/1/query"
GEOFON_API_URL = "https://geofon.gfz-potsdam.de/eqinfo/event.php"
KANDILLI_API_URL = "http://www.koeri.boun.edu.tr/sismo/liste-son-depremler/son-depremler.html"
@app.route('/earthquake-data')
def get_earthquake_data():
    last_usgs_time = 0
    last_emsc_time = 0
    last_geofon_time = 0
    last_kandilli_time = 0
    data = {"usgs": [], "emsc": [], "geofon": [], "kandilli": []}
    while True:
        # USGS API
        usgs_params = {
            "format": "geojson",
            "starttime": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(last_usgs_time)),
            "minmagnitude": 2.5,
            "orderby": "time",
        }
        usgs_response = requests.get(USGS_API_URL, params=usgs_params)
        usgs_data = usgs_response.json()
        if usgs_data["metadata"]["count"] > 0:
            data["usgs"].extend(usgs_data["features"])
            last_usgs_time = int(usgs_data["features"][-1]["properties"]["time"] / 1000)
        # EMSC API
        emsc_params = {
            "format": "geojson",
            "start": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime(last_emsc_time)),
            "minmag": 2.5,
            "orderby": "time",
        }
        emsc_response = requests.get(EMSC_API_URL, params=emsc_params)
        emsc_data = emsc_response.json()
        if emsc_data["metadata"]["count"] > 0:
            data["emsc"].extend(emsc_data["features"])
            last_emsc_time = int(emsc_data["features"][-1]["properties"]["time"] / 1000)
        # GEOFON API
        geofon_params = {
            "fmt": "json",
            "limit": 10,
            "minmag": 2.5,
            "start": last_geofon_time,
            "orderby": "time",
        }
        geofon_response = requests.get(GEOFON_API_URL, params=geofon_params)
        geofon_data = geofon_response.json()
        if geofon_data["result"]:
            data["geofon"].extend(geofon_data["result"])
            last_geofon_time = int(geofon_data["result"][-1]["time"] / 1000)
        # KANDILLI API
        kandilli_response = requests.get(KANDILLI_API_URL)
        kandilli_data = kandilli_response.text
        kandilli_data = kandilli_data.split("\n")[1:-1]
        for item in kandilli_data:
            item_data = item.split()
            timestamp_str = f"{item_data[0]} {item_data[1]}"