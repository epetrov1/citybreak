import stripe
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail


stripe.api_key = settings.STRIPE_SECRET_KEY

def success_view(request):
    return render(request, 'ticket/success.html')

def failed_view(request):
    return render(request, 'ticket/failed.html')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN =  "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            invoice_creation={"enabled": True},
            line_items=[
                {
                    'price': 'price_1NSHsiH0PxqPRdQrFDk55wsA',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/ticket/success/',
            cancel_url=YOUR_DOMAIN + '/ticket/cancel/',
        )
        return HttpResponseRedirect(checkout_session.url) 


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOKS_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
    # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        session = stripe.checkout.Session.retrieve(
        event['data']['object']['id'],
        expand=['line_items'],
        )
        customer_email = session['customer_details']['email']
        customer_name  = session['customer_details']['name']
        send_mail(
            subject = 'Tattoo city break',
            message = f'Hello {customer_name}, you buy ticket.',
            recipient_list=[customer_email, 'tattocitybrek@mail.com'],
            from_email = 'my@mail.com'
        )


    # Passed signature verification
    return HttpResponse(status=200)