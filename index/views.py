from django.shortcuts import render
from .models import Pages


def home(request):
    '''Returns the home page'''
    return render(request, 'index.html')


def get_page(request, page):
    '''Returns the requested page'''
    print(page)
    context = {"page_name":page}
    return render(request, 'page.html', context=context)


def teachers(request):
    '''Returns tesachers page'''
    return render(request, 'teachers.html')


def courses(request, course):
    '''Returns a course page'''
    course_object = Pages.objects.all().filter(title=course).first()
    levels = course_object.roadmap.split('\n')
    level = ""
    roadmap = {}
    for item in levels:
        if item:
            if 'Level' in item:
                level = item
                if level not in roadmap:
                    roadmap[level] = []
            else:
                roadmap[level].append(item)
    print(roadmap)
    context = {"course":course_object, "roadmap":roadmap}
    return render(request, 'courses.html', context)
