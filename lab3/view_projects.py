from pathlib import Path
from project import menu
import json

def view(user_id):

    mypath = Path("/home/shimaa/PycharmProjects/Lab2/projects_data.json")
    with open('projects_data.json') as json_file:
        if mypath.stat().st_size == 0:
            print("there is no projects")
        else:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                if Dict['project_user_id'] == user_id:
                    list.append(Dict)

            if len(list) == 0:
                print("no project for you ")
                menu(user_id)
            else:
                print("your projects :")
                for dict in list:
                    print(dict['title'])


