## Usage:
```python
from scraper import extractAllProvision, cleanSubProvisions

url = 'path/to/the/file.html'
result = cleanSubProvisions(extractAllProvision(url))


```

## Files:
- getChangeConUrls.py
  Get all urls of a specific party name

- scraper.py
  The file contains all functions that extract party name and information

- test.py
  Test file that contains test codes

- *.xlsx
  Test Results

## Requirments:
- lxml
- BeautifulSoup
- urllib
