from typing import Optional

from .. import SearchEntry, SearchResult
from ..api_client import APIClient
from ..controller import Controller

# The API docs and the actual API disagree on the key names, accept both
_ENTRY_KEYS = {
    "clientID": "client_id",
    "installationID": "installation_id",
    "organizationID": "organization_id",
    "metaMatches": "meta_matches",
    "allMetadata": "metadata",
}
_ENTRY_FIELDS = {"type", "id", "name", "description", "notes", "created", "updated", "client_id", "installation_id",
                 "organization_id", "meta_matches", "metadata"}


class SearchController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def search(self, query: str = "*", types: Optional[list[str]] = None, limit: Optional[int] = None,
               offset: Optional[int] = None, metadata: Optional[dict[str, str]] = None):
        params = {"q": query}
        if types:
            params["types"] = ",".join(types)
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if metadata:
            for k, v in metadata.items():
                params["metadata.{0}".format(k)] = v

        path = "api/v3beta/search{0}".format(self.format_query_string(params))
        resp = self._api_client.request("GET", path)
        results = []
        for x in resp.get("results") or []:
            entry = {}
            for k, v in x.items():
                k = _ENTRY_KEYS.get(k, k)
                if k in _ENTRY_FIELDS:
                    entry[k] = v
            results.append(SearchEntry(**entry))
        return SearchResult(resp.get("total"), resp.get("limit"), resp.get("offset"), results)
