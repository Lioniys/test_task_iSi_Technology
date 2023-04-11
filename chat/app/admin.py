from django.contrib import admin
from .models import Message, Thread, ThreadUser

admin.site.register(Message)
admin.site.register(Thread)
admin.site.register(ThreadUser)