import time
import sys

from requests_xml import XMLSession

session = XMLSession()

data = {
    'a': int(time.time() * 1000),
    'mode': 191,
    'producttype': 1,
    'username': sys.argv[1],
    'password': sys.argv[2]
}
r = session.post('http://172.16.0.1:8090/login.xml',data=data)
print(r.xml.xpath('//requestresponse//message')[0].text)
