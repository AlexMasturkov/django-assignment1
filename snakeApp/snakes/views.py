from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Snake
from .forms import SnakeForm

# Create your views here.
def index(request):
    return render(request, 'index.html',{})


def snakes(request):
    snakes = Snake.objects.all()
    return render(request, 'snakes.html',{
        'snakes': snakes
    })

def add(request):
  if request.method == 'POST':
    form = SnakeForm(request.POST)
# capitalizing name string
    new_form = form.save(commit=False)
    name = form.cleaned_data['name']
    new_form.name = name.capitalize()
    new_form.save()
    
    messages.success(request, 'Snake has been added')
    return redirect('snakes')
  else:
    form = SnakeForm()
    return render(request, 'add.html', {
      'form': form
    })


def edit(request, id):
  snake = get_object_or_404(Snake, pk=id)
  if request.method == 'POST':
    form = SnakeForm(request.POST, instance=snake)
    if form.is_valid():     
      form.save()
      messages.success(request, 'Snake has been edit')
    else:
      messages.error(request,'wrong')  
    return redirect('snakes')
  else:
    form = SnakeForm(instance=snake)
    return render(request, 'edit.html', {
      'form': form,
      'snake': snake
    })



def delete(request, id):
  if request.method == 'POST':
    snake = get_object_or_404(Snake, pk=id)
    snake.delete()  
    messages.success(request, 'Snake has been deleted')
  return redirect('snakes')

