import csv
from models.dish import Dish
from models.ingredient import Ingredient


# def add_ingradients(data, dish_set):
#     for item in data:
#         for dish in list(dish_set):
#             if dish.name == item[0]:
#                 dish.add_ingredient_dependency(
#                     Ingredient(item[2]), int(item[3])
#                 )


# def get_recipes(data):
#     new_set = set()

#     for item in data:
#         if Dish(item[0], float(item[1])) not in new_set:
#             new_set.add(Dish(item[0], float(item[1])))

#     add_ingradients(data, new_set)

#     return new_set


# def csv_reader(source_path: str):
#     try:
#         with open(source_path, encoding="utf-8") as file:
#             graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
#             header, *data = graduacao_reader

#         return get_recipes(data)
#     except FileNotFoundError:
#         print("Arquivo inexistente")


# Req 3!
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.__csv_reader(source_path)

    def __csv_reader(self, source_path: str):
        try:
            with open(source_path, encoding="utf-8") as file:
                graduacao_reader = csv.reader(
                    file, delimiter=",", quotechar='"'
                )
                header, *data = graduacao_reader

            return self.__get_recipes(data)
        except FileNotFoundError:
            print("Arquivo inexistente")

    def __get_recipes(self, data):
        new_set = set()

        for item in data:
            if Dish(item[0], float(item[1])) not in new_set:
                new_set.add(Dish(item[0], float(item[1])))

        self.__add_ingradients(data, new_set)

        return new_set

    def __add_ingradients(self, data, dish_set):
        for item in data:
            for dish in list(dish_set):
                if dish.name == item[0]:
                    dish.add_ingredient_dependency(
                        Ingredient(item[2]), int(item[3])
                    )
