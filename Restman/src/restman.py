import requests
import json

class Restman:
    def get(self, url, headers=None, cert=None, timeout=None):
        """Send a GET request."""
        try:
            headers = self._parse_headers(headers)
            response = requests.get(url, headers=headers, cert=cert, timeout=timeout)
            return response
        except requests.RequestException as e:
            raise Exception(f"GET request failed: {str(e)}")

    def post(self, url, headers=None, data=None, cert=None, timeout=None):
        """Send a POST request."""
        try:
            headers = self._parse_headers(headers)
            data = json.loads(data) if data else None
            response = requests.post(url, headers=headers, json=data, cert=cert, timeout=timeout)
            return response
        except requests.RequestException as e:
            raise Exception(f"POST request failed: {str(e)}")

    def _parse_headers(self, headers):
        """Parse headers from JSON string."""
        if headers:
            try:
                return json.loads(headers)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON for headers")
        return None
