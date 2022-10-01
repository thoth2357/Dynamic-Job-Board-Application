from enum import unique
from django.db import models

# Create your models here.
class Scraping_Service(models.Model):
    url_link = models.URLField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.url_link

class Filter_tag(models.Model):
    '''
    model to use for filter tagging
    '''
    tag_name = models.CharField(max_length=25, null=True, blank=True, unique=True, help_text="Tag name to use for filtering. Must be unique.")
    tag_description = models.TextField(max_length=100, null=True, blank=True)
    tag_search_company = models.CharField(max_length=100, null=True, blank=True,help_text="Companies name to search for, separated by comma (,). Leave blank if interested in Category only.")
    tag_search_category = models.CharField(max_length=100, null=True, blank=True, help_text="Categories to search for, separated by comma (,). Leave blank if interested in Company only.")
    search_url = models.URLField(max_length=200, null=True, blank=True, help_text="Automatically generated..Readonly Field can't be edited")
    def __str__(self) -> str:
        return f"{self.tag_name}"
    
    def save(self, *args, **kwargs):
        if self.tag_search_company is not None and self.tag_search_category is not None:
            self.search_url = f"?q=job_company={self.tag_search_company.replace(',','')}&category={self.tag_search_category}"
        super(Filter_tag, self).save(*args, **kwargs)