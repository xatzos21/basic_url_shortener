from django.shortcuts import render, redirect
import random, string
from .models import Url


# Create your views here.
def home(request):
    return render(request, "main_app/home.html")


def create_short_url(request):
    if request.method == "POST":
        slug = "".join(random.choice(string.ascii_letters) for x in range(10))
        url = request.POST["url"]
        new_url = Url(url=url, slug=slug)
        new_url.save()
        return redirect("/")


def url_created(request):
    url = Url.objects.all()
    return render(request, "main_app/short_url.html", {"url": url})
