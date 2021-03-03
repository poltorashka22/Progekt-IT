from django.shortcuts import render

# Create your views here.
def hoom(request):
	return render(request, 'hoome.html')
