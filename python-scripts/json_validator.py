# python-scripts/json_validator.py

import json
import sys

def validate_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
        return False

if __name__ == "__main__":
    json_str = sys.stdin.read()
    is_valid = validate_json(json_str)
    print(json.dumps({'is_valid': is_valid}))
