DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # all_devs = [worker for worker in DATA if worker["language"]=="python"]
    # # all_devs = list(map(lambda worker: worker["name"] + " " + worker["language"],all_devs))
    # all_python_devs = list(filter(lambda worker: worker["language"]=="python", DATA))
    # all_python_devs = list(map(lambda worker: worker["name"] +"-"+ worker["language"] ,all_python_devs))

    # all_platzi_workers = list(filter(lambda worker: worker["organization"] =="Platzi", DATA))    
    # all_platzi_workers = list(map(lambda worker: worker["name"]  + "- " + worker["organization"], all_platzi_workers))
    
    # all_platziandpython = list (filter(lambda worker: worker["language"]=="python"  worker["organization"]=="platzi", DATA))
    # #all_platziandpython = list (filter(lambda worker: worker["language"]=="python", DATA))
    # all_platziandpython = list(map(lambda worker: worker["name"] + " - " +  worker["organization"] +" - "+ worker["language"], all_platziandpython))
    old_people = [worker["name"] for worker in DATA if worker["age"]>30]


    for worker in old_people:
        print(worker)


if __name__ == "__main__":
    run() 