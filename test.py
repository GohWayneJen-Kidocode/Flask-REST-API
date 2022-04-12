import requests

BASE = "http://127.0.0.1:5000/"

#data = [{"name": "Python REST API Tutorial - Building a Flask REST API", "views": 437000, "likes": 10000},
#        {"name": "How to make a new file in Windows 10", "views": 2370000, "likes": 573000}]
#
#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print (response.json())

#response = requests.patch(BASE + "video/1", {"views":438000})

response = requests.get(BASE + "video/1")
print (response.json())