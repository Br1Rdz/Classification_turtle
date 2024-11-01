import random


def random_string():
    random_list = ["¿Puedes tu reformular tu pregunta acerca de la tortuga de tu interes, porfavor?",
                'No entendi tu pregunta',
                '......',
                #"¿Que es lo que quieres saber sobre las tortugas?",
                "¿En que puedo ayudarte?"
                ]
    
    list_count = len(random_list)
    random_item = random.randrange(list_count)
    
    return random_list[random_item]

# print(random_string())