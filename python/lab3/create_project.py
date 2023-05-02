import json
from math import *
import time
from pathlib import Path
from project import menu


def create(user_id):

    title = input("Title : ")
    details = input("Details : ")
    total_target = input("Total target : ")
    start_time = input("Start Date (mm/dd/yyyy) : ")
    end_time = input("End Date (mm/dd/yyyy) : ")

    list_data = {'project_user_id': user_id,'title': title, 'details': details , 'total_target': total_target, 'start_time': start_time,
             'end_time': end_time}

    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')

        if valid_date1 and valid_date2:

            mypath = Path("/home/shimaa/PycharmProjects/Lab2/projects_data.json")
            with open('projects_data.json') as json_file:

                if mypath.stat().st_size == 0:
                    projects = open("projects_data.json", "a")
                    json.dump(list_data, projects)
                    projects.write("\n")
                    projects.close()

                # search for poject name if it is already exist or no
                else:
                    list = []
                    for line in json_file:
                        Dict = json.loads(line)
                        list.append(Dict)
                    for dict in list:
                        if title == dict['title'] and dict['project_user_id'] == user_id:
                            print("\nthis project name is already exit ,, please try again")
                            create(user_id)
                    else :
                        projects = open("projects_data.json", "a")
                        json.dump(list_data, projects)
                        projects.write("\n")
                        projects.close()

            print('Your project is created successfully')
        else:
            print("\nYour data is invalid ,, please enter valid data :")
            create(user_id)

    except ValueError:
        print('Invalid date!')
        create(user_id)





