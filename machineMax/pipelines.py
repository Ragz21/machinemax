# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo


class MachinemaxPipeline:

    collection_name = 'articles'
    mongo_uri = 'mongodb+srv://machineMax:<password>@cluster0.wmlolkb.mongodb.net/?retryWrites=true&w=majority'
    mongo_db = 'guardian'

    def __init__(self):
        # Creating a db connection to mongo
        self.conn = pymongo.MongoClient(
            self.mongo_uri,
            27017
        )
        db = self.conn[self.mongo_db]
        self.collection = db[self.collection_name]

    def process_item(self, item, spider):
        # Insertion of crawled articles to the collection
        self.collection.insert(dict(item))
        return item
