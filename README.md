# Whois-Abuse
Insert an IP list and get the Country and Abuse E-Mails

Running goes something like:
<pre>
python whois_ip.py 
{'8.8.8.8\n': {'Country': ['United States'], 'ISP': [u'LVLT-GOGL-8-8-8'], 'emails': [u'network-abuse@google.com', u'arin-contact@google.com'], 'abuse': u'network-abuse@google.com'}, '1.1.1.1\n': {'Country': ['Australia'], 'ISP': [u'APNIC-LABS'], 'emails': [u'research@apnic.net', u'abuse@apnic.net'], 'abuse': u'abuse@apnic.net'}}
</pre>
