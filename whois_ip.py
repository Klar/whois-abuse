from ipwhois import IPWhois

# for mappings  like CH to Switzerland
from ipwhois.utils import get_countries
countries = get_countries()

#define input file
input_file = 'ips.txt'

#read file and create a list
list_file = open(input_file)
my_list = list_file.readlines()
list_file.close()

#for testing purpose only
my_list = ['111.111.111.111','222.222.222.222']

try:
	for ip in my_list:
		response = IPWhois(ip.strip("\n")).lookup_whois()
		print "%s - %s" % (ip, countries[response['asn_country_code']])
		for mail in response["nets"][0]["emails"].split():
			print " * %s" % mail
		print "\n"
except Exception, e:
	print e
