from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        formatted_message = f"Ime in priimek: {name}\nTelefonska številka: {phone}\nZadeva: {subject}\nSporočilo: {message}"
        print(formatted_message)
        try:
            send_mail(
                subject="Nova stranka pošilja povpraševanje",
                message=formatted_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['tvojemail@domena.si'],  
            )
            messages.success(request, 'Vaš obrazec je bil uspešno poslan.')
            return render(request, 'success_message.html', {'name': name})
        except Exception as e:
            print(f"Napaka pri pošiljanju: {e}")
            messages.error(request, 'Prišlo je do napake pri pošiljanju.')
    
    return render(request, 'home.html')
