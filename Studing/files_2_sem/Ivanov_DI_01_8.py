class Thing:
    def __init__(self, name):
        self.name = name
        self.content = []

    def put(self, item):
        self.content.append(item)

    def take(self, item):
        if item in self.content:
            self.content.remove(item)
        else:
            print(f"{item} not found in {self.name}")

class Refrigerator(Thing):
    pass

class Closet(Thing):
    pass

class BedsideTable(Thing):
    pass

# Create instances of the classes
refrigerator = Refrigerator("refrigerator")
closet = Closet("closet")
bedside_table = BedsideTable("bedside table")

# Put items into the things
refrigerator.put("apple")
closet.put("scissors")
closet.put("book")
bedside_table.put("pencil")

# Take items from the things
bedside_table.take("pencil")
closet.take("scissors")
refrigerator.take("apple")