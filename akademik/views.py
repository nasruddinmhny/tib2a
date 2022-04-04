from django.shortcuts import render,HttpResponse

# Create your views here.
def dashboard_akademik(request):
    return HttpResponse('<h2>Halaman Dashboard</h2>')

def add_akademik(request):
    data_akademik = 'akademik'
    nama_mhs = 'Rifki'

    context = {
        'data_akademik':data_akademik,
        'nama_mhs':nama_mhs,

    }

    return render(request,'index.html',context)