from django.shortcuts import render

# Vista per la Privacy Policy
def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

# Vista per la Cookie Policy
def cookie_policy(request):
    return render(request, 'pages/cookie_policy.html')