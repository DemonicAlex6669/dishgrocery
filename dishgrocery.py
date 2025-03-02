import requests
import json


def main():
    dish = input("what dish would you like to make?: ")
    url = "www.themealdb.com/api/json/v1/1/search.php?s={dish}"
    responce = requests.get(url)
    data = responce.json()

    for i in range(20):
        if data[f"strIngrediant{i}"]:
            ingrediant = data[f"strIngrediant{i}"]
            return ingrediant
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
