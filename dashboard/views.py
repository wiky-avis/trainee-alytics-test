from django.shortcuts import redirect, render

from .figures import get_graph
from .forms import FunctionForm
from .models import Function


def home(request):
    graph_list = Function.objects.all()
    form = FunctionForm()
    return render(
        request, 'base.html', {
            'graph_list': graph_list,
            'form': form})


def new_graph(request):
    form = FunctionForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        graph = form.save(commit=False)
        graph.graph = get_graph()
        graph.save()
        return redirect('home')
    return render(request, 'includes/new_graph.html', {'form': form})
