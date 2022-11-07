run:
    pip install -r requirements.txt
	python3 -m pytest
	python3 -m unittest discover
    scrapy crawl theguardian
    flask --app server run
