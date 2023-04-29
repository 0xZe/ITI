from project import menu
from view_projects import view
import json


def delete(user_id):
    view(user_id)

    project_name = input('\nSelect one projct to delete : ')

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    # search for poject name and remove and update json file
    for dict in list:
        if dict['title'] == project_name:
            list.remove(dict)
            # update in json file
            projects = open("projects_data.json", "w")
            for add_dict in list:
                json.dump(add_dict, projects)
                projects.write("\n")
            projects.close()

            print("\ndelete project successfully")
            break
    else:
        print("this project name is n't exist ,, please try again")
        delete(user_id)
