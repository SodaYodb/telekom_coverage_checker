# several years old
import requests

def request_telekom(IN_PLZ, IN_CITY, IN_STREET, IN_STATE):
    try:
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
            data_to_save = (str(int(json_resp2["maxSpeed"]['available'] / 1000)))
        else:
            data_to_save = ("NO DATA")
    except Exception:
        data_to_save = ("FAIL TOSM")
        time.sleep(1)
    return data_to_save
