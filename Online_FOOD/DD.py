# import requests
# import json
# from geopy.geocoders import Nominatim
#
# send_url = "http://api.ipstack.com/check?access_key=9c621eede65735f07bef4f8d9e72a045"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']
# print(city)
# print(latitude,longitude)
#
# latlang=str(latitude)+","+str(longitude)
#
# geolocator = Nominatim(user_agent="Online Food  Services")
# location = geolocator.reverse(latlang)
# print(location.address)
# print((location.latitude, location.longitude))

import  random
res=random.randint(10000,99999)
print(res)

