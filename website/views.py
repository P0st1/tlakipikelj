from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import Testimonial
from .forms import TestimonialForm

def home(request):
    testimonial_form = TestimonialForm()
    message_sent = False
    name = ''

    if request.method == 'POST':
        if 'message' in request.POST and 'phone' in request.POST:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            location = request.POST.get('location')
            area = request.POST.get('area')            
            message = request.POST.get('message')

            formatted_message = f"Ime in priimek: {name}\nTelefonska številka: {phone}\nLokacija: {location}\nKvadratura: {area}\nSporočilo: {message}"

            try:
                send_mail(
                    subject="Nova stranka pošilja povpraševanje",
                    message=formatted_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['pikeljtlaki@gmail.com'],
                )
                message_sent = True  
            except Exception as e:
                print(f"Napaka pri pošiljanju: {e}")

        elif 'rating' in request.POST:
            testimonial_form = TestimonialForm(request.POST)
            if testimonial_form.is_valid():
                testimonial_form.save()
                return redirect('home')

    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {
        'testimonials': testimonials,
        'testimonial_form': testimonial_form,
        'message_sent': message_sent,  
        'sent_name': name,
    })


