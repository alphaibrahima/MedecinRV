from django.shortcuts import render

def Home(request):
    return render(request, 'home.html', {})



def Contact(request):
    if request.method == 'POST':
        message-name
        message-email
        message
    return render(request, 'contact.html', {})

