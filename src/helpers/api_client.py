import requests


class ApiClient:
    def __init__(self, base_url, timeout=30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def _request(self, method, endpoint, **kwargs):
        kwargs.setdefault("timeout", self.timeout)
        response = self.session.request(method=method, url=self._build_url(endpoint), **kwargs)
        return response

    def get(self, endpoint, params=None, headers=None):
        return self._request("GET", endpoint, params=params, headers=headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        return self._request("POST", endpoint, data=data, json=json, headers=headers)

    def put(self, endpoint, data=None, json=None, headers=None):
        return self._request("PUT", endpoint, data=data, json=json, headers=headers)

    def patch(self, endpoint, data=None, json=None, headers=None):
        return self._request("PATCH", endpoint, data=data, json=json, headers=headers)

    def delete(self, endpoint, headers=None):
        return self._request("DELETE", endpoint, headers=headers)

    def close(self):
        self.session.close()