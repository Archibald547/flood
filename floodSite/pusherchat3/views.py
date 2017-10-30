#render library for returning views to the browser
from django.shortcuts import render
#decorator to make a function only accessible to registered users
from django.contrib.auth.decorators import login_required
#import the user library
from pusher import Pusher

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#replace the xxx with your app_id, key and secret respectively
#instantate the pusher class
#pusher = Pusher(app_id=u'421271', key=u'bdf7192982f166c2e380', secret=u'20a8fe413e31f927e643')
pusher_client = Pusher(
  app_id='422896',
  key='3ee88d093290efeabf8f',
  secret='95bf4b337d7f605b5817',
  cluster='ap1',
  ssl=True
)
# Create your views here.

#login required to access this page. will redirect to admin login page.
@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"chat3.html");

@csrf_exempt
def broadcast(request):
    #pusher.trigger(u'my-channel', u'my-event', {u'name': request.user.username, u'message': request.POST['message']})
    pusher_client.trigger('my-channel', 'my-event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done")
