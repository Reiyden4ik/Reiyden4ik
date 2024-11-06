import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    ...  # TODO СЃС‡РёС‚Р°С‚СЊ СЃРѕРґРµСЂР¶РёРјРѕРµ csv С„Р°Р№Р»Р°

    a = open(INPUT_FILENAME, "r")
    b = open(OUTPUT_FILENAME, "w")

    reader = csv.DictReader(a)
    c = []
    for i in reader:
        c.append(i)

    ...  # TODO РЎРµСЂРёР°Р»РёР·РѕРІР°С‚СЊ РІ С„Р°Р№Р» СЃ РѕС‚СЃС‚СѓРїР°РјРё СЂР°РІРЅС‹РјРё 4

    json.dump(c, b, indent = 4)
    b.close()
    a.close()


if __name__ == '__main__':
    # РќСѓР¶РЅРѕ РґР»СЏ РїСЂРѕРІРµСЂРєРё
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")