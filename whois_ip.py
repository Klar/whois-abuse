import time
import traceback
from ipwhois import IPWhois
import pprint

# for mappings  like CH to Switzerland
from ipwhois.utils import get_countries
countries = get_countries()

#define input file
input_file = 'ips.txt'

#read file and create a list
list_file = open(input_file)
iplist = list_file.readlines()
list_file.close()

ip_abuse = {}

for ip in iplist:
	try:
		ip = str(ip)
		ip_abuse[ip] = {'ISP':[], 'Country':[], 'abuse':[],'emails':[]}

		obj = IPWhois('{}'.format(ip.strip("\n")))
		result = obj.lookup_rdap(depth=1)

		#pprint.pprint(result)
		
		for r_object in result['objects']:

			if result['objects'][r_object]['contact']['email']:

				email = result['objects'][r_object]['contact']['email'][0]['value']

				ip_abuse[ip]["emails"].append(email)
			
		for mail in ip_abuse[ip]["emails"]:
			if "abuse" in mail:
				ip_abuse[ip]["abuse"] = mail	


		country = countries[result['asn_country_code']]
		ip_abuse[ip]["Country"].append(country)
		
		isp = result['network']['name']
		ip_abuse[ip]["ISP"].append(isp)



	except:
		print str(traceback.format_exc())
		print "no whois for %s" %ip
		continue

	time.sleep(2)

print ip_abuse

#for key, value in ip_abuse.items():
#	print key
#	print value
