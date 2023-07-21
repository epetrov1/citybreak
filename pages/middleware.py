from django.http import HttpResponse
from django.shortcuts import render
from django.urls import resolve

class CookiePopupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define a list of URL paths that don't require cookie consent
        exempt_paths = ['cookie_description']  # Add the URL path of the exempted page here

        # Get the current URL path
        url_name = resolve(request.path_info).url_name
        # Check if the current URL path is exempted
        if url_name not in exempt_paths and not request.COOKIES.get('accept_cookies_'):
            # If not exempted and cookies not accepted, render the cookie consent template
            response = render(request, 'pages/cookie_consent.html')
        else:
            # If exempted or cookies accepted, proceed with the original response
            response = self.get_response(request)
        if request.COOKIES.get('decline_cookies_'):
            response = self.get_response(request)
        return response
