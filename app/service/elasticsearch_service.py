# pylint: disable=E1101,W0613
# This class is just a prototype. Disabled unused argument rule
from abc import ABC
from elasticsearch import Elasticsearch
from google.cloud import secretmanager
from app.models.search_models import SearchQuery
from app.service.search_service import SearchService


class ElasticsearchService(ABC, SearchService):
    def __init__(self, cloud_id: str, user_id: str, secret_id: str, index: str):
        client = secretmanager.SecretManagerServiceClient()
        response = client.access_secret_version(name=secret_id)
        password = response.payload.data.decode("UTF-8")
        self.elasticsearch = Elasticsearch(
            cloud_id=cloud_id,
            http_auth=(user_id, password),
        )
        self.index = index

    def execute_search_query(self, search_query: SearchQuery):
        result = self.elasticsearch.search(
            index="most-tech-dev",
            body={
                "query": {
                    "multi_match": {
                        "query": f"{search_query.keystroke}",
                        "fuzziness": "AUTO",
                        "prefix_length": 1,
                        "type": "bool_prefix",
                        "fields": ["keystroke", "keystroke._2gram", "keystroke._3gram"],
                    }
                }
            },
        )["hits"]["hits"]
        return [patern["_source"] for patern in result]
