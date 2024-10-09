from django.shortcuts import render, HttpResponse
from myapp.forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home(request):
        return render(request, 'home.html')

def about(request):
        return render(request, 'about.html')

def contact(request):
        return render(request, 'contact.html')

def gallery(request):
        return render(request, 'gallery.html')


def contact(request):
        if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                        # Process the form data
                        return redirect('success')
        else:
                form = ContactForm()
        return render(request, 'contact.html', {'form': form})

def success(request):
        return HttpResponse('Success!')