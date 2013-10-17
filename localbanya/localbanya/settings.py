
BOT_NAME = 'LocalBaniaBot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['localbanya.spiders']
NEWSPIDER_MODULE = 'localbanya.spiders'
DEFAULT_ITEM_CLASS = 'localbanya.items.CartItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES ={
        'localbanya.pipelines.CleansePipeline':300,
        'localbanya.pipelines.JsonWriterPipeline':200,
        'localbanya.pipelines.DjangoWriterPipeline':100,
        #        'localbanya.pipelines.MySQLStorePipeline':100,
        }
DBsettings = {
        "USER" : "",
        "PASS" : "",
        "NAME" : "",
        "HOST" : "",
        "PORT" : ""
        }



import sys
sys.path.append('/home/xadmin/Workspaces/Aptana/display')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'display.settings'

execfile('/home/xadmin/virtualenvs/displaydjango/django/bin/activate_this.py',
{'__file__': '/home/xadmin/virtualenvs/displaydjango/django/bin/activate_this.py'})
