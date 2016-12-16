import requests
name = raw_input("Qual seu nome:")
end = raw_input("Qual seu endereco:")
url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + end
response = requests.get(url)
data = response.json()
print str(name) + " seu endereco e: " + str(data['results'][0]['formatted_address'])
fh = open("Endereco.json","w")
fh.write(response.content)
fh.close()
