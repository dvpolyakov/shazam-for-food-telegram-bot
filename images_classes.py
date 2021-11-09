eats_classes_dict = {
    "burger": "бургер",
    "strawberry": "клубника",
    "croissant": "круассан",
    "fast food": "фаст-фуд",
    "american food": "американская еда",
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
    "pie": "пирог",
    "french fries": "картофель фри",
    "pasta": "паста",
    "khinkali": "хинкали",
    "shawarma": "шаурма",
    "barbecue": "барбекю",
    "sauce": "соус",
    "beverage": "напитки",
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
    "apple": "яблоко",
    'pringles': "чипсы Pringles"
}

not_food_classes = {
    "person": "человек",
    "bird": "птица",
    "animal": "животное",
    "car": "автомобиль",
    "plant": "растение",
    "interior": "интерьер",
    "not food": "не еда",
}

en_dishes_names, ru_dishes_names = list(eats_classes_dict.keys()), list(
    eats_classes_dict.values()
)
en_non_food_names, ru_non_food_names = list(not_food_classes.keys()), list(
    not_food_classes.values()
)
en_all_classes_list = en_dishes_names + en_non_food_names
