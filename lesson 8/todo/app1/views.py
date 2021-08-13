from django.shortcuts import render, redirect
from django.views import View
from .models import Task


class TodoView(View):
    def get(self, request):
        context = {
            'tasks': [
                {'id': i.id,
                 'text': i.text,
                 'completed': 'completed' if i.is_completed else ''} for i in Task.objects.all()
            ]
        }
        print(context)
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(text=request.POST['text'])
        return redirect('/')


class Delete(View):
    def get(self, request, task_id):
        Task.objects.get(id=task_id).delete()
        return redirect('/')


class Check(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        task.is_completed = False if task.is_completed else True
        task.save()
        print(task.is_completed)
        return redirect('/')
