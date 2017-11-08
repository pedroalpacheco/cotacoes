# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ScrapyMoedasSqlPipeline(object):
    def process_item(self, item, spider):
        self.conn.execute(
            'insert into dolar(compra, venda, data) values (:compra, :venda, :data)',
            item
        )
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "dolar"'
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table dolar(id integer primary key, compra text, venda text, data text)'
            )

    def open_spider(self, spider):
        self.conn = sqlite3.connect('../db.sqlite3')
        self.create_table()

    def close_spider(self):
        self.conn.close()