from django.shortcuts import redirect

# check if authenticated else sent to login page
def auth_middleware(get_response):
    # one time config

    def middleware(request):
        # print(request.session.get('email'))
        # print(request.META['PATH_INFO'])

        returnUrl = request.META['PATH_INFO']
        if not request.session.get('email'):
            return redirect(f'/accounts/login?return_url={returnUrl}')

        # before
        response = get_response(request)
        # after
        return response

    return middleware