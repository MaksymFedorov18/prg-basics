with open("pets.txt", "r")as file:
    content = file.read()
    counter = len(content.split())
    print(f"{content} \nTotal words:{counter}")