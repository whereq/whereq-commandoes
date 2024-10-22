import argparse
from restman import Restman

def main():
    parser = argparse.ArgumentParser(
        description="Restman - Command-line RESTful API testing tool"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # GET request subcommand
    get_parser = subparsers.add_parser('GET', help="Send a GET request")
    get_parser.add_argument('url', type=str, help="The URL to send the GET request to")
    get_parser.add_argument('--headers', type=str, help="HTTP headers as a JSON string")
    get_parser.add_argument('--cert', type=str, help="Path to SSL certificate")
    get_parser.add_argument('--timeout', type=int, help="Request timeout in seconds")

    # POST request subcommand
    post_parser = subparsers.add_parser('POST', help="Send a POST request")
    post_parser.add_argument('url', type=str, help="The URL to send the POST request to")
    post_parser.add_argument('--headers', type=str, help="HTTP headers as a JSON string")
    post_parser.add_argument('--data', type=str, help="POST data as a JSON string")
    post_parser.add_argument('--cert', type=str, help="Path to SSL certificate")
    post_parser.add_argument('--timeout', type=int, help="Request timeout in seconds")

    # Other subcommands (PUT, DELETE, etc.) can be similarly defined

    args = parser.parse_args()

    restman = Restman()

    # Based on the command, invoke the corresponding action
    if args.command == 'GET':
        response = restman.get(args.url, headers=args.headers, cert=args.cert, timeout=args.timeout)
        print(response.text)
    elif args.command == 'POST':
        response = restman.post(args.url, headers=args.headers, data=args.data, cert=args.cert, timeout=args.timeout)
        print(response.text)
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()

if __name__ == '__main__':
    main()
