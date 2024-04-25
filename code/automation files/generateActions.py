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
    "BATNA": ["Dates"       ],

    "BISKRA": ["Tomatoes", "Greenpepper", "Dates", "Wheat", "Aubergine"  ],

    "BLIDA": ["Potatoes", "Greenpepper", "Wheat", "Aubergine"          ],
    "BOUIRA": ["Potatoes", "Wheat"],
  
    "TEBESSA": ["Potatoes", "Dates"],
    "TLEMCEN": ["Tomatoes"     ],
    "TIARET": ["Potatoes"    , "Aubergine"],

    "ALGER": ["Potatoes", "Tomatoes"             ],
    "DJELFA": ["Dates"    ],
    "JIJEL": ["Tomatoes", "Greenpepper", "Corn"      ],
    "SETIF": ["Greenpepper"],
    "SAIDA": ["Aubergine"],
    "SKIKDA": ["Corn" ],
    "S.B.ABBES": ["Corn"  ],
    "ANNABA": ["Potatoes", "Wheat"   ],
    "GUELMA": ["Wheat"     ],
    "CONSTANTINE": ["Wheat"     ],

    "MOSTAGANEM": ["Tomatoes", "Greenpepper"         , "Aubergine"     ],
    "M'SILA": ["Greenpepper"     , "Aubergine"],
   
    "OUARGLA": ["Greenpepper", "Wheat", "Dates"],

    "EL-BAYADH": ["Corn", "Dates"    , "Aubergine"],


  
    "EL-TARF": ["Potatoes"   ],
    "TINDOUF": ["Tomatoes", "Greenpepper", "Aubergine"],

    "EL-OUED": ["Potatoes", "Tomatoes", "Greenpepper", "Dates"],
    "KHENCHELA": ["Dates", "Aubergine"     ],

    "TIPAZA": ["Tomatoes", "Greenpepper"             ],
    "MILA": ["Potatoes", "Wheat"     , "Aubergine"],
    "AIN-DEFLA": ["Potatoes", "Tomatoes"         ],

    "GHARDAIA": ["Dates"],

}

for city, product in algerian_crops.items():
    for crop in product:
        for c in conditions:
            print('["',crop,'",','"',c,'",','"',city,'"],');

        





                
