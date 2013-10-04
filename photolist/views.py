from django.shortcuts import render_to_response
from models import Photo
from random import sample
# Create your views here.
def index_list(request):
    photos = Photo.objects.all()
    return render_to_response('photolist/index.html',{'photos':photos})
    

def get_random(request)
    count = Photo.objects.all().count()
    rand_ids = sample(xrange(1, count), 10)
    Photo.objects.filter(id_in=rand_ids)
