import requests
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

data = pickle.loads(requests.get(url).text)

for row in data:
  result = ''
    for chars in row:
      result += chars[0] * chars[1]
    print result
