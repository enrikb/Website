from django.shortcuts import render

# Create your views here.

def home(request):
	test = "hello"
	return render(request, 'marketplace/index.html', locals())
