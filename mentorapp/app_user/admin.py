from django.contrib import admin

# Register your models here.
from .models import User, Profile, School, Major, Company, Industry, Request, Connection #, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, CompanyIndustry

admin.site.register(User)
admin.site.register(Request)
admin.site.register(School)
admin.site.register(Major)
admin.site.register(Company)
admin.site.register(Industry)
# admin.site.register(UserRequest)
# admin.site.register(UserSchool)
# admin.site.register(UserMajor)
# admin.site.register(UserCompany)
# admin.site.register(UserIndustry)
# admin.site.register(CompanyIndustry)
admin.site.register(Connection)

