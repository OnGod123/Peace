from django.http import HttpRequest, HttpResponse

def my_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        submitted_data = request.POST
        # Process the submitted data
        return HttpResponse('Data received')
    return HttpResponse('Send a POST request')

