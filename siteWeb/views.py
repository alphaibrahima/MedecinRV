from django.shortcuts import render
from django.core.mail import send_mail
def Home(request):
    return render(request, 'home.html', {})



def Contact(request):
    if request.method == "POST":
        message_name    = request.POST['message-name']
        message_email   = request.POST['message-email']
        message         = request.POST['message'] 

        # send an mail 
        send_mail(
            'Rendez-vous' + message_name, #sujet
            message, #contenu du message
            message_email, #de_qui_vient_le_mail
            [ # à envoyer le mail
                'alphaibrahimas95@gmail.com'
            ], 
        )
        return render(request, 'contact.html', {'message_name' : message_name})
    else :
        return render(request, 'contact.html', {})


