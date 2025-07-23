#!/usr/bin/env python3
"""
Extract access token from GitHub API response
"""

import sys
import json

def get_access_token(response_json):
    """Extract access token from GitHub API response"""
    try:
        data = json.loads(response_json)
        if 'token' in data:
            return data['token']
        else:
            print(f'Error: No token in response', file=sys.stderr)
            print(f'Response: {data}', file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f'Error parsing response: {e}', file=sys.stderr)
        print(f'Raw response: {response_json}', file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 get_access_token.py <json_response>")
        sys.exit(1)
    
    response_json = sys.argv[1]
    token = get_access_token(response_json)
    print(token) 