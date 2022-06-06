from django.contrib import messages
from django.http import HttpResponseRedirect
from room.models import CommentForm, Comment

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.room_id = id
            data.save()
            messages.success(request, "Sizning kommentariyangiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

