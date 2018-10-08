from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
#相似案件查询
class LawSimilarity(models.Model):
    TopOneLawSimilarityName = models.TextField(max_length = 100)
    TopTwoLawSimilarityName = models.TextField(max_length = 100)
    TopThreeLawSimilarityName = models.TextField(max_length = 100)

    def __add__(self, other):
          TopOneLawSimilarityName = self.TopOneLawSimilarityName+other.TopOneLawSimilarityName
          TopTwoLawSimilarityName = self.TopOneLawSimilarityName+other.TopTwoLawSimilarityName
          TopThreeLawSimilarityName = self.TopThreeLawSimilarityName+other.TopThreeLawSimilarityName

          return LawSimilarity(
          TopOneLawSimilarityName = TopOneLawSimilarityName,
          TopTwoLawSimilarityName = TopTwoLawSimilarityName,
          TopThreeLawSimilarityName = TopThreeLawSimilarityName,
          )
#用户表
class MyUser(models.Model):
    UserName = models.CharField(max_length=100,primary_key=True)#用户名
    UserPassword = models.CharField(max_length=100)#密码
    UserJob = models.CharField(max_length=50,null=True)#用户职业
    UserAvatar = models.FileField(upload_to='media')#用户头像

    def __str__(self):
        return self.UserName
#律师表
class LawyerList(models.Model):
   # user = models.ForeignKey(MyUser,on_delete=models.CASCADE)#用户
    LawyerName = models.CharField(max_length= 100 ,primary_key=True)#律师名
    LawyerEvaluation = models.FloatField(default= 0 )#律师评价
    LawyerIntroducation = models.TextField(max_length=100)#律师简介
    LawyerRank  =  models.TextField(max_length=100)#律师等级

    def __str__(self):
        return self.LawyerName

#所有法条表
class LawArticleAllList(models.Model):
    LawArticleAllList = models.TextField(max_length=100,primary_key=True)#法条名


    def __str__(self):
        return self.LawArticleAllList
#法条内容表
class LawArticleAll(models.Model):
    LawArticleId = models.CharField(max_length=100,primary_key=True)#法条id
    LawArticleAllContent = models.ForeignKey(LawArticleAllList,on_delete=models.CASCADE)#法条内容
    ContentUrl =models.URLField(max_length=200)#详情url


class CaseAllList(models.Model):
    CaseAllList = models.TextField(max_length=100,primary_key=True)#案件名
    def __str__(self):
        return self.CaseAllList
#所有案件表
class CaseAll(models.Model):
    caseId = models.CharField(max_length=100,primary_key=True)#案件id
    caseName = models.ForeignKey(LawArticleAllList)


#法条推荐
class LawRecommend(models.Model):
    TopOneLawRecommend = models.TextField(max_length=100)
    TopTwoLawRecommend = models.TextField(max_length=100)
    TopThreeLawRecommend = models.TextField(max_length=100)
    TopFourLawRecommend = models.TextField(max_length=100)
    TopFiveLawRecommend = models.TextField(max_length=100)
    TopSixLawRecommend = models.TextField(max_length=100)
    TopSevenLawRecommend = models.TextField(max_length=100)
    TopeightLawRecommend = models.TextField(max_length=100)
    TopNineLawRecommend = models.TextField(max_length=100)
    TopTenLawRecommend = models.TextField(max_length=100)
    def __add__(self, other):
        TopOneLawRecommend = self.TopOneLawRecommend + other.TopOneLawSimilarityName
        TopTwoLawRecommend = self.TopTwoLawRecommend + other.TopTwoLawRecommend
        TopThreeLawRecommend = self.TopThreeLawRecommend + other.TopThreeLawRecommend
        TopFourLawRecommend = self.TopFourLawRecommend + other.TopFourLawRecommend
        TopFiveLawRecommend = self.TopFiveLawRecommend + other.TopFiveLawRecommend
        TopSixLawRecommend = self.TopSixLawRecommend + other.TopSixLawRecommend
        TopSevenLawRecommend = self.TopSevenLawRecommend + other.TopSevenLawRecommend
        TopeightLawRecommend = self.TopeightLawRecommend + other.TopeightLawRecommend
        TopNineLawRecommend = self.TopNineLawRecommend + other.TopNineLawRecommend
        TopTenLawRecommend = self.TopTenLawRecommend + other.TopTenLawRecommend
        return LawRecommend (
            TopOneLawRecommend=     TopOneLawRecommend ,
            TopTwoLawRecommend =    TopTwoLawRecommend ,
            TopThreeLawRecommend  =  TopThreeLawRecommend ,
            TopFourLawRecommend =   TopFourLawRecommend,
            TopFiveLawRecommend =   TopFiveLawRecommend ,
            TopSixLawRecommend =    TopSixLawRecommend ,
            TopSevenLawRecommend  =  TopSevenLawRecommend ,
            TopeightLawRecommend  = TopeightLawRecommend ,
            TopNineLawRecommend =   TopNineLawRecommend ,
            TopTenLawRecommend =    TopTenLawRecommend
        )
class UploadFile(models.Model):
    file = models.FileField(upload_to='mainapp/media')
    def __str__(self):
        return self.file


    # Create your models here.
