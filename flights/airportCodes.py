import requests
import bs4
import wikipediaapi
import re

airports = ["Houari Boumediene Airport","Zvartnots International Airport","Adelaide Airport","Canberra International Airport","Melbourne Airport","Perth Airport","Sydney Airport","Vienna International Airport","Ministro Pistarini International Airport","Heydar Aliyev International Airport","Shahjalal International Airport","Brussels Airport","Liège Airport","Sarajevo International Airport","São Paulo–Guarulhos International Airport","Sofia Airport","Phnom Penh International Airport","Halifax Stanfield International Airport","Montréal–Pierre Elliott Trudeau International Airport","Beijing Capital International Airport","Chengdu Shuangliu International Airport","Chongqing Jiangbei International Airport","Guangzhou Baiyun International Airport","Hangzhou Xiaoshan International Airport","Hong Kong International Airport","Macau International Airport","Shanghai Pudong International Airport","Zagreb Airport","Larnaca International Airport","Václav Havel Airport Prague","Copenhagen Airport","Djibouti–Ambouli International Airport","Mariscal Sucre International Airport","Addis Ababa Bole International Airport","Helsinki Airport","Nice Côte d'Azur Airport","Charles de Gaulle Airport","Tbilisi International Airport","Berlin Tegel International Airport","Frankfurt am Main International Airport","Munich Airport","Kotoka International Airport","Athens International Airport","Mykonos International Airport","Thessaloniki International Airport","Budapest Ferenc Liszt International Airport","Sardar Vallabhbhai Patel International Airport","Sri Guru Ram Dass Jee International Airport","Kempegowda International Airport","Chennai International Airport","Indira Gandhi International Airport","Goa International Airport","Rajiv Gandhi International Airport","Cochin International Airport","Netaji Subhash Chandra Bose International Airport","Calicut International Airport","Chatrapati Shivaji International Airport","Dr. Babasaheb Ambedkar International Airport","Trivandrum International Airport","Ngurah Rai International Airport","Soekarno–Hatta International Airport","Isfahan International Airport","Mashhad International Airport","Shiraz International Airport","Tehran Imam Khomeini International Airport","Basra International Airport","Baghdad International Airport","Erbil International Airport","Al Najaf International Airport","Sulaymaniyah International Airport","Dublin Airport","Milan–Malpensa Airport","Pisa International Airport","Leonardo da Vinci–Fiumicino Airport","Venice Marco Polo Airport","Haneda International Airport","Narita International Airport","Queen Alia International Airport","Moi International Airport","Jomo Kenyatta International Airport","Kuwait International Airport","Beirut–Rafic Hariri International Airport","Luxembourg Findel Airport","Kuala Lumpur International Airport","Penang International Airport","Velana International Airport","Malta International Airport","Guadalajara International Airport","Mexico City International Airport","Mohammed V International Airport","Marrakesh Menara Airport","Maputo International Airport","Yangon International Airport","Hosea Kutako International Airport","Tribhuvan International Airport","Amsterdam Airport Schiphol","Auckland International Airport","Murtala Muhammed International Airport","Oslo Gardermoen Airport","Muscat International Airport","Salalah International Airport","Sohar Airport","Faisalabad International Airport","Islamabad International Airport","Jinnah International Airport","Allama Iqbal International Airport","Multan International Airport","Bacha Khan International Airport","Sialkot International Airport","Clark International Airport","Ninoy Aquino International Airport","Warsaw Frédéric Chopin International Airport","Hamad International Airport","Skopje International Airport","Henri Coandă International Airport","Domodedovo International Airport","Pulkovo International Airport","Kigali International Airport","Belgrade Nikola Tesla Airport","Seychelles International Airport","Singapore Changi International Airport","Cape Town International Airport","King Shaka International Airport","O. R. Tambo International Airport","Incheon International Airport","Barcelona–El Prat Airport","Adolfo Suárez Madrid–Barajas Airport","Málaga Airport","Zaragoza Airport","Bandaranaike International Airport","Khartoum International Airport","Stockholm Arlanda Airport","Göteborg Landvetter Airport","EuroAirport Basel Mulhouse Freiburg","Geneva International Airport","Zürich International Airport","Julius Nyerere International Airport","Kilimanjaro International Airport","Abeid Amani Karume International Airport","Suvarnabhumi International Airport","Chiang Mai International Airport","Krabi International Airport","Phuket International Airport","Tunis-Carthage International Airport","Adana Şakirpaşa Airport","Esenboğa International Airport","Antalya Airport","Milas–Bodrum Airport","Hatay Airport","Istanbul Atatürk International Airport","Istanbul Sabiha Gökçen International Airport","Entebbe International Airport","Boryspil International Airport","Birmingham Airport","Cardiff Airport","Edinburgh Airport","London Gatwick International Airport","London Heathrow International Airport","London Stansted Airport","Manchester Airport","Hartsfield–Jackson Atlanta International Airport","Boston Logan International Airport","Chicago O'Hare International Airport","Dallas/Fort Worth International Airport","George Bush Intercontinental Airport","Los Angeles International Airport","Miami International Airport","John F. Kennedy International Airport","Philadelphia International Airport","Pittsburgh International Airport","Washington Dulles International Airport","Da Nang International Airport","Noi Bai International Airport","Tan Son Nhat International Airport"]
test= ["Houari Boumediene Airport"]

aircodes = dict()

wiki=wikipediaapi.Wikipedia('en')

#go to wikipedia page and grab the IATA code store in dict
for a in airports:
	a=a.replace(" ","_")
	page= wiki.page(a)
	m =re.search("IATA:...." , page.summary)
	if m:
		result=m[0][-3:]
	else:
		print(a)
	#print('https://en.wikipedia.org/wiki/'+a)
	#r = requests.get('https://en.wikipedia.org/wiki/'+a)
	#r2 = requests.get(r.url)
	#print(r)
	aircodes[a] = result
	#if r is not None:
	#	html = bs4.BeautifulSoup(r.text, 'html.parser')
	#	print(r)

print(aircodes)
print([aircodes.values()])