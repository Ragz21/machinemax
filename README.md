# Machinemax 
A solution that crawls for articles from a news website (theguardian.com), stores in a
mongo database then makes it available to search via an API.
## Installation
Update MONGO_URI in settings.py with your MongoDB connection credentials
Then run the command :
```bash
make run
```
## Spider
The data crawled is in the following format

1. author of type Array of strings
2. headline of type String
3. content of type String	
4. url of type String
5. published_at of type Date

## Flask API
Following APIs are provided
### GET /
Response:
```commandline
{
    "status": "success",
    "count": 90,
    "results": [
        {
            "_id": {
                "$oid": "636226dae7a5c118d7a371c9"
            },
            "author": [],
            "headline": "North Korea missile crosses maritime border...",
            "content": "North Korea fired at least 10 missiles off its ...",
            "url": "https://www.theguardian.com/world/2022/nov/02/north...",
            "published_at": null
        },
        {
            "_id": {
                "$oid": "636226dbe7a5c118d7a371ca"
            },
            "author": [],
            "headline": "Liz Cheney backs second Democrat, picking Ryan ...",
            "content": "The Republican congresswoman Liz Cheney has now ...",
            "url": "https://www.theguardian.com/us-news/2022/nov/02/liz-...",
            "published_at": null
        }
    ]
}
```
### GET /search
Uri:
```commandline
http://127.0.0.1:5000/search?query=<>
```
Response:
```commandline
{
    "status": "success",
    "count": 1,
    "results": [
        {
            "_id": {
                "$oid": "636226dfe7a5c118d7a371d5"
            },
            "author": [],
            "headline": "Southgate criticised for claiming Qatar workers...",
            "content": "Gareth Southgate is facing criticism from human ...",
            "url": "https://www.theguardian.com/football/2022/nov/01/gareth...",
            "published_at": null
        }
    ]
}
```
