from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from app_user.models import *
from helper import parse_req_body

# Create your views here.
def connections(request):
    user = request.user
    if request.method == 'POST':
        body = parse_req_body(request.body)
        print(body)
        if body['task'] == 'edit_connection':
            if body['action'] == 'Remove':
                connection_id = int(body['connection_id'])
                Connection.objects.delete(pk=connection_id)
    if user.is_student == True:
        connections = list(Connection.objects.filter(student=user).filter(status='C'))
    elif user.is_mentor == True:
        connections = list(Connection.objects.filter(mentor=user).filter(status='C'))
    context = {'connections': connections}
    return render(request, 'connection/connections.html', context=context)


def pending(request):
    user = request.user
    if request.method == "POST":
        body = parse_req_body(request.body)
        print(body)
        if body['task'] == 'edit_connection':
            connection_id = int(body['connection_id'])
            if body['action'] == 'Decline':
                Connection.objects.delete(pk=connection_id)
            elif body['action'] == 'Accept':
                connection = Connection.objects.get(pk=connection_id)
                print(connection)
                connection.status = 'C'
                connection.save()
    if user.is_student:
        connections = Connection.objects.filter(student=user).filter(status='P').filter(request_from='M')
    elif user.is_mentor:
        connections = Connection.objects.filter(mentor=user).filter(status='P').filter(request_from='S')
    context = {'connections': connections}
    return render(request, 'connection/pending.html', context=context)

    


    # if body['action'] == 'Connect':
    #             other_user_id = int(body['other_user_id'])
    #             other_user = User.objects.get(pk=other_user_id)
    #             if user.is_student:
    #                 connection = Connection(student=user, mentor=other_user, status='P', request_from='S')
    #             else:
    #                 connection=Connection(mentor=user, student=other_user, status='P', request_from='M')