from django.contrib import admin
from portfolio_app.models import User
from portfolio_app.models import Product
from portfolio_app.models import Feedback

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Feedback)

