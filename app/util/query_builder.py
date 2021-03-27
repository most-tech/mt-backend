from app.models.search_models import SearchRequest


class QueryBuilder:
    @staticmethod
    def from_search_request(search_request: SearchRequest):
        def _get_filters(search_request):
            filters = [
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
            ]
            if search_request.labels != "":
                for keyword in search_request.labels.split(","):
                    if keyword != "":
                        filters.append(
                            {"match": {"labels": {"query": f"{keyword.strip()}"}}}
                        )
            return filters

        # from_search_request
        return {
            "query": {
                "bool": {"must": _get_filters(search_request=search_request)},
            },
            "aggs": {
                "facets": {"terms": {"field": "labels", "exclude": [""]}},
            },
            "highlight": {"fields": {"paragraph": {"number_of_fragments": 0}}},
        }
