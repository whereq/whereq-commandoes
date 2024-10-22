import json

def parse_json_string(json_string):
    """Parse a JSON string."""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")
