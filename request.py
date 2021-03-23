import requests

url = 'http://localhost:2000/predict_ap'
r = requests.post(url,json={'bedrooms':2, 'bathrooms':2, 'floors':2,'waterfront':1, 
                            'view':2, 'condition':3,'grade':6})

