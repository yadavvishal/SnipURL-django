from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import URL

# View function to handle URL shortening
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']  # Get the original URL from POST data
        url, created = URL.objects.get_or_create(original_url=original_url)  # Get or create URL the object
        short_url = request.build_absolute_uri(url.short_code)  # Build the short URL using absolute URI
        return render(request, 'index.html', {'short_url': short_url})  # Render template with short URL
    return render(request, 'index.html')  # Render default template for GET requests

# View function to redirect to original URL
def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)  # Get the URL object by short code or return 404
    return redirect(url.original_url)  # Redirect to the original URL associated with the short code
