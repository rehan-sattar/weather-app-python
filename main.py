import requests

cityName = input("Enter the city  Name : ")
api_address = 'http://api.openweathermap.org/data/2.5/weather?q='+cityName+'&appid=9f162c4a7576a32569f4374bd5fdff7b'
json_data = requests.get(api_address).json()
print(json_data)


#9f162c4a7576a32569f4374bd5fdff7b

