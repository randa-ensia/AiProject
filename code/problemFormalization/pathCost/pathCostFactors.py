"""
this file contains :

*the "adjacement factors" those are scalars that will be used to calculate the cost of changing the conditions of the land we are
plating.
the "conditions" are an abstraction for all the factors that will affect the production of the crops like the
labor , the used fertilizers , the consumption of water , the type of soil , the weather of the wilaya ect...

*the "product suitability" indicates the degree of suitability of the three climates we have in Algeria with the
prodcuts we are trying to plant.
for instance the desert climate is 'Low Suitable' for plating the lemons. 
this 'suitability' will be used to determine the adjacement factor for changing the conditions to use it in the
calculating of the path cost

*the "wilaya to climate" dictionnary that indicates the climate of each wilaya so that we can get its suitability
for the products

*the "cost_per_hec* dictionnary which contains the cost of one hectar of the land. it will be used to calculate the
cost of adding/removing a land to use it for a given products

*the "fixed factors" dictionnary which contains a scalar for the cost of each condition. one may confuse the adjacement
factors with the fixed factors so here is the diffrence:

    -the adjacement factors are used to calculate the cost of changing the condition when the actions applied changed 
    condition so if we don't change the conditions we're not gonna use it
    
    -the fixed factors calculates the cost of planting with the chosen condition (wether we change it or keep it the same, planting under
    that condition will have a cost)
"""
adjustment_factors = {
    'High Suitable': {
        'poor': {'below average': 1.1,
                 'average': 1.3,
                 'above average': 1.6, 
                 'ideal': 2.1},

         'below average': {
			   'poor':0.9,
			   'average': 1.2,
               'above average': 1.5,            
               'ideal': 2.0},

         'average': {
		    'poor':0.75,
            'below average':0.83,
            'above average': 1.3, 
            'ideal': 1.8},

         'above average': {
            'poor':0.62,
            'below average':0.67,
            'average': 0.6, 
            'ideal': 1.5},
        'ideal': {
            'poor':0.47,
            'below average':0.5,
            'average': 0.55, 
            'above average': 0.66
                  }
     
    },

    
    'Medium Suitable': {
        'poor': {'below average': 1.3,
                 'average': 1.5,
                 'above average': 1.8, 
                 'ideal': 2.3},

         'below average': { 
                  'poor':0.75,
                   'average': 1.4,
                   'above average': 1.7,            
                   'ideal': 2.1},

         'average': { 
                    'poor':0.66,
                    'below average':0.71,
                    'above average': 1.5, 
                    'ideal': 2.0
                    },

         'above average': {
                   'poor':0.55,
                   'below average':0.59,
                   'average': 0.66, 
                   'ideal': 1.7
                   },
          'ideal': {
                   'poor':0.43,
                   'below average':0.47,
                   'average': 0.5, 
                   'above average': 0.58
                  },

    },
    

    'Low Suitable': {
      'poor': { 
                 'below average': 1.6,
                 'average': 1.8,
                 'above average': 2.1, 
                 'ideal': 2.6},

         'below average': {
                        'poor':0.62,
                         'average': 1.7,
                         'above average': 2.0,            
                         'ideal': 2.3},

         'average': {
                    'poor':0.56,
                    'below average':0.59,
                    'above average': 1.8, 
                    'ideal': 2.1},

         'above average': {
                   'poor':0.47,
                   'below average':0.5,
                   'average': 0.56, 
                    'ideal': 2.0
                    },
          'ideal': {
                   'poor':0.38,
                   'below average':0.43,
                   'average': 0.47, 
                   'above average': 0.5
                  }
         
    }
}

product_suitability = {
    'Continental': {
        'Wheat': 'High Suitable',
        'Corn': 'High Suitable',
        'Dates':'Low Suitable',
        'Potatoes': 'Medium Suitable',
        'Tomatoes': 'Low Suitable',
        'Greenpepper':'Low Suitable',
        'Aubergines':'Low Suitable',
        'Onions': 'High Suitable',
        'Carrots': 'High Suitable',
        'Lemon':'Medium Suitable',
        'Apple': 'High Suitable'
    },
    'Mediterranean': {
        'Wheat': 'Medium Suitable',
        'Corn': 'Medium Suitable',
        'Dates':'Medium Suitable',
        'Potatoes': 'High Suitable',
        'Tomatoes': 'High Suitable',
        'Greenpepper':'Medium Suitable',
        'Aubergines':'Medium Suitable',
        'Onions': 'Medium Suitable',
        'Carrots': 'Medium Suitable',
        'Lemon':'High Suitable',
        'Apple': 'Medium Suitable'

    },
    'Desert': {
        'Wheat': 'Low Suitable',
        'Corn': 'Low Suitable',
        'Dates':'High Suitable',
        'Potatoes': 'Low Suitable',
        'Tomatoes': 'Medium Suitable',
        'Greenpepper':'High Suitable',
        'Aubergines':'High Suitable',
        'Onions': 'Low Suitable',
        'Carrots': 'Low Suitable',
        'Lemon':'Low Suitable',
        'Apple': 'Low Suitable'
    }
}

wilaya_to_climate = {
    'ADRAR': 'Desert',
    'CHLEF': 'Mediterranean',
    'LAGHOUAT': 'Continental',
    'O.E.BOUAGHI': 'Continental',
    'BATNA': 'Continental',
    'BEJAIA': 'Mediterranean',
    'BISKRA': 'Desert',
    'BECHAR': 'Desert',
    'BLIDA': 'Mediterranean',
    'BOUIRA': 'Mediterranean',
    'TAMANRASSET': 'Desert',
    'TEBESSA': 'Continental',
    'TLEMCEN': 'Mediterranean',
    'TIARET': 'Continental',
    'TIZI-OUZOU': 'Mediterranean',
    'ALGER': 'Mediterranean',
    'DJELFA': 'Continental',
    'JIJEL': 'Mediterranean',
    'SETIF': 'Mediterranean',
    'SAIDA': 'Mediterranean',
    'SKIKDA': 'Mediterranean',
    'S.B.ABBES': 'Mediterranean',
    'ANNABA': 'Mediterranean',
    'GUELMA': 'Mediterranean',
    'CONSTANTINE': 'Mediterranean',
    'MEDEA':'Mediterranean',
    'MOSTAGANEM': 'Mediterranean',
    'MSILA': 'Continental',
    'MASCARA': 'Mediterranean',
    'OUARGLA': 'Desert',
    'ORAN': 'Mediterranean',
    'EL-BAYADH': 'Continental',
    'ILLIZI': 'Desert',
    'B.B.ARRERIDJ': 'Mediterranean',
    'BOUMERDES': 'Mediterranean',
    'EL-TARF': 'Mediterranean',
    'TINDOUF': 'Desert',
    'TISSEMSILT': 'Mediterranean',
    'EL-OUED': 'Desert',
    'KHENCHELA': 'Continental',
    'SOUK-AHRAS': 'Mediterranean',
    'TIPAZA': 'Mediterranean',
    'MILA': 'Mediterranean',
    'AIN-DEFLA': 'Mediterranean',
    'NAAMA': 'Continental',
    'A.TEMOUCHENT': 'Mediterranean',
    'GHARDAIA': 'Desert',
    'RELIZANE': 'Mediterranean',
    
}

cost_per_hec={
       'Wheat': 1608,
        'Corn': 2194 ,
        'Dates':3200,
        'Potatoes': 5000,
        'Tomatoes': 4940 ,
        'Greenpepper':8750,
        'Aubergines':12500 ,
        'Onions': 5307,
        'Carrots': 12018,
        'Lemon':10000,
        'Apple': 15000

}

fixed_factors = {
    'poor': 1.2,  # poor means a bad productivity means the material,fertilizer ...   are not that expensive
    'below average': 1.6,  
    'average': 2.0, 
    'above average': 2.4, 
    'ideal': 2.8 
}  

#At first i thought about using a dictionary that has all the conditions and not only ideal 
max_idealproductivity = {
        'Wheat':90,
        'Corn': 150 ,
        'Dates':180,
        'Potatoes': 500,
        'Tomatoes': 1000 ,
        'Greenpepper':500,
        'Aubergines':600 ,
        'Onions': 600,
        'Carrots': 1000,
        'Lemon':500,
        'Apple': 500
}
