import requests

sample = ["39104", "Magdeburg", "Alter Markt", "Sachsen-Anhalt"]

def request_telekom(IN_PLZ, IN_CITY, IN_STREET, IN_STATE):
    r1 = requests.get(
        "https://t-map.telekom.de/tmap2/coverage_checker/search/?q=" + IN_PLZ + "+" + IN_CITY + "++" + IN_STREET + "++" + IN_STATE + "=1")
    json_resp = r1.json()
    OSM_X = str(json_resp['features'][0]['geometry']['coordinates'][0])
    OSM_Y = str(json_resp['features'][0]['geometry']['coordinates'][1])
    OSM_ID = str(json_resp['features'][0]['properties']['osm_id'])

    r2 = requests.get(
        "https://t-map.telekom.de/tmap2/coverage_checker/hpac/?klsId=" + OSM_ID + "&x=" + OSM_X + "&y=" + OSM_Y)
    json_resp2 = r2.json()
    if json_resp2["maxSpeed"]['available']:
        # Kbits/s Mbit/s delete "/1000" for Kbit/s
        data_to_save = (str(int(json_resp2["maxSpeed"]['available'] / 1000)))
    else:
        # it could be there is no internet connection
        data_to_save = ("NO DATA")
    return data_to_save

print(request_telekom(sample[0], sample[1], sample[2], sample[3]))
