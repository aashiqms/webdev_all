from django.shortcuts import render
from portfolio_app.forms import NewUserForm
from .forms import FeedbackForm
# from django.http import HttpResponse
# from portfolio_app.models import User
# from . import forms


def index(request):
    return render(request, 'portfolio_app/index.html')


def users_function(request):
    
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)  # to save data to database and commitm it to database
            return index(request)
        else:
            print('ERROR')
            
    return render(request, 'portfolio_app/users.html', {'form_key': form})


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'portfolio_app/thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'portfolio_app/feedback.html', {'form': form})

# Forms created from forms.Form are manually configured by you. You're better off using these for forms
# that do not directly interact with models. For example a contact form, or
# a newsletter subscription form, where you might not necessarily be interacting with the database.
# Where as a form created from forms.ModelForm will be automatically created and then can later be tweaked by you.
# The best examples really are from the superb documentation provided on the Django website.


