from django.db import models

class WebSite(models.Model):
    link = models.CharField(max_length=450)
    code = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.link + "---------------------" + str(self.status)


class Post(models.Model):
    website = models.ForeignKey(WebSite,on_delete=models.CASCADE)
    title = models.TextField()
    post_link = models.TextField()
    time = models.DateField(null=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title + "  " + self.time.day + "  " + self.website.link

