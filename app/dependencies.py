from injector import singleton, inject

from app.service.elasticsearch_service import ElasticsearchService
from app.service.search_service import SearchService
import configparser

import os


@inject
def configure(binder):
    config_name = os.getenv("FLASK_CONFIGURATION", "DEFAULT")
    config_parser = configparser.ConfigParser()
    config_parser.read("config.ini")
    config = config_parser[config_name]
    binder.bind(
        SearchService,
        to=ElasticsearchService(
            config["ELASTICSEARCH_CLOUD_ID"],
            config["ELASTICSEARCH_USER_ID"],
            config["ELASTICSEARCH_SECRET_ID"],
        ),
        scope=singleton,
    )
