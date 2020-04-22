from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse,redirect
from django.views import generic
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
import datetime
class home(generic.FormView):
    def get(self, request, *args, **kwargs):
        slideshows = Slideshows.objects.all()
        drone = Drone.objects.all()
        context = {
            "slideshows": slideshows,
            "homemission": Homemission,
        }

        return render(request, 'chavakali/home.html',context)


class ministries(generic.FormView):
    def get(self, request, *args, **kwargs):

        return render (request, 'chavakali/ministries.html',)

class mercy(generic.FormView):
    def get(self,request, *args, **kwargs):
        mercyimageone = Mercyimageones.objects.all()
        mercycover = Mercycover.objects.all()
        mercyfooter = Mercyfooter.objects.all()

        context = {
            "mercyimageone": mercyimageone,
            "mercycover": Mercycover,
            "mercyfooter": Mercyfooter
        }
        return render(request, 'chavakali/mercyministry.html',)

class prison(generic.FormView):
    def get(self, request, *args, **kwargs):

        return render(request, 'chavakali/prisonministry.html',)

class outreach (generic.FormView):
    def get(self,request, *args, **kwargs):

        return render (request, 'chavakali/outreachministry.html',)

class hospital(generic.FormView):
    def get(self, request, *args, **kwargs):

        return render(request, 'chavakali/hospitalministry.html',)

class men(generic.FormView):
    def get(self, request, *args, **kwargs):
        mencover =Mencover.objects.all()
        menfooter=Menfooter.objects.all()

        context = {
            "mencover": mencover,
            "menfooter":menfooter
        }

        return render(request, 'chavakali/mensministry.html',)

class women(generic.FormView):
    def get(self, request, *args, **kwargs):
        womencover = Womencover.objects.all()
        womenfooter = Womenfooter.objects.all()

        context = {
            "womencover":womencover,
            "womenfooter":womenfooter
        }
        return render(request, 'chavakali/womensministry.html',)

class couples(generic.FormView):
    def get (self, request, *args, **kwargs):
        couplescover = Couplescover.objects.all()
        couplesfooter = Couplesfooter.objects.all()


        context = {
            "couplescover":couplescover,
            "couplesfooter":couplesfooter
        }

        return render(request, 'chavakali/couples.html',)

class youths(generic.FormView):
    def get(self, request, *args, **kwargs):
        youthcover = Youthcover.objects.all()
        youthfooter = Youthfooter.objects.all()

        conetxt = {
            "youthcover":youthcover,
            "youthfooter":youthfooter
        }
        return render (request, 'chavakali/youthministry.html',)


class teens(generic.FormView):
    def get(self, request, *args, **kwargs):
        teenscover = Teenscover.objects.all()
        teensfooter = Teensfooter.objects.all()

        context = {
            "teenscover":teenscover,
            "teensfooter":teensfooter
        }
        return render (request, 'chavakali/teens.html',)


class sundayschool(generic.FormView):
    def get (self, request, *args, **kwargs):
        sundayschoolcover = Sundayschoolcover.objects.all()
        sundayschoolfooter = Sundayschoolfooter.objects.all()

        context = {
            "sundayschoolcover":sundayschoolcover,
            "sundayschoolfooter":sundayschoolfooter
        }
        return render (request, 'chavakali/sundayschool.html',)

class founder (generic.FormView):
    def get(self, request, *args, **kwargs):
        bishop = Bishop.objects.all()
        reverend =Reverend.objects.all()

        context = {
            "bishop":bishop,
            "reverend":reverend
        }
        return render(request, 'chavakali/founder.html',)

class events(generic.FormView):
    def get(self, request, *args,**kwargs):
        eventone =Eventone.objects.all()
        eventtwo =Eventtwo.objects.all()
        eventtheree =Eventthree.objects.all()

        context = {
            "eventone":eventone,
            "eventtwo":eventtwo,
            "eventthree":eventtheree
        }

        return render(request,'chavakali/events.html')
class projects(generic.FormView):
    def get(self, request, *args, **kwargs):
        projectone =Projectone.objects.all()
        projecttwo =Projecttwo.objects.all()
        projectthree =Projectthree.objects.all()

        context = {
            "projectone":projectone,
            "projecttwo":projecttwo,
            "projectthree":projectthree
        }
        return render (request, 'chavakali/projects.html',)



class gallery(generic.FormView):
    def get (self, request, *args, **kwargs):

        return render(request, 'chavakali/gallery.html')

class sermons(generic.FormView):
    def get(self, request, *args, **kwargs):

        return render(request, 'chavakali/sermons.html')

class give(generic.FormView):
    def get (self, request, *args, **kwargs):

        return render(request, 'chavakali/givenow.html')


class wwn(generic.FormView):
    def get (self, request, *args, **kwargs):
        wwncover = Wwncover.objects.all()
        wwnfooter = Wwnfooter.objects.all()

        context = {
            "wwncover":wwncover,
            "wwnfooter":wwnfooter
        }

        return render(request, 'chavakali/wwn.html')

class prayer(generic.FormView):
    def get(self,request,*args,**kwargs):
        return HttpResponse("hey")
    def post(self, request, *args, **kwargs):
        form = request.POST

        name = form["name"]
        phoneNumber = form["phoneNumber"]
        prayerRequest = form["prayerRequest"]

        return HttpResponse("Prayer Request Submited")

class login(generic.FormView):
    def post(self, request, *args, **kwargs):
        form = request.POST
        useremail = form["userermail"]
        password = form["password"]

        try:
            username = User.objects.get(email=useremail)
            username = username.username
        except:
            return HttpResponse("Email not Registered")

        return HttpResponse(username)
