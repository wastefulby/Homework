from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models

# Create your views here.

def show_references(request):
    return render(request, template_name='references/references.html', context={})

def genre_list(request):
    if request.method == "GET":
        reference_name = request.GET.get('name')

        if request.GET.get('name') == 'author':
            reference = models.ReferencesAuthor.objects.all()
        elif request.GET.get('name') == 'genre':
            reference = models.ReferencesGenre.objects.all()
        elif request.GET.get('name') == 'currenсy':
            reference = models.ReferencesCurrenсy.objects.all()
        return render(request, template_name='references/list.html', context={'objects': reference, 'name': reference_name})

def create(request):
    if request.method == "GET":
        reference_name = request.GET.get('name')
        
        if request.GET.get('name') == 'author':
            reference = models.ReferencesAuthor.objects.all()
        elif request.GET.get('name') == 'genre':
            reference = models.ReferencesGenre.objects.all()
        elif request.GET.get('name') == 'currenсy':
            reference = models.ReferencesCurrenсy.objects.all()
        return render(request, template_name='references/create.html', context={'name': reference_name})
    if request.method == "POST":
        reference_name = request.POST.get('url')
        
        if request.POST.get('url') == 'author':
            genre_update = models.ReferencesAuthor()
            reference = models.ReferencesAuthor.objects.all()
        elif request.POST.get('url') == 'genre':
            genre_update = models.ReferencesGenre()
            reference = models.ReferencesGenre.objects.all()
        elif request.POST.get('url') == 'currenсy':
            genre_update = models.ReferencesCurrenсy()
            reference = models.ReferencesCurrenсy.objects.all()
        
        genre_update.name = request.POST.get("name")
        genre_update.description = request.POST.get("description")
        genre_update.save()
    return render(request, template_name='references/list.html', context={'objects': reference, 'name': reference_name})
 
def update(request, pk):
    if request.method == "GET":
        reference_name = request.GET.get('name')
        
        if request.GET.get('name') == 'author':
            genre_update = models.ReferencesAuthor.objects.get(pk=pk)
        elif request.GET.get('name') == 'genre':
            genre_update = models.ReferencesGenre.objects.get(pk=pk)
        elif request.GET.get('name') == 'currenсy':
            genre_update = models.ReferencesCurrenсy.objects.get(pk=pk)
        return render(request, template_name='references/update.html', context={'objects': genre_update, 'name': reference_name})        
    if request.method == "POST":
        reference_name = request.POST.get('url')
        
        if request.POST.get('url') == 'author':
            genre_update = models.ReferencesAuthor.objects.get(pk=pk)
            reference = models.ReferencesAuthor.objects.all()
        elif request.POST.get('url') == 'genre':
            genre_update = models.ReferencesGenre.objects.get(pk=pk)
            reference = models.ReferencesGenre.objects.all()
        elif request.POST.get('url') == 'currenсy':
            genre_update = models.ReferencesCurrenсy.objects.get(pk=pk)
            reference = models.ReferencesCurrenсy.objects.all()
        
        genre_update.name = request.POST.get("name")
        genre_update.description = request.POST.get("description")
        genre_update.save()
        return render(request, template_name='references/list.html', context={'objects': reference, 'name': reference_name})
     
def delete(request, pk):
    if request.method == 'GET':
        reference_name = request.POST.get('name')
        if request.GET.get('name') == 'author':
            models.ReferencesAuthor.objects.get(pk=pk).delete()
            reference = models.ReferencesAuthor.objects.all()
        elif request.GET.get('name') == 'genre':
            models.ReferencesGenre.objects.get(pk=pk).delete()
            reference = models.ReferencesGenre.objects.all()
        elif request.GET.get('name') == 'currenсy':
            models.ReferencesCurrenсy.objects.get(pk=pk).delete()
            reference = models.ReferencesCurrenсy.objects.all()
            
        return render(request, template_name='references/list.html', context={'objects': reference, 'name': reference_name})


