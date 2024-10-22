# Restman: A Python Command-Line Tool for RESTful API Testing

## Features Overview:
1. **Command-Line Interface (CLI)** with options for HTTP methods and useful flags.
2. **Subcommands** for different HTTP methods like GET, POST, PUT, DELETE.
3. **Best practices** for specifying HTTP headers, SSL certificates, etc.
4. Encapsulated **core functionalities as a Python library** for future extension (e.g., adding a web service layer or GUI).

### Dependencies
To get started, you'll need a few dependencies. Here's how to install them:

```bash
pip install requests argparse
```

## Draft Project Structure

```bash
restman/
│
├── restman.py                # Main CLI interface
├── core/
│   ├── __init__.py           # Init file for the core module
│   ├── http_client.py        # Core HTTP request logic
│   └── utils.py              # Utility functions (e.g., parsing headers)
└── README.md                 # Project documentation
```

---

## `restman.py`: The Command-Line Interface

The CLI is the main entry point for the application. It uses `argparse` to handle user input and subcommands for different HTTP methods.

```python
import argparse
from core.http_client import HttpClient

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(
        description="Restman: A Command-Line Tool for Testing RESTful Endpoints"
    )

    # Global arguments (common for all subcommands)
    parser.add_argument(
        '-H', '--header', action='append', help='Specify HTTP headers (key:value format)', required=False
    )
    parser.add_argument(
        '--ssl', help='Path to SSL certificate', required=False
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Enable verbose output'
    )

    # Subparsers for HTTP methods
    subparsers = parser.add_subparsers(dest='method', help="HTTP method to execute")

    # GET request subcommand
    get_parser = subparsers.add_parser('get', help="Perform a GET request")
    get_parser.add_argument('url', help="The URL for the GET request")
    
    # POST request subcommand
    post_parser = subparsers.add_parser('post', help="Perform a POST request")
    post_parser.add_argument('url', help="The URL for the POST request")
    post_parser.add_argument('-d', '--data', help="Data to send with the POST request", required=True)

    # PUT request subcommand
    put_parser = subparsers.add_parser('put', help="Perform a PUT request")
    put_parser.add_argument('url', help="The URL for the PUT request")
    put_parser.add_argument('-d', '--data', help="Data to send with the PUT request", required=True)

    # DELETE request subcommand
    delete_parser = subparsers.add_parser('delete', help="Perform a DELETE request")
    delete_parser.add_argument('url', help="The URL for the DELETE request")

    args = parser.parse_args()

    # Initialize the HTTP client
    client = HttpClient()

    # Handle different methods
    if args.method == 'get':
        client.get(args.url, headers=args.header, ssl_cert=args.ssl, verbose=args.verbose)
    elif args.method == 'post':
        client.post(args.url, data=args.data, headers=args.header, ssl_cert=args.ssl, verbose=args.verbose)
    elif args.method == 'put':
        client.put(args.url, data=args.data, headers=args.header, ssl_cert=args.ssl, verbose=args.verbose)
    elif args.method == 'delete':
        client.delete(args.url, headers=args.header, ssl_cert=args.ssl, verbose=args.verbose)

if __name__ == "__main__":
    main()
```

---

## `http_client.py`: Core HTTP Client Logic

This file contains the logic for performing HTTP requests using the `requests` library. Each HTTP method has a corresponding function in this class.

```python
import requests
from core.utils import parse_headers

class HttpClient:
    def __init__(self):
        pass

    def get(self, url, headers=None, ssl_cert=None, verbose=False):
        headers = parse_headers(headers)
        try:
            response = requests.get(url, headers=headers, verify=ssl_cert)
            self._handle_response(response, verbose)
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request: {e}")

    def post(self, url, data, headers=None, ssl_cert=None, verbose=False):
        headers = parse_headers(headers)
        try:
            response = requests.post(url, data=data, headers=headers, verify=ssl_cert)
            self._handle_response(response, verbose)
        except requests.exceptions.RequestException as e:
            print(f"Error during POST request: {e}")

    def put(self, url, data, headers=None, ssl_cert=None, verbose=False):
        headers = parse_headers(headers)
        try:
            response = requests.put(url, data=data, headers=headers, verify=ssl_cert)
            self._handle_response(response, verbose)
        except requests.exceptions.RequestException as e:
            print(f"Error during PUT request: {e}")

    def delete(self, url, headers=None, ssl_cert=None, verbose=False):
        headers = parse_headers(headers)
        try:
            response = requests.delete(url, headers=headers, verify=ssl_cert)
            self._handle_response(response, verbose)
        except requests.exceptions.RequestException as e:
            print(f"Error during DELETE request: {e}")

    def _handle_response(self, response, verbose):
        if verbose:
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")
```

---

## `utils.py`: Helper Functions

This file contains utility functions for the application, such as parsing headers provided by the user in the command line.

```python
def parse_headers(header_list):
    """
    Parse the header list in 'key:value' format into a dictionary.
    """
    if header_list is None:
        return None

    headers = {}
    for header in header_list:
        key, value = header.split(":", 1)
        headers[key.strip()] = value.strip()

    return headers
```

---

## How to Run the Application

### Example Usage:

1. **Performing a GET request**:
   ```bash
   python restman.py get https://api.example.com/resource -H "Authorization: Bearer token" -v
   ```

2. **Performing a POST request**:
   ```bash
   python restman.py post https://api.example.com/resource -d '{"key":"value"}' -H "Content-Type: application/json"
   ```

3. **Performing a PUT request**:
   ```bash
   python restman.py put https://api.example.com/resource/1 -d '{"updated_key":"new_value"}' -H "Content-Type: application/json"
   ```

4. **Performing a DELETE request**:
   ```bash
   python restman.py delete https://api.example.com/resource/1 -H "Authorization: Bearer token"
   ```

### SSL Certificate Option:

To provide an SSL certificate:

```bash
python restman.py get https://secure-api.example.com --ssl /path/to/certificate.pem
```

---

## Future Considerations

- **Library encapsulation**: The core HTTP request logic is placed in a class (`HttpClient`), which can easily be extended in the future to support a web service layer or a web GUI.
- **Subcommands for more HTTP methods**: The current implementation supports GET, POST, PUT, and DELETE, but can easily be extended to other methods like PATCH, HEAD, etc.
- **Extensibility**: This structure is designed with future-proofing in mind, allowing for adding new features like authentication, multipart form handling, or integrating with external APIs.
