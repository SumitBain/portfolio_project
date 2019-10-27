from django.db import models

# Create your blog models
#title
#pub date
#body
#images
class Blog(models.Model):
    title= models.CharField(max_length=500)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

# add the blog app to the setting


#create a migration


#migrate



#add to the admin
