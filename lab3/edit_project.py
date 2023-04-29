from project import menu
from view_projects import view
import json


def edit(user_id):
    view(user_id)

    project_name = input('\nSelect one projct to edit : ')

    list = []
    json_file = open('projects_data.json')
    for line in json_file:
        Dict = json.loads(line)
        list.append(Dict)

    # search for poject name
    for dict in list:
        if dict['title'] == project_name:

            print("\nYour project information:")
            print(dict)

            key_name = input('\n\nplease enter the name of key that you want to update in this project : ')

            for key in dict:
                if key == key_name:
                    key_value = input('\n\nplease enter the new value of key : ')
                    dict[key] = key_value

                    # update in json file
                    projects = open("projects_data.json", "w")
                    for add_dict in list:
                        json.dump(add_dict, projects)
                        projects.write("\n")
                    projects.close()

                    print("\nupdate project successfully")
                    break
            else:
                print("invalid key_name ,, please try again :")
                edit(user_id)

    else:
        print("this project name is n't exist ,, please try again")
        edit(user_id)
