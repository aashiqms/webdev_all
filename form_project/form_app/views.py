from django.shortcuts import render
from . import forms



def index(request):
    return render(request, 'form_app/index.html')
    

def form_name_view(request):
    form = forms.FormName
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('validation successful')
            print('name: ' +form.cleaned_data['name'] )
            print('email: ' +form.cleaned_data['email'] )
            print('text: ' +form.cleaned_data['text'] )
    return render(request, 'form_app/form_page.html', {'form_d_view':form})
