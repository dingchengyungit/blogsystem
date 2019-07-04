from blog.models import Category
from django.contrib.auth.models import User

user = User.objects.all().first()
Category.objects.bulk_create([
    Category(name='cate%s' % i, owner=user)
    for i in range(20000)
])
