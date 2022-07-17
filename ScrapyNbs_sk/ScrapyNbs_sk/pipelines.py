# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapynbsSkPipeline:
    def __init__(self):
        self.con = sqlite3.connect("articles.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS articles(
        date TEXT,
        name TEXT,
        url PRIMARY KEY,
        labels TEXT,
        content TEXT
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO articles VALUES (?,?,?,?,?)""", (
            item['date'],
            item['name'],
            item['url'],
            item['labels'],
            item['content']
        ))
        self.con.commit()
        return item
