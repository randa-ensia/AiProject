"""

all the comibnitions "condition, wilaya,product"

for _ condition:
    for _ wilayas:
        for _ products of that wilaya:     
                

            _ _ _ :

            {
            addra: []
            }

"""

conditions = ['poor','average','ideal'];

products = ['Wheat','Corn','Dates','Potatoes','Tomatoes','Greenpepper','Aubergines'];

wilayas = [
    "ADRAR", "CHLEF", "LAGHOUAT", "O.E.BOUAGHI", "BATNA", "BISKRA",  
    "BLIDA", "BOUIRA",  "TEBESSA", "TLEMCEN", "TIARET", "ALGER", 
    "DJELFA", "JIJEL", "SETIF", "SAIDA", "SKIKDA", "S.B.ABBES", "ANNABA", "GUELMA", 
    "CONSTANTINE", "MOSTAGANEM", "MSILA",  "OUARGLA", 
    "EL-BAYADH", "EL-TARF", "TINDOUF", 
     "EL-OUED", "KHENCHELA",  "TIPAZA", "MILA", "AIN-DEFLA", 
    "GHARDAIA"]

algerian_crops = {
    "ADRAR": ["Corn", "Wheat"],
    "CHLEF": ["Tomatoes"            ],
    "LAGHOUAT": ["Dates", "Wheat"  ],
    "O.E.BOUAGHI": ["Corn"         ],
    "BATNA": ["Dates","Corn"       ],

    "BISKRA": ["Tomatoes", "Greenpepper", "Dates", "Wheat", "Aubergines"  ],
    "BECHAR": ["Corn"],
    "BLIDA": ["Potatoes", "Greenpepper", "Wheat", "Aubergines"          ],
    "BOUIRA": ["Potatoes", "Wheat"],
    "TAMANRASSET":["Corn"],
    "TEBESSA": ["Potatoes", "Dates"],
    "TLEMCEN": ["Tomatoes"     ],
    "TIARET": ["Potatoes"    , "Aubergines"],

    "ALGER": ["Potatoes", "Tomatoes"             ],
    "DJELFA": ["Dates"    ],
    "JIJEL": ["Tomatoes", "Greenpepper", "Corn"      ],
    "SETIF": ["Greenpepper"],
    "SAIDA": ["Aubergines"],
    "SKIKDA": ["Corn" ],
    "S.B.ABBES": ["Corn"  ],
    "ANNABA": ["Potatoes", "Wheat"   ],
    "GUELMA": ["Wheat"     ],
    "CONSTANTINE": ["Wheat"     ],
    "MEDEA":["Corn"],
    "MOSTAGANEM": ["Tomatoes", "Greenpepper"         , "Aubergines"     ],
    "MSILA": ["Greenpepper"     , "Aubergines"],
   
    "OUARGLA": ["Greenpepper", "Wheat", "Dates"],

    "EL-BAYADH": ["Corn", "Dates"    , "Aubergines"],


  
    "EL-TARF": ["Potatoes"   ],
    "TINDOUF": ["Tomatoes", "Greenpepper", "Aubergines"],

    "EL-OUED": ["Potatoes", "Tomatoes", "Greenpepper", "Dates"],
    "KHENCHELA": ["Dates", "Aubergines"     ],

    "TIPAZA": ["Tomatoes", "Greenpepper"             ],
    "MILA": ["Potatoes", "Wheat"     , "Aubergines"],
    "AIN-DEFLA": ["Potatoes", "Tomatoes"         ],

    "GHARDAIA": ["Dates"],

}

for city, product in algerian_crops.items():
    for crop in product:
        for c in conditions:
            print('["',crop,'",','"',c,'",','"',city,'"],');

        





                
