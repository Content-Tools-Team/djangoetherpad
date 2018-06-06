from django.shortcuts import render, get_object_or_404
import datetime
import time
import urllib
from urllib.parse import urlparse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# additional imports
from py_etherpad import EtherpadLiteClient

# local imports
from etherpad.models import Pad 
# from etherpadlite import forms
from etherpad import config



def home(request):
    pads = Pad.objects.all()
    return render(request, 'home.html', {'pads': pads})

# Create your views here.
def pad(request, pk):
    """Create and session and display an embedded pad
    """

    # Initialize some needed values
    pad = get_object_or_404(Pad, pk=pk)
    padLink = pad.server_url + 'p/' + pad.groupID + '$' + \
        urllib.parse.quote_plus(pad.name)
    server = urlparse(pad.server_url)
    author = User.objects.get(user=request.user)
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    # Create the session on the etherpad-lite side
    expires = datetime.datetime.utcnow() + datetime.timedelta(
        seconds=config.SESSION_LENGTH
    )
    epclient = EtherpadLiteClient(pad.server_apikey, pad.server_apiurl)

    try:
        epclient.createSession(
            pad.groupID,
            author.id,
            time.mktime(expires.timetuple()).__str__()
        )
    except Exception as e:
        # response = render(
        #     'etherpad-lite/pad.html',
        #     {
        #         'pad': pad,
        #         'link': padLink,
        #         'server': server,
        #         'uname': author.user.__unicode__(),
        #         'error': _('etherpad-lite session request returned:') +
        #         ' "' + e + '"'
        #     },
        #     context_instance=RequestContext(request)
        # )
        # return response
        return render(request, 'pad.html', {'pad':pad, 'link': padLink, 'server':server, 'uname': username, 'error': _('etherpad-lite session request returned:') + ' "' + e + '"'})
   
   
   
    # Set up the response
    # response = render(
    #     'etherpad-lite/pad.html',
    #     {
    #         'pad': pad,
    #         'link': padLink,
    #         'server': server,
    #         'uname': author.user.__unicode__(),
    #         'error': False
    #     },
    #     context_instance=RequestContext(request)
    # )

    return render(request, 'pad.html', {'pad': pad,'link': padLink,'server': server,'uname': author.username ,'error': False} )
