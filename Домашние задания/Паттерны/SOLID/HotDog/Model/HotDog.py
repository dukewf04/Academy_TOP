class HotDog:
    """Класс, где описаны варианты хот-догов, их стоимосить. Описано, какие можно добавлять добавки для хот-догов."""

    def __init__(self):
        self.hotdogs = [
            {
                "title": "Классический",
                "definition": "Булочка, сосиска, кетчуп, майонез",
                "components": ["bun", "sausage", "ketchup", "mayonnaise"],
                "price": 200
            },
            {
                "title": "Сонора",
                "definition": "Булочка, бекон, томаты, авокадо, майонез",
                "components": ["bun", "bacon", "tomato", "avocado", "mayonnaise"],
                "price": 190
            },
            {
                "title": "Каролинский",
                "definition": "Булочка, чили, лук, капуста",
                "components": ["bun", "chili", "onion", "cabbage"],
                "price": 150
            }
        ]

        self.dobavki = [
            {
                "title": "mayonnaise",
                "price": 10
            },
            {
                "title": "ketchup",
                "price": 15
            }
        ]