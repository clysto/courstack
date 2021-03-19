from django.http import JsonResponse
from rest_framework import status


def not_found(request, *args, **kwargs):
    """
    Generic 404 error handler.
    """
    data = {"error": "Not Found (404)"}
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)


def forbidden(request, exception, *args, **kwargs):
    """
    Generic 403 error handler.
    """
    data = {"error": "Forbidden (403)"}
    return JsonResponse(data, status=status.HTTP_403_FORBIDDEN)
