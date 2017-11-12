from django.db import models
from django.utils import timezone
##from 또는 import로 시작하는 부분은 다른 파일에 있는 것을 추가하라는 뜻입니다. 
# 다시 말해, 매번 다른 파일에 있는 것을 복사&붙여넣기로 해야 하는 작업을 from이 대신 불러와 주는 거죠.

class Post(models.Model): ##모델을 정의하는 코드입니다. class (객체정의) post(모델이름) 
                          ##models은 Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 
                          #한다고 알게 됩니다.
    author = models.ForeignKey('auth.User') ##다른 모델에 대한 링크를 의미합니다.
    title = models.CharField(max_length=200) ##글자 수가 제한된 텍스트를 정의할 때 사용합니다.
    text = models.TextField() ##글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다. 
    created_date = models.DateTimeField(
            default=timezone.now) ## - 날짜와 시간을 의미합니다.
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): ##method 정의
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title