# -*- coding: utf-8 -*-
import requests
url = "http://34.125.54.7//test_py.php?test=hi"
response = requests.get(url)
print(response.content)
#print(response.json())
