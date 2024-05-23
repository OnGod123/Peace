from django.http import HttpRequest, HttpResponse
import json

def post_info_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        # Accessing POST data
        post_data = request.POST

        # Extracting metadata from the request
        request_info = {
            'REQUEST_METHOD': request.method,
            'PATH_INFO': request.path,
            'QUERY_STRING': request.META.get('QUERY_STRING', ''),
            'CONTENT_TYPE': request.META.get('CONTENT_TYPE', ''),
            'CONTENT_LENGTH': request.META.get('CONTENT_LENGTH', ''),
            'HTTP_HOST': request.META.get('HTTP_HOST', ''),
            'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT', ''),
            'REMOTE_ADDR': request.META.get('REMOTE_ADDR', ''),
            'SERVER_NAME': request.META.get('SERVER_NAME', ''),
            'SERVER_PORT': request.META.get('SERVER_PORT', ''),
            'POST_DATA': post_data.dict(),  # Converting QueryDict to a regular dict for easier readability
        }

        # Converting the dictionary to a JSON string for better readability
        request_info_json = json.dumps(request_info, indent=4)

        # Returning the request information as an HTTP response
        return HttpResponse(f'<pre>{request_info_json}</pre>', content_type='application/json')

    return HttpResponse('This view only accepts POST requests.')

