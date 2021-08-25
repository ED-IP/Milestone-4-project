from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, ContactForm
from .forms import UserProfileForm, UserContactForm

from checkout.models import Order


# Create your views here.

@login_required
def profile(request):
    """display User profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, ' Update failed. Please review the new data for your profile.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order {order_number}. '
        'An email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def contact_form(request):
    current_user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserContactForm(request.POST, instance=current_user)
        form_data = {
            'user': request.POST[current_user],
            'user_email': request.POST['user_email'],
            'user_phone_number': request.POST['user_phone_number'],
            'description': request.POST['description'],
        }
        form = UserContactForm(form_data)
        if form.is_valid():
            # form.save(commit=False)
            # pepito2 = form.save(commit=False)
            # print(pepito2)
            # form.user = current_user
            form.save()
            # print(pepito)
            messages.success(request, 'Message successfuly sent')
        else:
            messages.error(request, 'Message failed. Please check the fields have the right data')
    else:
        form = UserContactForm(instance=current_user)

    template = 'profiles/contact_form.html'

    context = {'form': form}
    return render(request, template, context)
