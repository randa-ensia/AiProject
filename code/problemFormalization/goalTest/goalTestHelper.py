def calcTotalProduction(state):
 total_production = {product: 0 for product in state['wilayas']['ADRAR']['Products']}#it is a dict of production for all the products
 for wilaya in state['wilayas'].values():
     for product, details in wilaya['Products'].items():#looping over the products of each wilaya
         total_production[product] += details['production']#calculate the total production of a product for all wilayas
         
 # print("Total production of each product:") ==> this is for testing !
 # for product, production in total_production.items():
        #     print(f"{product}: {production}")    
 return total_production