"""Users Lambda Handler - STUB VERSION

This module handles user profile operations and account management.

Endpoints:
    GET /users/me - Get current authenticated user's profile

Future Implementation:
    - Extract and validate JWT token from Authorization header
    - Decode token to extract user_id
    - Query UsersTable in DynamoDB
    - Return user profile (excluding sensitive data like password hash)
    - Support profile updates (PUT /users/me)
"""

import json
from typing import Any


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Handle user profile operations.

    This is the main entry point for the Users Lambda function. Currently returns
    501 Not Implemented as this is a stub version.

    Args:
        event: API Gateway event containing:
            - httpMethod (str): HTTP method (GET)
            - path (str): Request path (/users/me)
            - headers (dict): Request headers including Authorization with JWT
        context: Lambda context object with runtime information

    Returns:
        API Gateway response dict containing:
            - statusCode (int): HTTP status code (501 for not implemented)
            - headers (dict): Response headers including CORS
            - body (str): JSON string with response message and auth status
    """

    print(f"Received event: {json.dumps(event)}")

    http_method = event['httpMethod']
    path = event['path']

    # Check if Authorization header exists (even though we're not using it yet)
    headers = event.get('headers', {})
    auth_header = headers.get('Authorization') or headers.get('authorization')

    return {
        'statusCode': 501,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Users endpoint not implemented yet',
            'received_path': path,
            'received_method': http_method,
            'has_auth_header': auth_header is not None,
            'note': 'Will return user profile based on JWT token'
        })
    }
