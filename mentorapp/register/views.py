from django.shortcuts import render, redirect
from .forms import StudentRegisterForm, MentorRegisterForm
from app_user.models import User, Profile, School, Major, Company, Industry, Request #, UserSchool, UserMajor, UserCompany, UserIndustry, UserRequest, Connection, CompanyIndustry


def register(request):
    return render(request, "register/register.html")


def student_register(request):
    if request.method == "POST":
        student_form = StudentRegisterForm(request.POST)
        if student_form.is_valid():
            user = student_form.save(commit=False)
            user.is_student = True
            user.save()
            school = School.objects.create(name=student_form.cleaned_data["school"])
            major = Major.objects.create(name=student_form.cleaned_data["major"])
            if student_form.cleaned_data["industry"] != None:
                industry = Industry.objects.create(name=student_form.cleaned_data["industry"])
                user.industries.add(industry)
            user.schools.add(school)
            user.majors.add(major)
            user.save()
            user_profile = Profile.objects.create(user=user)
            user_profile.save()
            redirect("profile/profile.html")
    else:
        student_form = StudentRegisterForm()
    return render(request, "register/student_register.html", {"student_form": student_form})


def mentor_register(request):
    if request.method == "POST":
        mentor_form = MentorRegisterForm(request.POST)
        if mentor_form.is_valid():
            user = mentor_form.save(commit=False)
            user.is_mentor = True
            user.save()
            if mentor_form.cleaned_data["school"] != None:
                school = School.objects.create(name=mentor_form.cleaned_data["school"])
                user.schools.add(school)
            if mentor_form.cleaned_data["major"] != None:
                major = Major.objects.create(name=mentor_form.cleaned_data["major"])
                user.majors.add(major)
            industry = Industry.objects.create(name=mentor_form.cleaned_data["industry"])
            company = Company.objects.create(name=mentor_form.cleaned_data["company"])
            user.industries.add(industry)
            user.companies.add(company)
            user.save()
            user_profile = Profile.objects.create(user=user)
            user_profile.save()
            redirect("profile/profile.html")
    else:
        mentor_form = MentorRegisterForm()
    return render(request, "register/mentor_register.html", {"mentor_form": mentor_form})


# from django.shortcuts import render, redirect
# from .forms import RegisterForm, StudentMentorForm
#
#
# def student_register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         student_mentor_form = StudentMentorForm(request.POST)
#         if form.is_valid() and student_mentor_form.is_valid():
#             user = form.save()
#
#             # app_user = user_app_form.save(commit=False)
#             # app_user.user = user
#             # app_user.is_student = user_app_form.cleaned_data["student"]
#             # app_user.is_mentor = user_app_form.cleaned_data["mentor"]
#             # app_user.save()
#
#             if student_mentor_form.cleaned_data["student"] == True:
#                 student = student_form.save(commit=False)
#                 student.user = user
#                 student.save()
#
#             if mentor_form.cleaned_data["mentor"] == True:
#                 mentor = mentor_form.save(commit=False)
#                 mentor.user = user
#                 mentor.save()
#             # username = form.cleaned_data["username"]
#             # first_name = form.cleaned_data["first_name"]
#             # last_name = form.cleaned_data["last_name"]
#             # email = form.cleaned_data["email"]
#             #
#             # student = user_app_form.cleaned_data["student"]
#             # mentor = user_app_form.cleaned_data["mentor"]
#
#             # newUser = User.objects.create(username= form_username, first_name=form_first_name, last_name=form_last_name, email_address=form_email, is_student=form_student, is_mentor=form_mentor)
#             # newUser.save()
#             # form.save() # this will save the app_user in the app_user database
#         # return redirect("/home") -- will redirect to home page when we create it
#     else:
#         form = RegisterForm()
#         student_form = StudentForm()
#         mentor_form = MentorForm()
#     return render(request, "register/register.html", {"form":form, "student_form": student_form, "mentor_form": mentor_form})
