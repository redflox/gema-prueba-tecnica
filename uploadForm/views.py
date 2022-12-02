from django.shortcuts import render, redirect
from . import models
from django.core.files.storage import FileSystemStorage
import csv
from os import remove

# Create your views here.

def uploadFile(request):
    try:
        if request.method == "POST" and request.FILES['uploadedFile']:
            uploadedFile = request.FILES['uploadedFile']
            fileSystem = FileSystemStorage()
            # Saving the information in local (/media)
            fileName = fileSystem.save(uploadedFile.name, uploadedFile)

            # Open the file local for verification
            pathName = './media/' + fileName
            # with open(pathName, newline='') as f:
            #     users = csv.reader(f, delimiter=',', quotechar='\n')
            #     for user in users:
            #         if (int(user[3]) <=0 or int(user[3]) >=4):
            #             return render(request, "upload.html", {
            #                 'error': 'File Corrupted'
            #             })
            
            # Saving the information in the database if the file is integrity
            archivo = models.Archivo(
                name = fileName
            )
            archivo.save()

            # get file of database
            file = models.Archivo.objects.get(name=fileName)

            with open(pathName, newline='') as f:
                users = csv.reader(f, delimiter=',', quotechar='\n')
                for user in users:
                    estado = models.Estado.objects.get(id=user[3])
                    revisor = models.Revisor.objects.get(id=user[4])

                    user = models.Usuario(
                        email = user[0],
                        name = user[1],
                        surname = user[2],
                        estado = estado,
                        archivo = file,
                        revisor = revisor
                    )
                    user.save()
            
            
            return redirect('/fileresult/' + fileName)
    except:
        return render(request, "upload.html", {
                            'error': 'not exist file or type file is not supported'
                        })      
    return render(request, "upload.html")

def fileResult(request, fileName):
    arc = models.Archivo.objects.get(name=fileName)   
    act = models.Usuario.objects.filter(archivo=arc, estado=1)
    ina = models.Usuario.objects.filter(archivo=arc, estado = 2)
    wait = models.Usuario.objects.filter(archivo=arc, estado = 3)

    return render(request, 'fileresult.html',{
        'usersActive': act,
        'usersInactive': ina,
        'usersWait': wait
    })