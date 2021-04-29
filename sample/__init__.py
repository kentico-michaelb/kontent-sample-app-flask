from flask import Flask
import config
from kontent_delivery.client import DeliveryClient
from sample.resolvers.custom_item_resolver import CustomItemResolver
from sample.resolvers.custom_link_resolver import CustomLinkResolver

app = Flask(__name__)

client = DeliveryClient(config.project_id, options=config.delivery_options)
client.custom_item_resolver = CustomItemResolver()
client.custom_link_resolver = CustomLinkResolver()

import sample.home.views
import sample.articles.views