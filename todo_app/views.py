from django.shortcuts import render,redirect, get_object_or_404
from .models import ToDo_Task
from django.contrib import messages


# Create your views here.
def task_create(request):
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('description')
        deadline=request.POST.get('deadline')
        status =request.POST.get('status')
        item_obj =ToDo_Task(title=title,description=desc,deadline=deadline,status=status)
        item_obj.save()
        messages.success(request, 'Task created successfully!')
        return redirect('task_list')
    else:
         tasks=ToDo_Task.objects.all()
         return render(request,'index.html',{'tasks':tasks})
    


def task_list(request): 
    tasks=ToDo_Task.objects.all()
    return render(request,'list.html',{'tasks':tasks})


def task_edit(request, pk):
    task = get_object_or_404(ToDo_Task, pk=pk)

    if request.method == 'POST':
        print(request.POST)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.deadline = request.POST.get('deadline')
        task.status = request.POST.get('status')
        task.save()

        messages.success(request, 'Task updated successfully!')
        return redirect('task_list')

    return render(request, 'update.html', {'task': task})



def task_delete(request,pk):
    task=ToDo_Task.objects.get(pk=pk)
    task.delete()
    tasks=ToDo_Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})