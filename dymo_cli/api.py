from typing import Dict, Any
from dymoapi import DymoAPI

client = None  # Will be initialized later

def set_client(api_key: str):
    """Initialize the DymoAPI client with the given API key."""
    global client
    client = DymoAPI({
        "api_key": api_key
    })  # Pass API key directly in constructor

def validate_email(value: str) -> Dict[str, Any]:
    return client.is_valid_email(value).get("response", {})

def validate_phone(value: str) -> Dict[str, Any]:
    return client.is_valid_phone(value).get("response", {})

def validate_ip(value: str) -> Dict[str, Any]:
    return client.is_valid_ip(value).get("response", {})

def validate_generic(value: str) -> Dict[str, Any]:
    # Generic fallback validation using the SDK (synchronous).
    return client.is_valid_data_raw(value)