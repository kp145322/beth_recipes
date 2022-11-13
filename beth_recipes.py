#print welcome message
#all ASCII art in this program created with patorjk.com ASCII art generator and Crawford2 font

print('''\
 __    __   ___ _        __  ___  ___ ___   ___      ______  ___       ____    ___ ______ __ __ __  _____     ____    ___    __ ____ ____   ___ _____
|  |__|  | /  _] |      /  ]/   \|   |   | /  _]    |      |/   \     |    \  /  _]      |  |  |  |/ ___/    |    \  /  _]  /  ]    |    \ /  _] ___/
|  |  |  |/  [_| |     /  /|     | _   _ |/  [_     |      |     |    |  o  )/  [_|      |  |  |_ (   \_     |  D  )/  [_  /  / |  ||  o  )  [(   \_
|  |  |  |    _] |___ /  / |  O  |  \_/  |    _]    |_|  |_|  O  |    |     |    _]_|  |_|  _  | \|\__  |    |    /|    _]/  /  |  ||   _/    _]__  |
|  `  '  |   [_|     /   \_|     |   |   |   [_       |  | |     |    |  O  |   [_  |  | |  |  |   /  \ |    |    \|   [_/   \_ |  ||  | |   [_/  \ |
 \      /|     |     \     |     |   |   |     |      |  | |     |    |     |     | |  | |  |  |   \    |    |  .  \     \     ||  ||  | |     \    |
  \_/\_/ |_____|_____|\____|\___/|___|___|_____|      |__|  \___/     |_____|_____| |__| |__|__|    \___|    |__|\_|_____|\____|____|__| |_____|\___|
                                                                                                                                                      \

''')

print('\nThis program will help you select recipes and add ingredients to your shopping list.\n\n\
Let\'s get started!')

# create empty shopping list
shopping_list = []

# define function to add ingredients to list
def add_to_list(ingredient_list):
  local_shopping_list = []
  for i in ingredient_list:
    add_yes_or_no = input('\nDo you need ' + i + '? Answer y or n.\n')
    if add_yes_or_no == 'y':
      print('Adding ' + str(i) +' to shopping list...')
      local_shopping_list += [i]
    else:
      print('\nOk, next item...')
  print('\nHere is your shopping list:')
  for i in local_shopping_list:
    print(i)
  print('\nAdding items to your master shopping list...')
  shopping_list.extend(local_shopping_list)


# define function to pick a recipe
def pick_recipe():

## choose protein
  choose_protein = input('\nWhat protein base would you like? Options are chicken, beef, pork, lamb, or veggie.\n')

## chicken options
  if choose_protein == 'chicken':

### choose chicken recipe
      choose_chicken_recipe = input('\nChicken sounds great! Here are your recipe options. Enter the number of the recipe \
(e.g. enter 1 for baked pesto mushroom chicken.)\n 1: baked pesto mushroom chicken\n 2: chicken potpie\n \
3: pesto chicken with penne pasta\n 4: white chicken chili\n 5: Moroccan in minutes\n')

### chicken recipe 1
      if choose_chicken_recipe == '1':
        print('\nBaked pesto mushroom chicken! Great choice.')
        baked_pesto_ingredients = ['chicken breasts (4)', 'mayo (1/4 cup)', 'pesto (1 T)',\
        'portobello mushroom caps (4)', 'mozzarella cheese (4 slices)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in baked_pesto_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(baked_pesto_ingredients)
### chicken recipe 2
      elif choose_chicken_recipe == '2':
        print('\nChicken Pot Pie! Great choice.')
        chicken_pot_pie_ingredients = ['diced peeled potatoes (2 c)', 'sliced carrots (2 c)', 'chopped onion (2/3 c)',\
        'butter (1 c)', 'all purpose flour (1 c)', 'salt (1 3/4 t)', 'dried thyme (1 t)', 'pepper (3/4 t)', 'chicken broth (3 c)', 'milk (1 1/2 c)',\
        'cubed cooked chicken (4 c)', 'frozen peas (1 c)', 'frozen corn (1 c)', '9 inch double crust pie pastry']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in chicken_pot_pie_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(chicken_pot_pie_ingredients)
### chicken recipe 3
      elif choose_chicken_recipe == '3':
        print('\nMmm pesto chicken with penne pasta! My favorite ^^.')
        pesto_chicken_ingredients = ['olive oil (1 t)', 'chicken breast (1 lb)', 'green onion, sliced (4)',\
        'artichoke hearts (1 x 13.75 oz can)', 'basil pesto (4 T)', 'sour cream (4 T)', 'penne pasta (8 oz)', 'parmesan cheese (4 T)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in pesto_chicken_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(pesto_chicken_ingredients)
### chicken recipe 4
      elif choose_chicken_recipe == '4':
        print('\nWhite Chicken Chili it is:')
        pesto_chicken_ingredients = ['olive oil (1 T)', 'onion, medium, chopped (1)', 'chopped green chilies (1 x 4 oz can)',\
        'all purpose flour (3 T)', 'ground cumin (2 t)', 'Beans, Bush\'s Great Northern (2 x 15.8 oz cans)', 'chicken broth (14.5 oz)', \
        'chicken breast (1 1/2 c)', 'monterey jack cheese, shredded (for topping)', 'sour ceam (for topping)', 'salsa (for topping)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in pesto_chicken_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(pesto_chicken_ingredients)
### chicken recipe 5
      elif choose_chicken_recipe == '5':
        print('\nMoroccan in minutes, nice choice.')
        moroccan_ingredients = ['chicken thighs, boneless, skinless (1 lb)', 'couscous (1 c)', 'currants or yellow raisins (1/4 c)',\
        'almonds, slivered, toasted (1/4 c)', 'chicken broth (14.5 oz)', 'diced tomatoes (1 x 14.5 oz can)', 'butter, unsalted (4 T)'\
        'onion, diced (1)', 'paprika (2 t)', 'ground cumin (2 t)', 'kosher salt (1 t)', 'ground cinnamon (1/4 t)',\
        'curry powder (1/4 unknown quantity)', 'cayenne (1/8 t)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in moroccan_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(moroccan_ingredients)
      else:
        print('I don\'t understand. Let\'s continue...')

## beef options
  elif choose_protein == 'beef':

### choose beef recipe
      choose_beef_recipe = input('\nBeef! It\'s what\'s been chosen for dinner.  Here are your recipe options. Enter the number of the recipe\
      (e.g. enter 1 for beefy beens and rice.)\n 1: beefy beans and rice\n 2: beef burritos\n 3: mom\'s spaghetti\n 4. thing Trevor likes\n 5: shepherd\'s pie\n')

### beef recipe 1
      if choose_beef_recipe == '1':
        print('\nBeefy beans and rice, sounds very nice!')
        beefy_beans_ingredients = ['ground beef (1 lb)', 'bratwurst (2)', 'onion, small, chopped (1)', 'green pepper (1)', 'salt (1 t)',\
        'pork-n-beans (2 x 16 oz cans)', 'catsup (1/2 c)', 'worcestershire sauce (1 t)', 'brown rice, riceland natural (2 c when cooked)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in beefy_beans_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(beefy_beans_ingredients)
### beef recipe 2
      elif choose_beef_recipe == '2':
        print('\nBeef burritos! Me encanta.')
        beef_burritos_ingredients = ['tortillas (8)', 'ground beef (1 lb)', 'onion, medium (1/2 c chopped)', 'refried beans', 'chili powder (2 T)',\
        'salt (1 t)', 'ground cumin (1/2 t)', 'garlic (2 cloves)', 'taco sauce', 'sour cream', 'shredded cheese', 'lettuce']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in beef_burritos_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(beef_burritos_ingredients)
### beef recipe 3
      elif choose_beef_recipe == '3':
        print('\nMom\'s spaghetti, nice pick. Try not to LOSE YOURSELF in the flavor.')
        spaghetti_ingredients = ['ground beef (2 lbs)', 'onion (3 c)', 'garlic (6 cloves)', 'spaghetti noodles', 'Hunt\'s tomato sauce (60 oz)',\
        'parsley (3/4 c fresh OR 3 T dried)', 'brown sugar (2 T)', 'salt (1 T)', 'oregano (1 1/2 T)', 'thyme (3/4 t)', 'bay leaves (3)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in spaghetti_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(spaghetti_ingredients)
### beef recipe 4
      elif choose_beef_recipe == '4':
        print('\nThing Trevor likes, yum!')
        trevor_likes_ingredients = ['ground beef (1 lb)', 'spaghetti noodles (1 lb dry)', 'olive oil (2 T)', 'buttom mushrooms, sliced (1 lb)',\
        'kosher salt (1 t)', 'black pepper (1/4 t)', 'diced tomatoes (1 x 14.5 oz can)', 'heavy cream (1 c)', 'grated parmesan (1 c)',\
        'fresh flat-leaf parsley, roughly chopped (1/2 c)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in trevor_likes_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(trevor_likes_ingredients)
### beef recipe 5
      elif choose_beef_recipe == '5':
        print('\nSheperd\'s pie! Let\'s get pastoral.')
        shepherd_ingredients = ['ground beef, grass fed (1 1/2 lbs)', 'peas and carrots (10 oz)', 'mashed potatoes, Yoder\'s (1 package',\
        'onion, chopped (1)', 'all purpose flour (2 T)', 'ketchup (2 T)', 'worcestershire sauce (1 T)', 'beef broth (3/4 c)',\
        'shredded cheddar (1/4 c)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in shepherd_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(shepherd_ingredients)
      else:
        print('I don\'t understand. Let\'s continue...')


## pork options
  elif choose_protein == 'pork':

### choose pork recipe
      choose_pork_recipe = input('\nPork! Let\'s prepare a plate of porcine provisions. Here are your recipe options. Enter the number of the recipe\
      (e.g. enter 1 for big game chili.)\n 1: big game chili\n 2: cowboy sausage and beans\n 3: Grandma Gerri\'s tortellini soup\n 4. jazzy jambalaya\n')

### pork recipe 1
      if choose_pork_recipe == '1':
        print('\nBig game chili! A cheesehead favorite.')
        chili_ingredients = ['Italinan sausage (1 lb)', 'onion, medium, chopped (1)', 'bell pepper, chopped (1)', 'diced tomatoes (1 x 28 oz can)', \
        'tomato sauce (1 x 29 oz can)', 'kidney beans (1 x 27 oz can)', 'black beans (1 x 15 oz can)', 'worcestershire sauce (1 T)', \
        'chili poweder (1 1/2 T)', 'ground cinammon (1 t)', 'Top the Tater OR other chip dip (1 c)', 'shredded cheddar (1/2 c)', \
        'green onion, sliced (1/2 c)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in chili_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(chili_ingredients)
### pork recipe 2
      elif choose_pork_recipe == '2':
        print('\nGiddyup! We\'re puttin\' on a pot of cowboy sausage and beans!')
        cowboy_ingredients = ['Johnsonville Polish kielbasa (1 x 13.5 oz pack)', 'onion, small, chopped (1)', 'canola oil (1 T)', \
        'potatoes, peeled and cubed (3)', 'baked beans (1 x 20 oz can)', 'chicken broth (1 c)', 'salsa (1 c)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in cowboy_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(cowboy_ingredients)
### pork recipe 3
      elif choose_pork_recipe == '3':
        print('\nGrandma Gerri\'s tortellini soup. Prepare to be satisfied.')
        tortellini_ingredients = ['Italian sausage (1 lb)', 'carrots, sliced (1 c)', 'zucchini, sliced (1 1/2 c)', 'onion, chopped (1 c)', \
        'garlic, thinly sliced (2 cloves)', 'beef broth (5 c)', 'tortellini, frozen (8 oz)', 'red wine (1/2 c)', 'basil (1/2 t)', \
        'oregano (1/2 t)', 'tomato sauce (8 oz)', 'tomatoes, chopped (1 can)', 'green pepper, chopped in 1/2 inch pieces (1)', \
        'parsley, chopped (3 T)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in tortellini_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(tortellini_ingredients)
### pork recipe 4
      elif choose_pork_recipe == '4':
        print('\nJazzy jambalaya. Account for a 20% kielbasa mining rate.')
        jambalaya_ingredients = ['kielbasa, sliced thin (14 oz)', 'chicken breast, chunked (1)', 'vegetable oil (2 T)', 'flour (2 T)', 'green pepper, chopped (1)', \
        'garlic, minced (1 clove)', 'v8 juice (1 1/2 c)', 'pepper (1/4 t)', 'salt (1/4 t)', 'ground red pepper (1/8 t)', 'rice']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in jambalaya_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(jambalaya_ingredients)
      else:
        print('I don\'t understand. Let\'s continue...')

## veggie options
  elif choose_protein == 'veggie':

### choose veggie recipe
      choose_veggie_recipe = input('\nVeggie. Read: cheese. Here are your recipe options. Enter the number of the recipe\
      (e.g. enter 1 for cheese souffle.)\n 1: cheese souffle\n 2: oven-roasted mushrooms and new potatoes\n 3: rice, broccoli, and feta saute\n')

### veggie recipe 1
      if choose_veggie_recipe == '1':
        print('\nCheese souffle. Commonly served for Christmas day breakfast.')
        souffle_ingredients = ['white bread (10 slices)', 'sharp cheddar, grated (1/2 lb)', 'eggs, well-beaten (8)', 'milk (4 c)',\
        'dry mustard (1 t)', 'salt (1 t)', 'paprika (1/2 t)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in souffle_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(souffle_ingredients)
### veggie recipe 2
      elif choose_veggie_recipe == '2':
        print('\nOven-roasted mushrooms and new potatoes. Why are the potatoes new, you ask? Because, they\'re better than OLD potatoes.')
        mushroom_potato_ingredients = ['potatoes, new, cut in 1/2 inch chunks (1 1/2 lbs)', 'vegatable oil (2 T)', \
        'white mushrooms, halved or quartered (1 lb)', 'red bell pepper, cut in 1/2 inch chunks (1)', 'garlic, minced (1 t)',\
        'green onions, sliced (1/2 c)', 'salt (1 t)', 'thyme, dried (1/2 t)', 'pepper (1/4 t)']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in mushroom_potato_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(mushroom_potato_ingredients)
### veggie recipe 3
      elif choose_veggie_recipe == '3':
        print('\nRice, broccoli, and feta saute. Sounds healthy, yet satisfying.')
        saute_ingredients = ['rice (1 c)', 'salt (1/2 t)', 'vegetable oil (2 t)', 'olive oil (1/4 c)', 'garlic, minced (4 cloves)',\
        'tomatoes, medium, cored seeded and diced (2)', 'broccoli, in bite-size pieces (1 bunch or 5 c)', 'oregano, dried (1/2 t)',\
        'feta cheese, crumbled (5 oz)', 'black pepper, freshly ground']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in saute_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(saute_ingredients)
      else:
        print('I don\'t understand. Let\'s continue...')


## lamb options
  elif choose_protein == 'lamb':

### choose lamb recipe
      choose_lamb_recipe = input('\nSo you\'ve chosen lamb. Here are your recipe options.\nHint: there is only one option (i.e. enter 1 for fast lamb curry)\n\
 1: fast lamb curry\n')

### lamb recipe 1
      if choose_lamb_recipe == '1':
        print('\nFast lamb curry! This is a \"runners\' thing.\" What\'s faster, the runner or the curry? I suppose that\'s a matter of persepctive.')
        curry_ingredients = ['ground lamb (1 lb)', 'curry powder (5 t)', 'marinara sauce (15 oz)', 'baby spinach, fresh, chopped (6 oz)'\
        'rice', 'naan']
        print('\nHere are the ingredients. Check your pantry and come back, then we\'ll add whatever you need to the shopping list!\n')
        for i in curry_ingredients:
          print(i)
        print('\nLet\'s add the ingredients you need to your shopping list!')
        add_to_list(curry_ingredients)
      else:
        print('I don\'t understand. Let\'s continue...')


## check if they want another recipe
  want_another = input('\nDO YOU WANT TO ADD ANOTHER RECIPE to your shopping list? Answer y or n.\n')
  if want_another == 'y':
    print('\nOk, let\'s find another recipe!')
    pick_recipe()
  elif want_another == 'n':
    print('\nOk, let\'s review and print your final shopping list.\n\nHere is your final shopping list:')
    print('''\
  _____ __ __   ___   ____  ____ ____  ____    ____      _      ____ _____ ______
 / ___/|  |  | /   \ |    \|    \    ||    \  /    |    | |    |    / ___/|      |
(   \_ |  |  ||     ||  o  )  o  )  | |  _  ||   __|    | |     |  (   \_ |      |
 \__  ||  _  ||  O  ||   _/|   _/|  | |  |  ||  |  |    | |___  |  |\__  ||_|  |_|
 /  \ ||  |  ||     ||  |  |  |  |  | |  |  ||  |_ |    |     | |  |/  \ |  |  |
 \    ||  |  ||     ||  |  |  |  |  | |  |  ||     |    |     | |  |\    |  |  |
  \___||__|__| \___/ |__|  |__| |____||__|__||___,_|    |_____||____|\___|  |__|
                                                                                  \
''')
    for i in shopping_list:
      print(i)
  else:
    print('\nI don\'t understand your input. Let\'s review and print your final shopping list.\n')
    print('''\
  _____ __ __   ___   ____  ____ ____  ____    ____      _      ____ _____ ______
 / ___/|  |  | /   \ |    \|    \    ||    \  /    |    | |    |    / ___/|      |
(   \_ |  |  ||     ||  o  )  o  )  | |  _  ||   __|    | |     |  (   \_ |      |
 \__  ||  _  ||  O  ||   _/|   _/|  | |  |  ||  |  |    | |___  |  |\__  ||_|  |_|
 /  \ ||  |  ||     ||  |  |  |  |  | |  |  ||  |_ |    |     | |  |/  \ |  |  |
 \    ||  |  ||     ||  |  |  |  |  | |  |  ||     |    |     | |  |\    |  |  |
  \___||__|__| \___/ |__|  |__| |____||__|__||___,_|    |_____||____|\___|  |__|
                                                                                  \
''')
    for i in shopping_list:
      print(i)


#check if they want a recipe
want_recipe = input('\nDo you want to find a recipe? Answer y or n.\n')

if want_recipe == 'y':
  pick_recipe()
elif want_recipe == 'n':
  print('\nOk, no recipes for you.')

#save shopping list
save_to_text = input('\nDo you want to save your shopping list to a text file? Answer y or n.\n')
if save_to_text == 'y':
  new_file = open("new_shopping_list.txt", "w")
  for item in shopping_list:
    new_file.write(item + '\n')
  new_file.close()
  print('\nYour shopping list is now saved to the file new_shopping_list in the same folder where the Beth\'s Recipes program is stored.\
\n\nHappy cooking!')
elif save_to_text == 'n':
  print('\nOk, goodbye!')
  
close_program = input('Please close this window or enter \'finish\'\n')
if close_program == 'finish':
  print('Goodbye!')
