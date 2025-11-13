"""Auth Lambda Handler - STUB VERSION

This module handles user authentication operations including registration and login.

Endpoints:
    POST /auth/register - Register a new user
    POST /auth/login    - Authenticate existing user

Event Structure:
    {
        'httpMethod': 'POST',
        'path': '/auth/register' or '/auth/login',
        'body': '{"email": "user@example.com", "password": "pass123"}'
    }
"""

import json
from typing import Any


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Handle authentication requests (register/login).

    This is the main entry point for the Auth Lambda function. Currently returns
    501 Not Implemented as this is a stub version.

    Args:
        event: API Gateway event containing:
            - httpMethod (str): HTTP method (POST)
            - path (str): Request path (/auth/register or /auth/login)
            - body (str): JSON string with email/password
            - headers (dict): Request headers
        context: Lambda context object with runtime information

    Returns:
        API Gateway response dict containing:
            - statusCode (int): HTTP status code (501 for not implemented)
            - headers (dict): Response headers including CORS
            - body (str): JSON string with response message
    """

    # Log the incoming event (you'll see this in SAM logs)
    print(f"Received event: {json.dumps(event)}")

    http_method = event['httpMethod']
    path = event['path']

    return {
        'statusCode': 501,  # 501 = Not Implemented
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Auth endpoint not implemented yet',
            'received_path': path,
            'received_method': http_method
        })
    }
