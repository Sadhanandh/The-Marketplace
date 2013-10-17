from scrapy.exceptions import DropItem
from localbanya.settings import DBsettings
import MySQLdb
import json
import urllib
import os
from display import RawPublicdb

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        print DBsettings["HOST"]
        return item



class CleansePipeline(object):


    def process_item(self, item, spider):
        if True:
            return item
        else:
            raise DropItem("Item Unclean %s" % item)


class DjangoWriterPipeline(object):


    def process_item(self, item, spider):
        dummy = None
        try:
            dummy =  RawPublicdb.objects.get(Hsh=item["Hsh"])
        except Exception :
            pass
        if dummy == None:
            item["Crp"] = item["Mrp"]
            item["Url"] = "/image/%s.jpg" % item["Hsh"]
            if not os.path.exists("image"):
                os.makedirs("image")
            urllib.urlretrieve(item["RemoteUrl"],"image/%s.jpg"%item["Hsh"])
            item.save()
            return item
        else:
            raise DropItem("Item Unclean %s" % item)




class MySQLStorePipeline(object):


    def __init__(self):
        self.conn = MySQLdb.connect(user=DBsettings["USER"], passwd=DBsettings["PASS"], db=DBsettings["NAME"], host=DBsettings["HOST"], charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()



    def process_item(self, item, spider):    
        try:
            self.cursor.execute("""INSERT INTO example_book_store (book_name, price)  
                        VALUES (%s, %s)""", 
                       (item['book_name'].encode('utf-8'), 
                        item['price'].encode('utf-8')))

            self.conn.commit()


        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item


