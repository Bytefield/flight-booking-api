"""Flights Lambda Handler

This module handles flight search and listing operations. It interacts with
DynamoDB to retrieve flight information.

Endpoints:
    GET /flights              - List all available flights
    GET /flights/{flight_id}  - Get details of a specific flight

DynamoDB Integration:
    Uses the FlightsTable to query flight data. Table structure:
    - Primary Key: flight_id (String)
    - GSI: origin-index for searching by origin airport
"""

from typing import Any
import boto3
import json
import os

# Environment variables
FLIGHTS_TABLE: str = os.environ['FLIGHTS_TABLE']

# DynamoDB resources (types from boto3.resources.base)
dynamodb: Any = boto3.resource('dynamodb')  # DynamoDBServiceResource
table: Any = dynamodb.Table(FLIGHTS_TABLE)  # Table


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """Route flight requests to appropriate handler functions.

    This is the main entry point for the Flights Lambda function. Routes requests
    based on HTTP method and path to the appropriate handler.

    Args:
        event: API Gateway event containing:
            - httpMethod (str): HTTP method (GET)
            - path (str): Request path (/flights or /flights/{flight_id})
            - pathParameters (dict): URL parameters (flight_id if present)
        context: Lambda context object with runtime information

    Returns:
        API Gateway response dict from list_flights or get_flight handlers,
        or 404 error if route not found.
    """
    http_method = event['httpMethod']
    path = event['path']

    if http_method == 'GET':
        if path == '/flights':
            return list_flights(event) or {'statusCode': 204, 'body': 'No flights found'}
        elif '/flights/' in path:
            return get_flight(event) or {'statusCode': 204, 'body': 'Flight not found'}

    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'Not found'})
    }


def list_flights(event: dict[str, Any]) -> dict[str, Any]:
    """List all available flights from the database.

    Performs a full table scan of FlightsTable to retrieve all flights.
    Note: In production, consider using pagination for large datasets.

    Args:
        event: API Gateway event (not currently used, reserved for future filtering)

    Returns:
        API Gateway response dict containing:
            - statusCode (int): 200 on success, 500 on error
            - headers (dict): Response headers including CORS
            - body (str): JSON string with flight list:
                {
                    'success': True,
                    'data': [
                        {
                            'flight_id': 'FL123',
                            'origin': 'MAD',
                            'destination': 'BCN',
                            'price': 89.99,
                            ...
                        }
                    ]
                }
    """
    try:
        response = table.scan()

        items: list[dict[str, Any]] = response.get('Items', [])

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'data': items
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }


def get_flight(event: dict[str, Any]) -> dict[str, Any]:
    """Get details of a specific flight by ID.

    Retrieves a single flight from FlightsTable using the flight_id from URL.

    Args:
        event: API Gateway event containing:
            - pathParameters (dict): Must include 'flight_id' key

    Returns:
        API Gateway response dict containing:
            - statusCode (int): 200 on success, 400 if missing ID,
                               404 if not found, 500 on error
            - headers (dict): Response headers including CORS
            - body (str): JSON string with flight details:
                {
                    'success': True,
                    'data': {
                        'flight_id': 'FL123',
                        'origin': 'MAD',
                        'destination': 'BCN',
                        'price': 89.99,
                        'departure_time': '2024-11-15T10:00:00Z',
                        'arrival_time': '2024-11-15T11:30:00Z',
                        'available_seats': 45
                    }
                }
    """
    path_params: dict[str, str] = event.get('pathParameters', {})
    flight_id: str = path_params.get('flight_id', '')

    if not flight_id:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing flight_id'})
        }

    try:
        response = table.get_item(Key={'flight_id': flight_id})  # Must match the primary_key

        # response structure:
        # {
        #     'Item': {...}     # The item or None if not found
        # }

        item: dict = response.get('Item')

        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Flight not found'})
            }

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'success': True,
                'data': item
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
