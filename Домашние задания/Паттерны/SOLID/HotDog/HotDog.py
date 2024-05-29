class HotDog:
    """Класс, где описаны варианты хот-догов, их стоимосить"""
    def __init__(self):
        self.classic = {
            "title": "Классический",
            "definition": "Булочка, сосиска, кетчуп, майонез",
            "components": ["bun", "sausage", "ketchup", "mayonnaise"],
            "cost": 200
        }
        self.sonora = {
            "title": "Сонора",
            "definition": "Булочка, бекон, томаты, авокадо, майонез",
            "components": ["bun", "bacon", "tomato", "avocado", "mayonnaise"],
            "cost": 190
        }
        self.karolin = {
            "title": "Каролинский",
            "definition": "Булочка, чили, лук, капуста",
            "components": ["bun", "chili", "onion", "cabbage"],
            "cost": 150
        }