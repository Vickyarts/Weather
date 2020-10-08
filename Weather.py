import requests
import datetime
import os
import sys
from bs4 import BeautifulSoup

siteurl = 'https://www.timeanddate.com'
authorsite = 'https://github.com/Vickyarts'


def show_weather(properties):
	clear_screen()
	now = datetime.datetime.today()
	print('')
	print('\t\t\tLIVE Weather Report')
	print('')
	print('\t\tDate: ' + str(now.day) + '.' + str(now.month) + '.' + str(now.year))
	print('\t\tTime: ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second))
	print('\t\tLocation: ' + properties['location'])
	print('\t\tTemperature: ' + properties['temperature'])
	if properties['pressure'] == 'No data':
		print('\t\tPressure: ' + properties['pressure'])
	else:
		print('\t\tPressure: ' + properties['pressure'] + ' mbar')
	print('\t\tVisibility: ' + str(properties['visibility']).upper())
	print('\t\tHumidity: ' + properties['humidity'])
	print('\t\tSite: ' + authorsite)
	print('')

def clear_screen():
	"""Clears the screen"""
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")

def remove_scripts(soup):
  [s.extract() for s in soup('script')]

def property_dict(propers):
	try:
		if len(propers) == 17:
			propers.insert(3,' ')
			propers.insert(3,' ')
			proper_dict = {}
			proper_dict['location'] = propers[1][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		elif len(propers) == 18:
			propers.insert(4,' ')
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		elif len(propers) == 19:
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2] + ' ' + propers[3][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		elif len(propers) == 20:
			del propers[7]
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2] + ' ' + propers[3] + ' ' + propers[4][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		elif len(propers) == 21:
			del propers[8]
			del propers[8]
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2] + ' ' + propers[3] + ' ' + propers[4] + ' ' + propers[5][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		elif len(propers) == 22:
			del propers[8]
			del propers[8]
			del propers[8]
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2] + ' ' + propers[3] + ' ' + propers[4] + ' ' + propers[5] + ' ' + propers[6][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]		
		elif len(propers) == 23:
			del propers[8]
			del propers[8]
			del propers[8]
			del propers[8]
			proper_dict = {}
			proper_dict['location'] = propers[1] + ' ' + propers[2] + ' ' + propers[3] + ' ' + propers[4] + ' ' + propers[5] + ' ' + propers[6] + ' ' +  propers[7][0:-7]
			templength = propers[18].find('\xa0')
			proper_dict['temperature'] = propers[18][0:templength] + ' ' + propers[18][-2:]
			proper_dict['humidity'] = propers[16][0:-3]
			visiblength = propers[14].find('Pressure')
			proper_dict['visibility'] = propers[14][0:visiblength]
			proper_dict['pressure'] = propers[14][visiblength+8:]
		else:
			na = 'No data'
			proper_dict = {}
			proper_dict['location'] = na
			proper_dict['temperature'] = na
			proper_dict['humidity'] = na
			proper_dict['visibility'] = na
			proper_dict['pressure'] = na
	except Exception:
		print('Oops, something went wrong!')
		print('')
		sys.exit()
	else:
		return proper_dict

def redirect(reurl):
	try:
		redirect_url = siteurl + reurl
		resite = requests.get(redirect_url).text
		resoup = BeautifulSoup(resite,'lxml')
		remove_scripts(resoup)
		proper = resoup.find('table', class_="table table--left table--inner-borders-rows")
		proper_split = proper.text.split(' ')
		properties = property_dict(proper_split)
		show_weather(properties)
	except Exception:
		print('Oops, something went wrong!')
		print('')
		sys.exit()

def search(city):
	try:
		weather_search = siteurl + '/weather/?query=' + city
		searchsite = requests.get(weather_search).text
	except requests.exceptions.ConnectionError:
		print('You need active internet connection!')
		print('')
		sys.exit()
	except Exception:
		print('Oops, something went wrong!')
		print('')
		sys.exit()
	else:
		soup = BeautifulSoup(searchsite,'lxml')
		links = soup.find_all('a')
		link = links[123]
		reurl = link.get('href')
		redirect(reurl)

def run():
	try:
		if len(sys.argv) == 2:
			search(sys.argv[1])
		else:
			city = input('Enter your city: ')
			search(city)
	except KeyboardInterrupt:
		print('Visit: ' + authorsite)
		print('')
		sys.exit()
	except Exception:
		print('Oops, something went wrong!')
		print('')

if __name__ == "__main__":
	run()
