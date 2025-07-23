#!/usr/bin/env python3
"""
Generate JWT token for GitHub App authentication
"""

import jwt
import time
import sys
import os

def generate_jwt(app_id, private_key_path):
    """Generate JWT token for GitHub App"""
    with open(private_key_path, 'r') as f:
        private_key = f.read()
    
    payload = {
        'iat': int(time.time()),
        'exp': int(time.time()) + 600,  # 10 minutes
        'iss': app_id
    }
    
    token = jwt.encode(payload, private_key, algorithm='RS256')
    return token

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_jwt.py <app_id> <private_key_path>")
        sys.exit(1)
    
    app_id = sys.argv[1]
    private_key_path = sys.argv[2]
    
    try:
        token = generate_jwt(app_id, private_key_path)
        print(token)
    except Exception as e:
        print(f"Error generating JWT: {e}", file=sys.stderr)
        sys.exit(1) 