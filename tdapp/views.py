from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render,get_object_or_404
from .forms import UserForm,UserProfileInfoForm
from .models import UserProfileInfo
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import DeleteView,TemplateView,RedirectView
from django.db.models import Q
# Create your views here.
# def index(request):
#     return render(request,'tdapp/index.html')

class index(TemplateView):
    template_name = 'tdapp/index.html'
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['all_details'] = UserProfileInfo.objects.all().order_by('-id')
        return context


class Teacher_details(TemplateView):
    template_name = 'tdapp/teacher_details.html'
    def get_context_data(self, **kwargs):
        context = super(Teacher_details, self).get_context_data(**kwargs)
        user_d = get_object_or_404(UserProfileInfo, id=self.kwargs['id'])
        context['user_data'] = user_d
        return context

## same as above in class based view 
# def Teacher_details(request,id):
#     people = UserProfileInfo.objects.filter(id=id).first()
#     context = {
#         'user_data': people,
#     }
#     return render(request,'tdapp/teacher_details.html',context)


class Filter_directory(TemplateView):
    template_name = 'tdapp/filter_directory.html'
    def get_context_data(self, **kwargs):
        context = super(Filter_directory, self).get_context_data(**kwargs)
       
        si = self.request.GET.get('si')
        filter_users = User.objects.filter(Q(last_name__icontains=si))
        # context['result_count'] = users.count
        context['filter_users'] = filter_users
        return context
		#context['all_posts'] = UserPost.objects.filter(uploaded_by__in=users)
            

def register(request):

    registered = False

    if request.method == 'POST':
        email=request.POST['email']
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # Email validation already exist or not!
            if User.objects.filter(email=email).exists():
                print("email already exist")
                messages.info(request,'This Email already exist!')
                return redirect('/tdapp/register/')

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']
            profile.first_name = user.first_name
            profile.last_name = user.last_name
            profile.username = user.username
            profile.email = user.email
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'tdapp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'tdapp/login.html', {})


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))




