from scrapy.item import Item, Field
from scrapy.contrib_exp.djangoitem import DjangoItem
from display import RawPublicdb

class CartItemOld(Item):
    name = Field()
    brand = Field()
    mrp = Field()
    qty = Field()
    remoteimg = Field()
    img = Field()
    variety = Field()
    hsh = Field()
    category = Field()

    

class CartItem(DjangoItem):
    django_model = RawPublicdb
