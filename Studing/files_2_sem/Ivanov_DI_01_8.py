class Thing:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def put(self, item):
        self.contents.append(item.name)

    def take(self, item_name):
        if item_name in self.contents:
            self.contents.remove(item_name)
        else:
            print(f"{item_name} not found in {self.name}")

class Refrigerator(Thing):
    def __init__(self):
        super().__init__("Refrigerator")

    def put(self, item):
        if item.is_edible:
            super().put(item)
        else:
            print(f"{item.name} is not edible, cannot put in refrigerator")

class BedsideTable(Thing):
    def __init__(self):
        super().__init__("Bedside Table")

    def put(self, item):
        if item.is_writing_material:
            super().put(item)
        else:
            print(f"{item.name} is not writing material, cannot put in bedside table")

class Closet(Thing):
    def __init__(self):
        super().__init__("Closet")

    def put(self, item):
        if item.is_clothes:
            super().put(item)
        else:
            print(f"{item.name} is not clothes, cannot put in closet")

class Item:
    def __init__(self, name, is_edible=False, is_writing_material=False, is_clothes=False):
        self.name = name
        self.is_edible = is_edible
        self.is_writing_material = is_writing_material
        self.is_clothes = is_clothes

scissors = Item("Scissors", is_writing_material=True)
book = Item("Book", is_writing_material=True)
pencil = Item("Pencil", is_writing_material=True)
apple = Item("Apple", is_edible=True)
shirt = Item("Shirt", is_clothes=True)

refrigerator = Refrigerator()
bedside_table = BedsideTable()
closet = Closet()

refrigerator.put(apple)
bedside_table.put(scissors)
bedside_table.put(book)
bedside_table.put(pencil)
closet.put(shirt)
closet.take(shirt)

print("In the refrigerator:", refrigerator.contents)
print("In the bedside table:", bedside_table.contents)
print("In the closet:", closet.contents)