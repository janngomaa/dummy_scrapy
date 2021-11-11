BOT_NAME = 'tutorial'

import keyring

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "tutorial.pipelines.SaveQuotesPipeline": 300,
}

DATABASE = {
    "drivername": "postgresql",
    "host": keyring.get_password('postgresql', 'host'),
    "port": keyring.get_password('postgresql', 'port'),
    "database": keyring.get_password('postgresql', 'database'),
    "username": keyring.get_password('postgresql', 'username'),
    "password": keyring.get_password('postgresql', 'password')
    
}