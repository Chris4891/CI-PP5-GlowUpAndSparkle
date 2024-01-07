from django.shortcuts import render, redirect
from store.forms import SubscriberForm
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.http import require_POST
def Newsletter(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.save()

            context = {'email': subscriber.email}
            email_content = render_to_string('emailtemplate.html', context)

            email_subject = 'Thank you for Subscribing'
            recipient_list = [subscriber.email]
            from_email = 'shahwaizmughal02@gmail.com'

            send_mail(
                email_subject,
                '',
                from_email,
                recipient_list,
                html_message=email_content,
                fail_silently=False
            )

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
