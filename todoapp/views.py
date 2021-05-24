from django.shortcuts import render,redirect,HttpResponse
from .models import Todo
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListview(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todo1'


class TaskDetailView(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'todo'

class TaskUpdateView(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'todo'
    fields = ('task','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('abcd')






def add(request):
    todo1 = Todo.objects.all()
    if request.method=="POST":
        task=request.POST.get('task','')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=Todo(task=task,priority=priority,date=date)
        todo.save()

    return render(request,'home.html',{'todo1':todo1})


def delete(request,taskid):
    if request.method=="POST":
        task=Todo.objects.get(id=taskid)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,taskid):
    todo=Todo.objects.get(id=taskid)
    forms=TodoForm(request.POST or None,instance=todo)
    if forms.is_valid():
        forms.save()
        return redirect('/')
    return render(request,'update.html',{'forms':forms,'todo':todo})
