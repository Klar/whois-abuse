import time

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
ip_abuse = {}

for ip in my_list:
	try:
		ip = str(ip)
		ip_abuse[ip] = {'Country':[],'email':[]}

		response = IPWhois(ip.strip("\n")).lookup_whois()
		con = countries[response['asn_country_code']]
		ip_abuse[ip]["Country"].append(con)

		for mail in response["nets"][0]["emails"].split():
			ip_abuse[ip]["email"].append(mail)
	except:
		print "no whois for %s" %ip
		continue

	time.sleep(2)

print ip_abuse
