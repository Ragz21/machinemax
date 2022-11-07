# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from settings import MONGO_DB, MONGO_URI


class MachinemaxPipeline:
    """
        Scrapy pipeline to establish connection to MongoDB

        Attributes
        ----------
            collection_name : str
                Name of the mongoDB collection.
            mongo_uri : str
                MongoDB connection string.
            mongo_db : str
                MongoDB name.
    """
    collection_name = 'articles'
    mongo_uri = MONGO_URI
    mongo_db = MONGO_DB

    def __init__(self):
        """
            Initialise a db connection to mongo
        """
        self.conn = pymongo.MongoClient(
            self.mongo_uri,
            27017
        )
        db = self.conn[self.mongo_db]
        self.collection = db[self.collection_name]

    def process_item(self, item, spider):
        """
            Default method to handle insertion of crawled articles to the collection.

            Parameters
            ----------
            item : Iterable
                These are the items list scraped by the spider.
            spider :
                mentions the spider used to scrape.

            Returns
            -------
            MachinemaxItem
                Parsed article
        """
        self.collection.insert(dict(item))
        return item
