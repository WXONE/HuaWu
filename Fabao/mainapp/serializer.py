from rest_framework import serializers
from mainapp.models import *
#from django.contrib.auth.models import
#json 格式化 model 对象

class LawArticleAllSerializer(serializers.ModelSerializer):
    LawArticleAllContent = serializers.PrimaryKeyRelatedField(many=True,read_only=True,)

    class Meta:
        model = LawArticleAll
        fields = ('LawArticleId','LawArticleAllContent','ContentUrl')

class LawArticleAllListSerializer (serializers.ModelSerializer):
    Law_Article = LawArticleAllSerializer(source = 'LawArticleAll_set',read_only = True,many=True)

    class Meta:
        model = LawArticleAllList
        fields = ('LawArticleAllList','Law_Article_All')

class LawSimilaritySerializer(serializers.ModelSerializer):
    class Meta:
        model = LawSimilarity
        fields = '__all__'
class LawyerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawyerList
        fields = '__all__'

class CaseAllListSerializer(serializers.ModelSerializer):
    CaseAllListEachName = serializers.PrimaryKeyRelatedField(read_only=True,)
    class Meta:
        model = CaseAllList
        fiele = '__all__'
class CaseAllSerializer(serializers.ModelSerializer):
    Case_All = CaseAllListSerializer(source='caseall_set',read_only="True",many=True)
    class Meta :
        model = CaseAll
        fields = '__all__'

class LawSimilaritySerializer(serializers.ModelSerializer):
    class Meta :
        model = LawSimilaritySerializer
        fields = '__all__'
class LawRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawRecommend
        fields = '__all__'



