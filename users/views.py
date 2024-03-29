
from django.core.mail import EmailMultiAlternatives
from users.admin import MyUserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from users.forms import LoginForm, UploadProfileImage
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.loader import get_template
from users.forms import ContactForm, EnContactForm, RoNewsletterForm, EnNewsletterForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from users.models import ContactApp, EnContactApp
from django import forms
from django.utils.translation import gettext_lazy as _


def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user, backend=settings.DJANGO_AUTH_BACKEND)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })


def handle_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile(request):
    remote_address = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        user_profile = request.user.profile
        form = UploadProfileImage(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return HttpResponseRedirect(reverse('users:profile'))

    else:
        form = UploadProfileImage()

    return render(request, 'users/profile.html', {
        'form': form,
        'ip_address': remote_address
    })


@login_required
def en_profile(request):
    remote_address = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        user_profile = request.user.profile
        form = UploadProfileImage(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return HttpResponseRedirect(reverse('users:en_profile'))

    else:
        form = UploadProfileImage()

    return render(request, 'users/en_profile.html', {
        'form': form,
        'ip_address': remote_address
    })


@login_required
def profile_email(request):
    if settings.IS_PRODUCTION:
        avatar_path = '{MEDIA_ROOT}/{PROFILE_IMAGE}'.format(
            MEDIA_ROOT=settings.MEDIA_ROOT,
            PROFILE_IMAGE=request.user.profile.avatar)

    else:
        avatar_path = '{BASE_DIR}/{MEDIA_ROOT}/{PROFILE_IMAGE}'.format(
            BASE_DIR=settings.BASE_DIR,
            MEDIA_ROOT=settings.MEDIA_ROOT,
            PROFILE_IMAGE=request.user.profile.avatar)

    remote_address = request.META.get('REMOTE_ADDR')
    email_template = get_template('users/email.html')
    email_content = email_template.render(
        {
            'your_profile': request.user.profile,
            'your_email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'ip_address': remote_address
        })

    mail = EmailMultiAlternatives(
        'Your profile data request',
        email_content,
        settings.EMAIL_HOST_USER,
        [request.user.email])

    mail.content_subtype = 'html'

    mail.attach_file(avatar_path)

    mail.send()

    return HttpResponseRedirect(reverse('users:profile'))


def register(request):
    # current_site = Site.objects.get_current()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = MyUserCreationForm()

    return render(request, 'users/en_register.html', {
                        # 'host': current_site.domain,
                        'form': form
                   })


def ro_register(request):
    # current_site = Site.objects.get_current()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = MyUserCreationForm()

    return render(request, 'users/register.html', {
                        # 'host': current_site.domain,
                        'form': form
                   })


def ro_news_letter(request):

    if request.method == 'POST':
        form = RoNewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Felicitari, te-ai abonat!')
            return HttpResponseRedirect(reverse('review:app_review'))
        # else:
        #     messages.success(request, 'Esti deja abonat!')
            # return HttpResponseRedirect(reverse('review:app_review'))
    else:
        form = RoNewsletterForm()

    return render(request, 'snippets/footer.html', {

                        'form_news': form
                   })


def en_news_letter(request):

    if request.method == 'POST':
        form = EnNewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Done!')
            return HttpResponseRedirect(reverse('review:en_app_review'))
        # else:
        #     messages.success(request, 'Your are a subscriber!')
        #     return HttpResponseRedirect(reverse('review:en_app_review'))
    else:
        form = EnNewsletterForm()

    return render(request, 'snippets/en_footer.html', {

                        'form_news': form
                   })


def contact_view(request):
    contact_list = ContactApp.objects.all()
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_template = get_template('users/contact_email_send.html')

            email_content = email_template.render(
                {

                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'mobile': mobile,
                    'subject': subject,
                    'message': message,
                }
            )

            mail = EmailMultiAlternatives(
                f'Boanca Ionut Silviu:{subject}',
                email_content,
                settings.EMAIL_HOST_USER,
                [email],
                (settings.EMAIL_HOST_USER, )
            )
            mail.content_subtype = 'html'
            mail.send()
            messages.success(request, 'Mesajul tau a fost trimis!')
            return HttpResponseRedirect(reverse('users:contact'))
    else:
        form = ContactForm()

    context = {
        'form': form,
        'contact_list': contact_list}

    return render(request, "users/contact.html", context)


def en_contact_view(request):
    contact_list = EnContactApp.objects.all()
    if request.method == 'POST':

        form = EnContactForm(request.POST)

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_template = get_template('users/en_contact_email_send.html')

            email_content = email_template.render(
                {

                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'mobile': mobile,
                    'subject': subject,
                    'message': message,
                }
            )

            mail = EmailMultiAlternatives(
                f'Boanca Ionut Silviu:{subject}',
                email_content,
                settings.EMAIL_HOST_USER,
                [email],
                (settings.EMAIL_HOST_USER, )
            )
            mail.content_subtype = 'html'
            mail.send()
            messages.success(request, 'Your message has been send!')
            return HttpResponseRedirect(reverse('users:en_contact'))
    else:
        form = EnContactForm()

    context = {
        'form': form,
        'contact_list': contact_list}

    return render(request, "users/en_contact.html", context)


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Parola ta a fost modificata')
            return redirect('users:profile')
        else:
            messages.error(request, 'Corecteaza eroarea de mai jos')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })


@login_required
def en_change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed!')
            return redirect('users:en_profile')
        else:
            messages.error(request, 'Error:')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/en_change_password.html', {
        'form': form
    })
