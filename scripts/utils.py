# utils.py

import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_config():
    """Load configuration from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r') as config_file:
        return json.load(config_file)

def load_secret(key):
    """Load a secret from the secrets.json file."""
    config = get_config()
    secret_path = os.path.join(os.path.dirname(__file__), 'secrets.json')
    with open(secret_path, 'r') as secret_file:
        secrets = json.load(secret_file)
    return secrets.get(key)

def validate_token(token):
    """Validate a JSON Web Token."""
    import jwt
    try:
        jwt.decode(token, verify=True)
    except jwt.ExpiredSignatureError:
        logging.error("Token has expired.")
        return False
    except jwt.InvalidTokenError:
        logging.error("Token is invalid.")
        return False
    return True