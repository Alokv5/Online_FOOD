import requests
import json
from geopy.geocoders import Nominatim


my_address = ""
city = ""
class LocationMiddleware:
    def __init__(self, get_response):

        self.get_response=get_response
        send_url = "http://api.ipstack.com/check?access_key=9c621eede65735f07bef4f8d9e72a045"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        city1 = geo_json['city']

        latlang = str(latitude) + "," + str(longitude)
        geolocator = Nominatim(user_agent="Online Food  Services")
        location = geolocator.reverse(latlang)

        global my_address ,city
        my_address = location.address
        city= city1



    def __call__(self, request):
      response = self.get_response(request)
      return response

def returnAddress():
    return my_address,city


