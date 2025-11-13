"""Bookings Lambda Handler - STUB VERSION

This module handles flight booking operations including creating, listing, and
canceling bookings.

Endpoints:
    POST /bookings              - Create a new booking
    GET /bookings               - List user's bookings
    DELETE /bookings/{id}       - Cancel a booking

Future Implementation:
    - Validate JWT token from Authorization header
    - Check flight availability before booking
    - Update flight seat count in FlightsTable
    - Store booking in BookingsTable
    - Support pagination for listing bookings
"""

import json
from typing import Any


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Handle booking operations (create/list/cancel).

    This is the main entry point for the Bookings Lambda function. Currently returns
    501 Not Implemented as this is a stub version.

    Args:
        event: API Gateway event containing:
            - httpMethod (str): HTTP method (POST, GET, or DELETE)
            - path (str): Request path (/bookings or /bookings/{booking_id})
            - body (str): JSON string with booking details (for POST)
            - headers (dict): Request headers (including Authorization)
            - pathParameters (dict): URL parameters (booking_id for DELETE)
        context: Lambda context object with runtime information

    Returns:
        API Gateway response dict containing:
            - statusCode (int): HTTP status code (501 for not implemented)
            - headers (dict): Response headers including CORS
            - body (str): JSON string with response message
    """

    print(f"Received event: {json.dumps(event)}")

    http_method = event['httpMethod']
    path = event['path']

    return {
        'statusCode': 501,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Bookings endpoint not implemented yet',
            'received_path': path,
            'received_method': http_method,
            'note': 'Will handle: create booking, list bookings, cancel booking'
        })
    }
