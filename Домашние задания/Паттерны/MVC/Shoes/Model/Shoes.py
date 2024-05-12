import json


class Shoes:
    SHOES_DATA_PATH = "shoes_data.json"
    SHOES_STRUCTURE = {
        "gender_type": ("мужская", "женская"),
        "type": "",
        "color": "",
        "price": "",
        "manufactor": "",
        "size": "",
    }

    def __init__(self):
        self.shoes_data = list()
        try:
            with open(self.SHOES_DATA_PATH, "r", encoding="utf-8") as file:
                self.shoes_data = json.load(file)
        except:
            pass

    def save_data(self, data):
        with open(self.SHOES_DATA_PATH, "w", encoding="utf-8") as file:
            self.shoes_data.append(data)
            json.dump(self.shoes_data, file, indent=3, ensure_ascii=False)

    def load_data(self):
        try:
            with open(self.SHOES_DATA_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
                print(json.dumps(data, indent=3, ensure_ascii=False))
        except:
            print("Ошибка при чтении файла либо он не существует.")
