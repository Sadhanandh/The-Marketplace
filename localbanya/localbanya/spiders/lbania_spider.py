from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from localbanya.items import CartItem
import json
import urlparse
import copy
import hashlib
import HTMLParser


class LBanyaSpider(BaseSpider):
    name = "localbanya"
    allowed_domains = ["localbanya.com"]
    baseurl = "http://www.localbanya.com/"
    start_urls= [
            "http://www.localbanya.com/products/Bottles,-Cans---Packets/Chips---Wafers-/06/03",
            ]


    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       urls = hxs.select('//ul[@id="navigation"]//ul/li/a/@href').extract()
       for i in urls:
           yield Request(urlparse.urljoin(self.baseurl, i[1:]), callback=self.parse_url)

    def parse_url(self,response):
        filename = "Local.txt"
        f = open(filename,"wb")
        hxs = HtmlXPathSelector(response)
        divs = hxs.select('//div[@class="shelf_in"]')
        items = []
        for div in divs:
            item = CartItem()
            img = div.select('div/a/img/@src').extract()
            fullpath  = [urlparse.urljoin(response.url, img[0])][0]
            brand = div.select('div[@class="two-blocks"]/h5[1]/a/text()').extract()[0]
            name = div.select('div[@class="two-blocks"]/h5[2]/a/text()').extract()[0]

            brand = HTMLParser.HTMLParser().unescape(brand)
            name = HTMLParser.HTMLParser().unescape(name)
            opts = div.select('div[@class="add2c"]//select/option')
            sub = []
            item["Desc"] = name
            item["Name"] = brand
            item["RemoteUrl"] = fullpath
            zitems = []
            for i,opt in enumerate(opts):
                l_mrp = opt.select('@mrp').extract()[0]
                l_qty = opt.select('text()').extract()[0]
                l_mrp = HTMLParser.HTMLParser().unescape(l_mrp)
                l_qty = HTMLParser.HTMLParser().unescape(l_qty)
                item["Mrp"] = l_mrp
                item["Qty"] = l_qty
                if i==0:
                    mrp = l_mrp
                    qty = l_qty
                else:
                    zitem = copy.deepcopy(item)
                    zitem["Mrp"] = l_mrp
                    zitem["Qty"] = l_qty
                    zitems.append(zitem)
                dic = {}
                dic["Mrp"] = l_mrp
                dic["Qty"] = l_qty
                sub.append(dic)
            var = i+1
            item["Mrp"] = mrp
            item["Qty"] = qty
            item["Variety"]=var
            item["Hsh"] = hsh(item)
            item["Category"]=response.url.split("/")[-3]
            items.append(item)
            for zitem in zitems:
                zitem["Variety"]=var
                zitem["Hsh"] = hsh(zitem)
                zitem["Category"]=response.url.split("/")[-3]
                items.append(zitem)
            print img,brand,name,str(sub),mrp,qty
            f.write("Fullpath: %s\n"%fullpath)
            f.write("Image: %s\nBrand: %s\nName: %s\n"%(img,brand,name))
            f.write("MRP: %s\nQTY: %s\n"%(mrp,qty))
            f.write("Variety: %s\n"%str(var))
            f.write("All:  %s \n\n"% json.dumps(sub))
        f.close()
        return items





def hsh(obj):
    VERSION = "1.0"
    txt = obj["Name"]+obj["Desc"]+obj["Qty"]+VERSION
    return hashlib.sha1(json.dumps(txt)).hexdigest()
