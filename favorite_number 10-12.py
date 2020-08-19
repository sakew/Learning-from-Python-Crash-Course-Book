import json

def get_stored_number():
    filename = "favorite_number.json"

    try:
        with open("favorite_number.json") as f_obj:
            favorite_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def your_favorite_number():
    favorite_number = get_stored_number()
    if favorite_number:
        print("I know your favorite number, it is: " + str(favorite_number) + "!")
    else:
        favorite_number = input("what is your favorite number? Input here: ")
        filename = "favorite_number.json"
        with open("favorite_number.json", "w") as f_obj:
            json.dump(favorite_number, f_obj)
            print("I know your favorite number, it is: " + str(favorite_number) + "!")

your_favorite_number()