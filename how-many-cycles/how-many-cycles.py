"""
Write a script or code that outputs how many Santander Cycles are available at the bike stand outside the Bank of England.

The JSON BikePoint API containing this information is available here:

https://api.tfl.gov.uk/swagger/ui/index.html

To save you time, the bike stand is called "Bank of England Museum, Bank".

You may use any scripting or coding language, and may use any helpful libraries etc to make the task easier, as you would in your normal work.
"""
from requests import get
from urllib.parse import urljoin

api_url = 'https://api.tfl.gov.uk'
bike_stand = 'Bank of England Museum, Bank'
search_url = urljoin(api_url, "BikePoint/Search")
searchresults = get(search_url, params={'query': bike_stand}).json()
bikepoint_url = urljoin(api_url, searchresults[0]['url'])
bikepoint_properties = get(bikepoint_url).json()['additionalProperties']
bikes = next(p['value'] for p in bikepoint_properties if p['key'] == "NbBikes")
print(bikes)
