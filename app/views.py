from django.http import JsonResponse
from django.shortcuts import render
from .models import Text

from django.db.models import Q

def home(request):
    if request.method == "GET":
        try:
            sms_words = request.GET.get('sms').split(' ')
        except:
            sms_words=[]
        array_of_objects=[]
        for i in sms_words:
            sms_db = Text.objects.filter(Q(contenu=i) | Q(normalization=i))
            if sms_db.count()>0:
                array_of_objects.append(sms_db)
        context={"smss":array_of_objects}
    return render(request,"index.html",context)

def get_sms(request):
        try:
            sms_words = request.GET.get('sms').split(' ')
            print(sms_words)
        except:
            sms_words=[]
        array_of_objects=[]
        for i in sms_words:
            sms = Text.objects.filter(contenu=i)
            for s in sms:
                array_of_objects.append(str(s.normalization))
        data = array_of_objects
        return JsonResponse({"data":data},safe=False)

