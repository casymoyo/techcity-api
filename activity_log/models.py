# from django.db import models
# from store_app.models import Store
# from django.contrib.auth.models import User

# activity_choices = [
#     ('sale', 'sale'),
#     ('transfer', 'transfer'),
#     ('delete', 'delete'),
#     ('return', 'return')
# ]

# class Activity(models.Model):
#     type = models.CharField( choices=activity_choices, max_length=50)
#     description = models.CharField(max_length=255)
#     date_created = models.DateField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     store = models.ForeignKey(Store, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return f'{self.user.username} ->( {self.type} : {self.description})'


    