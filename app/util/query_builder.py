from app.models.search_models import SearchRequest


class QueryBuilder:
    @staticmethod
    def from_search_request(search_request: SearchRequest):
        def _get_facet_query(field_name, facet):
            return list(
                map(
                    lambda label: {"match": {field_name: {"query": f"{label}"}}},
                    facet,
                )
            )

        return {
            "query": {
                "bool": {
                    "must": [
                                {
                                    "multi_match": {
                                        "query": f"{search_request.search_term}",
                                        "fuzziness": "AUTO",
                                        "prefix_length": 1,
                                        "type": "bool_prefix",
                                        "fields": [
                                            "paragraph",
                                            "paragraph._2gram",
                                            "paragraph._3gram",
                                        ],
                                    },
                                }
                            ] + _get_facet_query("labels", search_request.labels)

                },
            },
            "aggs": {
                "labels": {"terms": {"field": "labels"}},
            },
            "highlight": {"fields": {"paragraph": {"number_of_fragments": 0}}},
        }
