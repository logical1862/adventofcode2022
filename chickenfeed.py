"""attempt to calculate best cost for home chicken feed blend"""



# dict{} defined as { ingredient name: [cost per pound, protein percentage] } input function converts to cost per pound
ingredient_list = {}

def test_feed_cost():
    Num_Ing = 4
    cost = 15
    bag_size = 10
    protein = 8


    for i in range(Num_Ing):
        ing_name = f'ing{i}'
        cost = cost + 2
        bag_size = bag_size + 2
        protein = protein + 2

        #get cost per pound
        cost_per_pound = cost / bag_size

        ingredient_list[ing_name] = [cost_per_pound, protein]
    return


def get_feed_cost() -> None:
    """take user input of cost per pound per ingredient"""
    # get ingredients and costs
    Num_Ing = int(input('Number of Ingredients: '))
    print('Add ingredients and cost')
    for i in range(Num_Ing):
        ing_name = input(f'\nName {i}: ')
        cost = float(input('cost: '))
        bag_size = float(input('Size of bag in pounds: '))
        protein = int(input('Percentage protein: '))

        #get cost per pound
        cost_per_pound = cost / bag_size

        ingredient_list[ing_name] = [cost_per_pound, protein]
    return

def calc_best_cost() -> None:
    for count, ingredient in enumerate(ingredient_list):
        print(count, ingredient.values()
    
    return




if __name__ == "__main__":
    print('\n\nProtein Percent Calculator\n')
    

    #get_feed_cost()
    
    test_feed_cost()

    
    print('Calculating mix.')
    calc_best_cost()
