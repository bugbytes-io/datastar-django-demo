from django.shortcuts import render
from films.models import Film


# Create your views here.
def index(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'index.html', context)