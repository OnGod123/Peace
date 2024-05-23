
class HttpRequest:
    def __init__(self, environ):
        self.method = environ['REQUEST_METHOD'].upper()
        self.path = environ['PATH_INFO']
        self.GET = self._parse_query_string(environ['QUERY_STRING'])
        self.POST = self._parse_post_data(environ)
        self.META = environ  # Store the entire environ dictionary
        # Other initialization code...

    def _parse_query_string(self, query_string):
        # Parse the query string into a dictionary-like object
        return QueryDict(query_string)

    def _parse_post_data(self, environ):
        # Parse the POST data if the method is POST
        if self.method == 'POST':
            content_type = environ.get('CONTENT_TYPE', '')
            if content_type == 'application/x-www-form-urlencoded':
                return QueryDict(self.body)
            elif content_type.startswith('multipart/'):
                return self._parse_multipart(environ)
        return QueryDict()

    def _parse_multipart(self, environ):
        # Parse multipart form data (for file uploads)
        return QueryDict()

    @property
    def body(self):
        # Retrieve the request body
        return self._read_body()

    def _read_body(self):
        # Read the request body from the WSGI input
        input = self.META['wsgi.input']
        content_length = int(self.META.get('CONTENT_LENGTH', 0))
        return input.read(content_length)

