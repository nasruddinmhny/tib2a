from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def manage_mahasiswa(request):
    template_name='mahasiswa/index.html'
    title = 'List Mahasiswa'

    context={
        'title':title,
    }
    return render(request,template_name,context)

def add_mahasiswa(request):
    template_name='mahasiswa/add_mahasiswa.html'
    title = 'Form Tambah Data Mahasiswa'
    context={
        'title':title,
    }
    return render(request,template_name,context)