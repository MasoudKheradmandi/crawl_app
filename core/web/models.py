from django.db import models

class WebSite(models.Model):
    CRAWL_CHOICES = (
        ('crawl','crawl'),
        ('rss','rss'),
    )
    crawl_strategies = models.CharField(max_length=200,choices=CRAWL_CHOICES)
    link = models.CharField(max_length=450)
    code = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.link + "---------------------" + str(self.status)


class Post(models.Model):
    website = models.ForeignKey(WebSite,on_delete=models.CASCADE)
    title = models.TextField()
    post_link = models.URLField(db_index=True,unique=True)
    time = models.DateField(null=True)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.title + "  " + self.website.link

