from django.contrib import admin
from .models import Portfolio, PortfolioCategory, PortfolioDetail
# Register your models here.

admin.site.register(Portfolio)
admin.site.register(PortfolioCategory)
admin.site.register(PortfolioDetail)

