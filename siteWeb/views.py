from django.shortcuts import render

def Home(request):
    return render(request, 'home.html', {})



def Contact(request):
    if request.method == "POST":
        message_name    = request.POST['message-name']
        message_email   = request.POST['message-email']
        message         = request.POST['message'] 
        return render(request, 'contact.html', {'message_name' : message_name})
    else :
        return render(request, 'contact.html', {})


