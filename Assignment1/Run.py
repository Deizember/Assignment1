import requests


test = requests.get("http://www.facebook.com/Onichan27")

outfile = open("C:/Users/dicay/Downloads/Project/LearningPythonRequest/test.txt", "w")
test.encoding = 'ISO-8859-1'

outfile.write(str(test.text.encode('utf-8')))
