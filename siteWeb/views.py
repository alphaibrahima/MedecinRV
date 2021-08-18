from django.shortcuts import render
from django.core.mail import send_mail




def Home(request):
    return render(request, 'home.html', {})

def Blog(request):
    return render(request, 'blog.html', {})

# def Service(request):
#     return render(request, 'service.html', {})


def RendezVous(request):
    if request.method == "POST":
        your_name     = request.POST['your-name']
        your_phone    = request.POST['your-phone']
        your_email    = request.POST['your-email']
        your_address  = request.POST['your-address'] 
        votre_horaire = request.POST.get('votre-horaire' )
        votre_jour    = request.POST.get('votre-jour') 
        your_message  = request.POST['your-message'] 


        contenu = ("Nom : " + your_name  + " Phone : " + your_phone + " Email : " + your_email + " Addresse : " + your_address + " Horaire : " 
        + votre_horaire + " Jour : " + votre_jour + " Message : " + your_message)
        # send an mail 
        send_mail(
            'Demande de Rendez-vous',  #sujet
            contenu, #contenu du message
            your_email, #de_qui_vient_le_mail
            [ # à envoyer à
                'alphaibrahimas95@gmail.com'
            ], 
        )
        
        return render(request, 'rende-vous.html', {
            'your_name'     : your_name,
            'your_phone'    : your_phone,
            'your_email'    : your_email,
            'your_address'  : your_address,
            'votre_horaire' : votre_horaire,
            'votre_jour'    : votre_jour,
            'your_message'  : your_message
        })
    else :
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


