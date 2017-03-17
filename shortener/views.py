from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm, CheckPswForm
from .models import KirrURL

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        bg_image = 'https://i.ytimg.com/vi/YrddaP6ml1M/maxresdefault.jpg'#'http://zonewallpaper.net/wp-content/uploads/2016/11/Best-4K-Nature-Wallpapers.jpg'#'https://upload.wikimedia.org/wikipedia/commons/0/05/20100726_Kalamitsi_Beach_Ionian_Sea_Lefkada_island_Greece.jpg'
        context = {
            "title": "WotChat",
            "form": the_form,
            "bg_image": bg_image
        }
        return render(request, "shortener/home.html", context) # Try Django 1.8 & 1.9 http://joincfe.com/youtube

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "WotChat",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
    
        return render(request, template ,context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

class RedirectToEmailcheckView(View):
    def get(self, request, shortcode=None, *args, **kwargs):        
        qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():        
            raise Http404
        obj = qs.first()
        
        the_form = CheckPswForm()
        bg_image = 'https://i.ytimg.com/vi/YrddaP6ml1M/maxresdefault.jpg'
        context = {
            "title": "WotChat",
            "form": the_form,
            "bg_image": bg_image
        }
        return render(request, "shortener/checkemail.html", context) 

    def post(self, request, shortcode=None, *args, **kwargs):
        form = CheckPswForm(request.POST)
        context = {
            "title": "WotChat",
            "form": form
        }
        template = "shortener/checkemail.html"
        if form.is_valid():
            new_email = form.cleaned_data.get("email")
            try:
                obj = KirrURL.objects.get(email=new_email, shortcode=shortcode)
                # obj.info
                template = "shortener/results.html"
                context = {
                    "object": obj,
                    "no_users":4,
                    "user": ['io', 'mamt', 'e','tu'],
                }
            except:
                template = "shortener/already-exists.html"
                context = {}                        
    
        return render(request, template, context)

        # return HttpResponseRedirect(obj.url)        




