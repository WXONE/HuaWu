from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, mixins, generics, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# from mainapp.serializer import *
# from .models import *

from .models import LawSimilarity,MyUser,LawyerList,LawArticleAllList,LawArticleAll,CaseAllList,CaseAll,LawRecommend,UploadFile
from mainapp.serializer import LawArticleAllSerializer,LawArticleAllListSerializer,LawSimilaritySerializer,LawyerListSerializer,CaseAllListSerializer,CaseAllSerializer,LawSimilaritySerializer,LawRecommendSerializer

class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    传入的pk值为案例，查询相似案例
    '''
    queryset = CaseAll.objects.all()
    serializer_class = CaseAllSerializer
    @action(detail=False , methods=['get'])
    def get_random_menus(self,request):
        import random
        import numpy as np
        size = self.queryset.count()
        count = request.GET['count']
        count = int(count)
        #sample:从一个list中随机挑选n个数组成list
        random_index = random.sample(range(size),count)
        random_Laws = np.array(self.queryset)[random_index]
        serializer = CaseAllSerializer
        return Response(serializer.data)
@csrf_exempt
def upload_string(request):
    if request.method == 'POST':
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name,file)
        upload_string_url = fs.url(filename)

        from mainapp.tests import test_string
        test_string(upload_string_url)
        return HttpResponse(upload_string_url)



# Create your views here.
