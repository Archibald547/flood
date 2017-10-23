from .models import todo
from django.shortcuts import render_to_response, render
from .add_task import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from django.shortcuts import get_object_or_404
from schedule.models import Event, EventRelation, Calendar
import datetime
 
def index(request):
    items = todo.objects.filter(completed=False)
    return render_to_response('todo.html', {'items': items}) 

def completed(request, pk):
    post = todo.objects.get(pk=pk)
    post.completed = True
    post.save()

    items = todo.objects.filter(completed=False)
    return render_to_response('todo.html', {'items': items})    

def delete_task(request, pk):
    task = todo.objects.get(pk=pk)
    task.delete()

    items = todo.objects.filter(completed=False)
    return render_to_response('todo.html', {'items': items}) 

def post_task(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
        	#Post for todo list reference
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            #Event for calendar reference
            # event = form.save(commit=False)
            # event.title = form.cleaned_data['name']
            # event.description = form.cleaned_data['description']
            # event.start = form.cleaned_data['date']
            # event.end = event.start + datetime.timedelta(minutes=30)
            # event.save()

            return redirect('todo')
    else:
        form = PostForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, pk):
    post = get_object_or_404(todo, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('todo')
    else:
        form = PostForm(instance=post)
    return render(request, 'add_task.html', {'form': form})
    		

