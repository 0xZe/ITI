from project import menu
from view_projects import view
import json
import time


def search(user_id):
    view(user_id)

    project_date = input('\nWrite project date (mm/dd/yyyy) : ')
    try:
        valid_date = time.strptime(project_date, '%m/%d/%Y')
        if valid_date:
            list = []
            json_file = open('projects_data.json')
            for line in json_file:
                Dict = json.loads(line)
                list.append(Dict)

            # search for poject
            for dict in list:

                if project_date == dict['start_time'] or project_date == dict['end_time']:
                    print("\nYour project information:")
                    print(dict)
                else:
                    print("this project is n't exist ,, please try again")
                    search(user_id)

        else:
            print("\nYour data is invalid ,, please enter valid data :")

    except ValueError:
        print('Invalid date!')
