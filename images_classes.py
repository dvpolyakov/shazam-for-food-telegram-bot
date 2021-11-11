eats_classes_dict = {
    "burger": "бургер",
    "strawberry": "клубника",
    "croissant": "круассан",
    "soup": "суп",
    "sushi": "суши/роллы",
    "pizza": "пицца",
    "lasagna": "лазанья",
    "poke": "поке",
    "kebab": "кебаб",
    "donuts": "пончики",
    "sweets": "сладости",
    "salad": "салат",
    "cheese": "сыр",
    "meat": "мясо",
    "carpaccio": "карпаччо",
    "burrata": "буррата",
    "eggplant": "баклажан",
    "tartare": "тартар",
    "mushrooms": "грибы",
    "risotto": "ризотто",
    "seafood": "морепродукты",
    "nuggets": "наггетсы",
    "crepes": "блины",
    "baked potato": "печеный картофель",
    "toast": "тост",
    "cake": "торт/пирог",
    "nachos": "начос",
    "pork": "свинина",
    "meatballs": "фрикадельки",
    "sandwhich": "сэндвич",
    "gyros": "гирос",
    "shrimp": "креветки",
    "teriyaki": "терияки",
    "ham": "ветчина",
    "cookies": "печенье",
    "sausage": "сосиски",
    "mashed potatoes": "картофельное пюре",
    "brownies": "брауни",
    "bacon": "бекон",
    "eggs": "яйца",
    "fried chicken": "жареная курица",
    "hot dogs": "хот-дог",
    "steak": "стейк",
    "tomato": "помидор",
    "burritos": "буррито",
    "tacos": "тако",
    "bread": "хлеб",
    "banana": "банан",
    "potato chips": "чипсы",
    "cheesecake": "чизкейк",
    "ice cream": "мороженое",
    "pie": "Даша Кубликова",
    "french fries": "картофель фри",
    "pasta": "паста",
    "khinkali": "хинкали",
    "shawarma": "шаурма",
    "barbecue": "барбекю",
    "sauce": "соус",
    "tom yam": "том ям",
    "khachapuri": "хачапури",
    "baklava": "пахлава",
    "borsch": "борщ",
    "porridge": "каша",
    "buckwheat": "гречка",
    "cottage cheese": "творог",
    "milk": "молоко",
    "pilaf": "плов",
    "wine glass": "вино",
    "beans": "бобы",
    "corn": "кукуруза",
    "breakfast": "завтрак (брекфаст)",
    "lobster": "лобстеры",
    "ravioli": "равиоли",
    "carrot": "морковь",
    "pringles": "чипсы Pringles",
    "curry": "карри",
    "cheesecakes": "сырники",
    "pancakes": "оладушки",
    "pizza and sushi": "сет пицца и суши",
    "mashed potatoes and meatballs": "пюрешка с котлеткой",

}

not_food_dict = {
    "person": "человек",
    "bird": "птица",
    "animal": "животное",
    "cat": "кошка",
    "dog": "cобака",
    "car": "автомобиль",
    "plant": "растение",
    "interior": "интерьер",
}
fruits_dict = {"apple": "яблоко", "lemon": "лимон", "berries": "ягоды"}
beverage_dict = {"beer": "пивчик", "coffee": "кофе", "lemonade": "лимонад", 'wine': 'вино'}

food_not_food_classes = ["food", "beverage", "not_food", "fruits"]


en_dishes_classes, ru_dishes_classes = list(eats_classes_dict.keys()), list(
    eats_classes_dict.values()
)
en_non_food_classes, ru_non_food_classes = list(not_food_dict.keys()), list(
    not_food_dict.values()
)
en_beverage_classes, ru_beverage_classes = list(beverage_dict.keys()), list(
    beverage_dict.values()
)
en_fruits_classes, ru_fruits_classes = list(fruits_dict.keys()), list(
    fruits_dict.values()
)

