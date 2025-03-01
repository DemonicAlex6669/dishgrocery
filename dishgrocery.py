import requests
import json


main():
    url = ...
    responce = request.get(url)
    data = responce.json()

    ingrediant = ...

    for ingrediant in ingrediants:
        print(f"{ingrediant} ok? ")
        answer = input()
        if answer.lower == "yes" or "y":
            have = input("do you have this ingrediant? ")
            if have.lower == "no" or "n":
                with file("grocery.txt", mode=a) as file:
                file.write(f"{ingrediant} /n")

    add = input("would you like to add an ingrediant? ")
    while add.lower == "yes" or "y":
        with file("grocery.txt", mode=a) as file:
            more = input("new ingrediant: ")
            file.write("{more} /n")
            add = input("add another? ")


if __name__ == "__main__":
    main()
