"""
This file can be used to automate error detection in the conditions data of the initial state

to use it paste your part of code inside of the stateionnary 
the output will be the wilaya of the error + the type of the error
"""

state = {
    'wilayas':{
       'ADRAR':{
            'Products':{
                'Wheat':{
                    'lands_surface':17264,
                    'production': 691593,
                    'condition':'Above average',
                    'productivity':37.6,
                },
                'Corn':{
                    'lands_surface':1262,
                    'production': 38786,
                    'condition':'Below average',
                    'productivity':30.7,
                },
                'Dates':{
                    'lands_surface':28320,
                    'production': 934562,
                    'condition':'Below average',
                    'productivity':33.1,
                },
                'Potatoes':{
                    'lands_surface':411,
                    'production': 80204,
                    'condition':'Below average',
                    'productivity':195.0,
                },
                'Tomatoes':{
                    'lands_surface':672,
                    'production': 170114,
                    'condition':'Below average',
                    'productivity':253.2,
                },
                'Greenpepper':{
                    'lands_surface':30,
                    'production': 4574,
                    'condition':'Below average',
                    'productivity':150.7,
                },
                'Aubergines':{
                    'lands_surface':79,
                    'production': 8589,
                    'condition':'Below average',
                    'productivity':108.3,
                },
                'Onions':{
                    'lands_surface':713,
                    'production': 85560,
                    'condition':'Below average',
                    'productivity':120,
                },
                'Carrots':{
                    'lands_surface':648,
                    'production': 74607,
                    'condition':'Poor',
                    'productivity':115.2,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Apple':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                }
            },
            'Land_data':{
                'cultivated land':53562,
                'terre_au_repo':1948,
                'unused land':464748
            }
        },
        'CHLEF':{
            'Products':{
                'Wheat':{
                    'lands_surface':74486,
                    'production': 1817492,
                    'condition':'Average',
                    'productivity':24,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':4193,
                    'production': 1262540,
                    'condition':'Above average',
                    'productivity':301.1,
                },
                'Tomatoes':{
                    'lands_surface':587,
                    'production': 372424,
                    'condition':'Above average',
                    'productivity':634.2,
                },
                'Greenpepper':{
                    'lands_surface':102,
                    'production': 21354,
                    'condition':'Average',
                    'productivity':209.8,
                },
                'Aubergines':{
                    'lands_surface':19,
                    'production': 9315 ,
                    'condition':'Ideal',
                    'productivity':490.3,
                },
                'Onions':{
                    'lands_surface':252,
                    'production': 113600,
                    'condition':'Ideal',
                    'productivity':450.8,
                },
                'Carrots':{
                    'lands_surface':59,
                    'production': 24500,
                    'condition':'Average',
                    'productivity':415.3,
                },
                'Lemon':{
                    'lands_surface':60,
                    'production': 12775,
                    'condition':'Average',
                    'productivity':214.7,
                },
                'Olive':{
                    'lands_surface':4718,
                    'production': 77496,
                    'condition':'Below average',
                    'productivity':12.4,
                },
                'Apple':{
                    'lands_surface':275,
                    'production': 32880,
                    'condition':'Below average',
                    'productivity':119.8,
                }
            },
            'Land_data':{
                'cultivated land':152242,
                'terre_au_repo':50988,
                'unused land':33567
            }
        },
        'LAGHOUAT':{
            'Products':{
                'Wheat':{
                    'lands_surface':8231,
                    'production': 181754,
                    'condition':'Average',
                    'productivity':31.9,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':265,
                    'production': 13207,
                    'condition':'Average',
                    'productivity':41,
                },
                'Potatoes':{
                    'lands_surface':3045,
                    'production': 861350,
                    'condition':'Average',
                    'productivity':282.9,
                },
                'Tomatoes':{
                    'lands_surface':350,
                    'production': 112500,
                    'condition':'Below average',
                    'productivity':321.4,
                },
                'Greenpepper':{
                    'lands_surface':331,
                    'production': 99300,
                    'condition':'Average',
                    'productivity':300.0,
                },
                'Aubergines':{
                    'lands_surface':19,
                    'production': 9315 ,
                    'condition':'Ideal',
                    'productivity':490.3,
                },
                'Onions':{
                    'lands_surface':1080,
                    'production': 258500,
                    'condition':'Average',
                    'productivity':239.4,
                },
                'Carrots':{
                    'lands_surface':721,
                    'production': 151410,
                    'condition':'Below average',
                    'productivity':210.0,
                },
                'Lemon':{
                    'lands_surface':4,
                    'production':240,
                    'condition':'Poor',
                    'productivity':60,
                },
                'Olive':{
                    'lands_surface':2277,
                    'production': 54100,
                    'condition':'Average',
                    'productivity':25.0,
                },
                'Apple':{
                    'lands_surface':576,
                    'production': 13248,
                    'condition':'Poor',
                    'productivity':23,
                }
            },
            'Land_data':{
                'cultivated land':50464,
                'terre_au_repo':27268,
                'unused land':0
            }
        },
        'O.E.BOUAGHI':{
            'Products':{
                'Wheat':{
                    'lands_surface':108000,
                    'production': 1212000,
                    'condition':'Below average',
                    'productivity':17,
                },
                'Corn':{
                    'lands_surface':38,
                    'production': 1632,
                    'condition':'Average',
                    'productivity':42.9,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':200,
                    'production': 52300,
                    'condition':'Average',
                    'productivity':261.5,
                },
                'Tomatoes':{
                    'lands_surface':200,
                    'production': 60000,
                    'condition':'Below average',
                    'productivity':300.0,
                },
                'Greenpepper':{
                    'lands_surface':239,
                    'production': 47800,
                    'condition':'Below average',
                    'productivity':200,
                },
                'Aubergines':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Onions':{
                    'lands_surface':200,
                    'production': 90250,
                    'condition':'Ideal',
                    'productivity':451.3,
                },
                'Carrots':{
                    'lands_surface':526,
                    'production': 158560,
                    'condition':'Below average',
                    'productivity':301.4,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':2073,
                    'production': 19277,
                    'condition':'Below average',
                    'productivity':12.4,
                },
                'Apple':{
                    'lands_surface':305,
                    'production': 17272,
                    'condition':'Poor',
                    'productivity':68,
                }
            },
            'Land_data':{
                'cultivated land':237923,
                'terre_au_repo':122962,
                'unused land':32325 
            }
        },
        'BATNA':{
            'Products':{
                'Wheat':{
                    'lands_surface':86899,
                    'production': 1421160,
                    'condition':'Below average',
                    'productivity':17.6,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':207,
                    'production': 16743,
                    'condition':'Above average',
                    'productivity':65.4,
                },
                'Potatoes':{
                    'lands_surface':1239,
                    'production': 368890,
                    'condition':'Average',
                    'productivity':297.8,
                },
                'Tomatoes':{
                    'lands_surface':280,
                    'production': 61140,
                    'condition':'Below average',
                    'productivity':218.2,
                },
                'Greenpepper':{
                    'lands_surface':211,
                    'production':34517,
                    'condition':'Below average',
                    'productivity':163.5,
                },
                'Aubergines':{
                    'lands_surface':88,
                    'production': 16160,
                    'condition':'Below average',
                    'productivity':183.6,
                },
                'Onions':{
                    'lands_surface':785,
                    'production': 151180,
                    'condition':'Below average',
                    'productivity':192.6,
                },
                'Carrots':{
                    'lands_surface':404,
                    'production': 79950,
                    'condition':'Poor',
                    'productivity':197.9,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':11855,
                    'production': 455945,
                    'condition':'Average',
                    'productivity':26,
                },
                'Apple':{
                    'lands_surface':4681,
                    'production': 1207214,
                    'condition':'Above average',
                    'productivity':303.8,
                }
            },
            'Land_data':{
                'cultivated land':229283,
                'terre_au_repo':193394,
                'unused land':83749 
            }
        },
        'BEJAIA':{
            'Products':{
                'Wheat':{
                    'lands_surface':5749,
                    'production': 129744,
                    'condition':'Average',
                    'productivity':25,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':170,
                    'production': 36590,
                    'condition':'Average',
                    'productivity':214.9,
                },
                'Tomatoes':{
                    'lands_surface':335,
                    'production': 84885,
                    'condition':'Below average',
                    'productivity':253.1,
                },
                'Greenpepper':{
                    'lands_surface':204,
                    'production':29374,
                    'condition':'Below average',
                    'productivity':144,
                },
                'Aubergines':{
                    'lands_surface':26,
                    'production': 3485,
                    'condition':'Below average',
                    'productivity':132.8,
                },
                'Onions':{
                    'lands_surface':572,
                    'production': 81153,
                    'condition':'Below average',
                    'productivity':141.8,
                },
                'Carrots':{
                    'lands_surface':5,
                    'production': 1288,
                    'condition':'Below average',
                    'productivity':245.2,
                },
                'Lemon':{
                    'lands_surface':57,
                    'production': 8176,
                    'condition':'Below average',
                    'productivity':162.7,
                },
                'Olive':{
                    'lands_surface':57614,
                    'production': 890333,
                    'condition':'Below average',
                    'productivity':20,
                },
                'Apple':{
                    'lands_surface':617,
                    'production': 29752,
                    'condition':'Poor',
                    'productivity':48.7,
                }
            },
            'Land_data':{
                'cultivated land':89209,
                'terre_au_repo':41708,
                'unused land':3587 
            }
        },
        'BISKRA':{
            'Products':{
                'Wheat':{
                    'lands_surface':18950,
                    'production': 789435,
                    'condition':'Above average',
                    'productivity':41.4,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':43851,
                    'production': 4723000,
                    'condition':'Ideal',
                    'productivity':108.7,
                },
                'Potatoes':{
                    'lands_surface':328,
                    'production': 94100,
                    'condition':'Average',
                    'productivity':286.9,
                },
                'Tomatoes':{
                    'lands_surface':2503,
                    'production': 3664280,
                    'condition':'Ideal',
                    'productivity':1464,
                },
                'Greenpepper':{
                    'lands_surface':1124,
                    'production':867535,
                    'condition':'Ideal',
                    'productivity':771.8,
                },
                'Aubergines':{
                    'lands_surface':879,
                    'production': 388745,
                    'condition':'Ideal',
                    'productivity':442.3,
                },
                'Onions':{
                    'lands_surface':2470,
                    'production':470900,
                    'condition':'Below average',
                    'productivity':190.6,
                },
                'Carrots':{
                    'lands_surface':1003,
                    'production': 119221,
                    'condition':'Poor',
                    'productivity':118.9,
                },
                'Lemon':{
                    'lands_surface':66,
                    'production':3010,
                    'condition':'Poor',
                    'productivity':47.2,
                },
                'Olive':{
                    'lands_surface':4569,
                    'production': 176490,
                    'condition':'Average',
                    'productivity':26.1,
                },
                'Apple':{
                    'lands_surface':471,
                    'production': 18118,
                    'condition':'Poor',
                    'productivity':41.4,
                }
            },
            'Land_data':{
                'cultivated land':112933,
                'terre_au_repo':72530,
                'unused land':67532 
            }
        },
        'BECHAR':{
            'Products':{
                'Wheat':{
                    'lands_surface':468,
                    'production': 13086,
                    'condition':'Average',
                    'productivity':25,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':13919,
                    'production': 398130,
                    'condition':'Below Average',
                    'productivity':40,
                },
                'Potatoes':{
                    'lands_surface':297,
                    'production': 63400,
                    'condition':'Average',
                    'productivity':213.5,
                },
                'Tomatoes':{
                    'lands_surface':240,
                    'production': 36012,
                    'condition':'Poor',
                    'productivity':150,
                },
                'Greenpepper':{
                    'lands_surface':61,
                    'production':5174,
                    'condition':'Poor',
                    'productivity':85,
                },
                'Aubergines':{
                    'lands_surface':75,
                    'production': 10917,
                    'condition':'Below average',
                    'productivity':145,
                },
                'Onions':{
                    'lands_surface':370,
                    'production':93880,
                    'condition':'Average',
                    'productivity':253.7,
                },
                'Carrots':{
                    'lands_surface':200,
                    'production': 23000,
                    'condition':'Poor',
                    'productivity':115,
                },
                'Lemon':{
                    'lands_surface':33,
                    'production':4495,
                    'condition':'Below average',
                    'productivity':155.0,
                },
                'Olive':{
                    'lands_surface':1650,
                    'production': 9962,
                    'condition':'Poor',
                    'productivity':6.2,
                },
                'Apple':{
                    'lands_surface':27,
                    'production': 1655,
                    'condition':'Poor',
                    'productivity':63.7,
                }
            },
            'Land_data':{
                'cultivated land':18356,
                'terre_au_repo':16716,
                'unused land':69834  
            }
        },
        'BLIDA':{
            'Products':{
                'Wheat':{
                    'lands_surface':7551,
                    'production': 220109,
                    'condition':'Average',
                    'productivity':29.6,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':580,
                    'production': 277720,
                    'condition':'Ideal',
                    'productivity':478.8,
                },
                'Tomatoes':{
                    'lands_surface':109,
                    'production': 58195,
                    'condition':'Average',
                    'productivity':531.5,
                },
                'Greenpepper':{
                    'lands_surface':238,
                    'production':123985,
                    'condition':'Ideal',
                    'productivity':520.6,
                },
                'Aubergines':{
                    'lands_surface':127,
                    'production': 47420,
                    'condition':'Above average',
                    'productivity':374.9,
                },
                'Onions':{
                    'lands_surface':558,
                    'production':102112,
                    'condition':'Below average',
                    'productivity':182.9,
                },
                'Carrots':{
                    'lands_surface':166,
                    'production':22280,
                    'condition':'Poor',
                    'productivity':134.2,
                },
                'Lemon':{
                    'lands_surface':1145,
                    'production': 278827,
                    'condition':'Average',
                    'productivity':271.5,
                },
                'Olive':{
                    'lands_surface':1230,
                    'production': 65064,
                    'condition':'Average',
                    'productivity':24.1,
                },
                'Apple':{
                    'lands_surface':1329,
                    'production': 342238,
                    'condition':'Average',
                    'productivity':257.4,
                }
            },
            'Land_data':{
                'cultivated land':47650,
                'terre_au_repo':6653,
                'unused land':1660  
            }
        },
        'BOUIRA':{
            'Products':{
                'Wheat':{
                    'lands_surface':53987,
                    'production': 1700355,
                    'condition':'Average',
                    'productivity':31.2,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':6093,
                    'production': 2104192,
                    'condition':'Above average',
                    'productivity':345.4,
                },
                'Tomatoes':{
                    'lands_surface':202,
                    'production': 59194,
                    'condition':'Below average',
                    'productivity':292.7,
                },
                'Greenpepper':{
                    'lands_surface':95,
                    'production':4752,
                    'condition':'Poor',
                    'productivity':50.3,
                },
                'Aubergines':{
                    'lands_surface':15,
                    'production': 1100,
                    'condition':'Poor',
                    'productivity':73.3,
                },
                'Onions':{
                    'lands_surface':568,
                    'production':67750,
                    'condition':'Below average',
                    'productivity':119.4,
                },
                'Carrots':{
                    'lands_surface':81,
                    'production':17578,
                    'condition':'Below average',
                    'productivity':218.4,
                },
                'Lemon':{
                    'lands_surface':36,
                    'production': 2460,
                    'condition':'Poor',
                    'productivity':73.4,
                },
                'Olive':{
                    'lands_surface':37309,
                    'production': 432442,
                    'condition':'Below average',
                    'productivity':16.0,
                },
                'Apple':{
                    'lands_surface':630,
                    'production': 13065,
                    'condition':'Poor',
                    'productivity':27,
                }
            },
            'Land_data':{
                'cultivated land':129979,
                'terre_au_repo':59981,
                'unused land':29689  
            }
        },
        'TAMANRASSET':{
            'Products':{
                'Wheat':{
                    'lands_surface':550,
                    'production': 13092,
                    'condition':'Average',
                    'productivity':23.8,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':7118,
                    'production': 105181,
                    'condition':'Poor',
                    'productivity':16.4,
                },
                'Potatoes':{
                    'lands_surface':55,
                    'production': 8467,
                    'condition':'Below average',
                    'productivity':153.9,
                },
                'Tomatoes':{
                    'lands_surface':220,
                    'production': 44460,
                    'condition':'Below average',
                    'productivity':202.5,
                },
                'Greenpepper':{
                    'lands_surface':33,
                    'production':5173,
                    'condition':'Below average',
                    'productivity':158.6,
                },
                'Aubergines':{
                    'lands_surface':45,
                    'production': 6179,
                    'condition':'Below average',
                    'productivity':137.6,
                },
                'Onions':{
                    'lands_surface':198,
                    'production':38767,
                    'condition':'Below average',
                    'productivity':196.3,
                },
                'Carrots':{
                    'lands_surface':111,
                    'production':14659,
                    'condition':'Poor',
                    'productivity':132.7,
                },
                'Lemon':{
                    'lands_surface':116,
                    'production': 3255,
                    'condition':'Poor',
                    'productivity':30,
                },
                'Olive':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Apple':{
                    'lands_surface':150,
                    'production': 2410,
                    'condition':'Poor',
                    'productivity':20.1,
                }
            },
            'Land_data':{
                'cultivated land':11262,
                'terre_au_repo':0,
                'unused land':54103  
            }
        },
        'TEBESSA':{
            'Products':{
                'Wheat':{
                    'lands_surface':6000,
                    'production': 822350,
                    'condition':'Below average',
                    'productivity':13.8,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':569,
                    'production': 19900,
                    'condition':'Average',
                    'productivity':49.7,
                },
                'Potatoes':{
                    'lands_surface':3376,
                    'production': 1603500,
                    'condition':'Ideal',
                    'productivity':475.0,
                },
                'Tomatoes':{
                    'lands_surface':110,
                    'production': 13360,
                    'condition':'Poor',
                    'productivity':121.5,
                },
                'Greenpepper':{
                    'lands_surface':33,
                    'production':5173,
                    'condition':'Below average',
                    'productivity':158.6,
                },
                'Aubergines':{
                    'lands_surface':45,
                    'production': 6179,
                    'condition':'Below average',
                    'productivity':137.6,
                },
                'Onions':{
                    'lands_surface':225,
                    'production':46500,
                    'condition':'Average',
                    'productivity':206.7,
                },
                'Carrots':{
                    'lands_surface':160,
                    'production':38960,
                    'condition':'Below average',
                    'productivity':243.5,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production':0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':9534,
                    'production':70600,
                    'condition':'Poor',
                    'productivity':7.0,
                },
                'Apple':{
                    'lands_surface':507,
                    'production': 19600,
                    'condition':'Poor',
                    'productivity':40,
                }
            },
            'Land_data':{
                'cultivated land':210639,
                'terre_au_repo':101536,
                'unused land':72094  
            }
        
        },

        ###########################################################33
        #############################################################
        'TLEMCEN':{
            'Products':{
                'Wheat':{
                    'lands_surface':82796,
                    'production': 909550,
                    'condition':'Below average',
                    'productivity':10.65,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':5606,
                    'production': 1762100,
                    'condition':'Above average',
                    'productivity':314.3,
                },
                'Tomatoes':{
                    'lands_surface':1010,
                    'production': 717500,
                    'condition':'Above average',
                    'productivity':710.4,
                },
                'Greenpepper':{
                    'lands_surface':700,
                    'production': 175000,
                    'condition':'Average',
                    'productivity':250.0,
                },
                'Aubergines':{
                    'lands_surface':85,
                    'production': 12000,
                    'condition':'Below average',
                    'productivity':141.2,
                },
                'Onions':{
                    'lands_surface':1355,
                    'production': 370000,
                    'condition':'Average',
                    'productivity':273.1,
                },
                'Carrots':{
                    'lands_surface':750,
                    'production': 125400,
                    'condition':'Poor',
                    'productivity':167.2,
                },
                'Lemon':{
                    'lands_surface':170,
                    'production': 37500,
                    'condition':'Average',
                    'productivity':250.0,
                },
                'Olive':{
                    'lands_surface':15546,
                    'production': 750000,
                    'condition':'Average',
                    'productivity':35.0,
                },
                'Apple':{
                    'lands_surface':1220,
                    'production': 108000,
                    'condition':'Below average',
                    'productivity':120.0,
                }
            },
            'Land_data':{
                'cultivated land':350085,
                'terre_au_repo':77872,
                'unused land':37953
            }
        },
        'TIARET':{
            'Products':{
                'Wheat':{
                    'lands_surface':177861,
                    'production': 2459500,
                    'condition':'Below average',
                    'productivity':12.5,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':6470,
                    'production': 2323442,
                    'condition':'Above average',
                    'productivity':359.1,
                },
                'Tomatoes':{
                    'lands_surface':220,
                    'production': 66000,
                    'condition':'Below average',
                    'productivity':300,
                },
                'Greenpepper':{
                    'lands_surface':162,
                    'production': 45360,
                    'condition':'Average',
                    'productivity':280.0,
                },
                'Aubergines':{
                    'lands_surface':40,
                    'production': 12800 ,
                    'condition':'Above average',
                    'productivity':320.0,
                },
                'Onions':{
                    'lands_surface':4820,
                    'production': 2724000,
                    'condition':'Ideal',
                    'productivity':565.1,
                },
                'Carrots':{
                    'lands_surface':340,
                    'production': 56180,
                    'condition':'Poor',
                    'productivity':165.2
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':4597,
                    'production': 64000,
                    'condition':'Below average',
                    'productivity':10.5,
                },
                'Apple':{
                    'lands_surface':2384,
                    'production': 95500,
                    'condition':'Poor',
                    'productivity':47.8,
                }
            },
            'Land_data':{
                'cultivated land':419469,
                'terre_au_repo':269257,
                'unused land':0
            }
        },
        'TIZI-OUZOU':{
            'Products':{
                'Wheat':{
                    'lands_surface':6637,
                    'production': 136725,
                    'condition':'Average',
                    'productivity':23.6,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':661,
                    'production': 202295,
                    'condition':'Above average',
                    'productivity':306.0,
                },
                'Tomatoes':{
                    'lands_surface':168,
                    'production': 48209,
                    'condition':'Below average',
                    'productivity':286.6,
                },
                'Greenpepper':{
                    'lands_surface':91,
                    'production': 13495,
                    'condition':'Below average',
                    'productivity':149.1,
                },
                'Aubergines':{
                    'lands_surface':3,
                    'production': 894 ,
                    'condition':'Average',
                    'productivity':256.9,
                },
                'Onions':{
                    'lands_surface':956,
                    'production': 133309,
                    'condition':'Below average',
                    'productivity':193.5,
                },
                'Carrots':{
                    'lands_surface':42,
                    'production': 9730,
                    'condition':'Below average',
                    'productivity':234.5,
                },
                'Lemon':{
                    'lands_surface':75,
                    'production': 20850,
                    'condition':'Above average',
                    'productivity':301.1,
                },
                'Olive':{
                    'lands_surface':38828,
                    'production': 504208,
                    'condition':'Below average',
                    'productivity':15.0,
                },
                'Apple':{
                    'lands_surface':359,
                    'production': 69004,
                    'condition':'Average',
                    'productivity':206.8,
                }
            },
            'Land_data':{
                'cultivated land':77515,
                'terre_au_repo':21328,
                'unused land':21859
            }
        },
        'ALGER':{
            'Products':{
                'Wheat':{
                    'lands_surface':1538,
                    'production': 49425,
                    'condition':'Average',
                    'productivity':29.45,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':1037,
                    'production': 409650,
                    'condition':'Above average',
                    'productivity':394.9,
                },
                'Tomatoes':{
                    'lands_surface':949,
                    'production': 523840,
                    'condition':'Average',
                    'productivity':552.1,
                },
                'Greenpepper':{
                    'lands_surface':500,
                    'production': 142385,
                    'condition':'Average',
                    'productivity':284.9,
                },
                'Aubergines':{
                    'lands_surface':520,
                    'production': 152290,
                    'condition':'Average',
                    'productivity':293.1,
                },
                'Onions':{
                    'lands_surface':130,
                    'production': 31330,
                    'condition':'Average',
                    'productivity':241.0,
                },
                'Carrots':{
                    'lands_surface':214,
                    'production': 56345,
                    'condition':'Below average',
                    'productivity':263.3,
                },
                'Lemon':{
                    'lands_surface':802,
                    'production': 125630,
                    'condition':'Average',
                    'productivity':217.8,
                },
                'Olive':{
                    'lands_surface':190,
                    'production': 5316,
                    'condition':'Below average',
                    'productivity':13.7
                },
                'Apple':{
                    'lands_surface':891,
                    'production': 182570,
                    'condition':'Average',
                    'productivity':209.6,
                }
            },
            'Land_data':{
                'cultivated land':25174,
                'terre_au_repo':3696,
                'unused land':2185 
            }
        },
        'DJELFA':{
            'Products':{
                'Wheat':{
                    'lands_surface':7297,
                    'production': 167000,
                    'condition':'Average',
                    'productivity':26.35,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':260,
                    'production': 13210,
                    'condition':'Above average',
                    'productivity':73.4,
                },
                'Potatoes':{
                    'lands_surface':5752,
                    'production': 1644220,
                    'condition':'Average',
                    'productivity':285.9,
                },
                'Tomatoes':{
                    'lands_surface':285,
                    'production': 42000,
                    'condition':'Poor',
                    'productivity':147.4,
                },
                'Greenpepper':{
                    'lands_surface':77,
                    'production':5940,
                    'condition':'Poor',
                    'productivity':77.1,
                },
                'Aubergines':{
                    'lands_surface':57,
                    'production': 5130,
                    'condition':'Poor',
                    'productivity':90.0,
                },
                'Onions':{
                    'lands_surface':1549,
                    'production': 596400,
                    'condition':'Above average',
                    'productivity':385.0,
                },
                'Carrots':{
                    'lands_surface':780,
                    'production': 129090,
                    'condition':'Poor',
                    'productivity':165.5,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':11329,
                    'production': 339800,
                    'condition':'Below average',
                    'productivity':13.9,
                },
                'Apple':{
                    'lands_surface':977,
                    'production': 120900,
                    'condition':'Below average',
                    'productivity':127.1,
                }
            },
            'Land_data':{
                'cultivated land':134331,
                'terre_au_repo':252721,
                'unused land':0 
            }
        },
        'JIJEL':{
            'Products':{
                'Wheat':{
                    'lands_surface':1322,
                    'production': 35937,
                    'condition':'Average',
                    'productivity':27.2,
                },
                'Corn':{
                    'lands_surface':108,
                    'production': 17375,
                    'condition':'Ideal',
                    'productivity':160.9,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':641,
                    'production': 189989,
                    'condition':'Average',
                    'productivity':296.4,
                },
                'Tomatoes':{
                    'lands_surface':669,
                    'production': 420250,
                    'condition':'Above average',
                    'productivity':628.6,
                },
                'Greenpepper':{
                    'lands_surface':298,
                    'production':193125,
                    'condition':'Ideal',
                    'productivity':647.4,
                },
                'Aubergines':{
                    'lands_surface':116,
                    'production': 40515,
                    'condition':'Above average',
                    'productivity':348.8,
                },
                'Onions':{
                    'lands_surface':893,
                    'production': 313697,
                    'condition':'Above average',
                    'productivity':351.3,
                },
                'Carrots':{
                    'lands_surface':34,
                    'production': 5936,
                    'condition':'Poor',
                    'productivity':177.2,
                },
                'Lemon':{
                    'lands_surface':51,
                    'production': 8449,
                    'condition':'Average',
                    'productivity':204.1,
                },
                'Olive':{
                    'lands_surface':16603,
                    'production': 555859,
                    'condition':'Average',
                    'productivity':26.4,
                },
                'Apple':{
                    'lands_surface':353,
                    'production': 51860,
                    'condition':'Below average',
                    'productivity':151.3,
                }
            },
            'Land_data':{
                'cultivated land':32692,
                'terre_au_repo':12275,
                'unused land':14511 
            }
        },
        'SETIF':{
            'Products':{
                'Wheat':{
                    'lands_surface':143970,
                    'production': 2599833,
                    'condition':'Below average',
                    'productivity':17.95,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':1481,
                    'production': 416344,
                    'condition':'Average',
                    'productivity':281.1,
                },
                'Tomatoes':{
                    'lands_surface':608,
                    'production': 203421,
                    'condition':'Below average',
                    'productivity':334.5,
                },
                'Greenpepper':{
                    'lands_surface':414,
                    'production':265004,
                    'condition':'Ideal',
                    'productivity':639.9,
                },
                'Aubergines':{
                    'lands_surface':7,
                    'production': 1005,
                    'condition':'Below average',
                    'productivity':143.6,
                },
                'Onions':{
                    'lands_surface':443,
                    'production':96965,
                    'condition':'Average',
                    'productivity':218.8,
                },
                'Carrots':{
                    'lands_surface':541,
                    'production':83210,
                    'condition':'Poor',
                    'productivity':153.8,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':23611,
                    'production': 341050,
                    'condition':'Below average',
                    'productivity':14.9,
                },
                'Apple':{
                    'lands_surface':1399,
                    'production': 58717,
                    'condition':'Poor',
                    'productivity':42.3,
                }
            },
            'Land_data':{
                'cultivated land':269912,
                'terre_au_repo':95202,
                'unused land':41084 
            }
        },
        'SAIDA':{
            'Products':{
                'Wheat':{
                    'lands_surface':54672,
                    'production': 568770,
                    'condition':'Below average',
                    'productivity':10.5,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':4047,
                    'production': 1194410,
                    'condition':'Average',
                    'productivity':295.1,
                },
                'Tomatoes':{
                    'lands_surface':588,
                    'production': 263600,
                    'condition':'Average',
                    'productivity':448.3,
                },
                'Greenpepper':{
                    'lands_surface':367,
                    'production':91840,
                    'condition':'Average',
                    'productivity':250.2,
                },
                'Aubergines':{
                    'lands_surface':51,
                    'production': 16430,
                    'condition':'Above average',
                    'productivity':322.2,
                },
                'Onions':{
                    'lands_surface':2262,
                    'production':991295,
                    'condition':'Ideal',
                    'productivity':483.2,
                },
                'Carrots':{
                    'lands_surface':843,
                    'production': 327221,
                    'condition':'Below average',
                    'productivity':388.2,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':5597,
                    'production': 150098,
                    'condition':'Average',
                    'productivity':20.9,
                },
                'Apple':{
                    'lands_surface':459,
                    'production': 17468,
                    'condition':'Poor',
                    'productivity':39.4,
                }
            },
            'Land_data':{
                'cultivated land':158436,
                'terre_au_repo':149771,
                'unused land':43479  
            }
        },
        'SKIKDA':{
            'Products':{
                'Wheat':{
                    'lands_surface':29630,
                    'production': 730600,
                    'condition':'Average',
                    'productivity':23.7,
                },
                'Corn':{
                    'lands_surface':113,
                    'production': 4990,
                    'condition':'Average',
                    'productivity':44.2,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':6020,
                    'production': 1617730,
                    'condition':'Average',
                    'productivity':268.7,
                },
                'Tomatoes':{
                    'lands_surface':413,
                    'production': 123750,
                    'condition':'Below average',
                    'productivity':300.0,
                },
                'Greenpepper':{
                    'lands_surface':379,
                    'production':64505,
                    'condition':'Below average',
                    'productivity':170.2,
                },
                'Aubergines':{
                    'lands_surface':101,
                    'production': 20790,
                    'condition':'Average',
                    'productivity':205.8,
                },
                'Onions':{
                    'lands_surface':4363,
                    'production':1197100,
                    'condition':'Average',
                    'productivity':274.4,
                },
                'Carrots':{
                    'lands_surface':566,
                    'production':167980,
                    'condition':'Below average',
                    'productivity':296.8,
                },
                'Lemon':{
                    'lands_surface':133,
                    'production':23154,
                    'condition':'Average',
                    'productivity':202.2,
                },
                'Olive':{
                    'lands_surface':11833,
                    'production': 222732,
                    'condition':'Below average',
                    'productivity':17.0,
                },
                'Apple':{
                    'lands_surface':1721,
                    'production': 215675,
                    'condition':'Below average',
                    'productivity':153.5,
                }
            },
            'Land_data':{
                'cultivated land':107927,
                'terre_au_repo':23902,
                'unused land':18217  
            }
        },
        'S.B.ABBES':{
            'Products':{
                'Wheat':{
                    'lands_surface':79288,
                    'production': 749500,
                    'condition':'Poor',
                    'productivity':9.25,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':2476,
                    'production': 641867,
                    'condition':'Average',
                    'productivity':259.2,
                },
                'Tomatoes':{
                    'lands_surface':310,
                    'production': 170500,
                    'condition':'Average',
                    'productivity':550.0,
                },
                'Greenpepper':{
                    'lands_surface':200,
                    'production':42000,
                    'condition':'Average',
                    'productivity':210.0,
                },
                'Aubergines':{
                    'lands_surface':68,
                    'production': 17680,
                    'condition':'Average',
                    'productivity':260.0,
                },
                'Onions':{
                    'lands_surface':655,
                    'production':138140,
                    'condition':'Average',
                    'productivity':210.9,
                },
                'Carrots':{
                    'lands_surface':210,
                    'production':50400,
                    'condition':'Below average',
                    'productivity':240.0,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':8781,
                    'production': 223824,
                    'condition':'Average',
                    'productivity':39.1,
                },
                'Apple':{
                    'lands_surface':2406,
                    'production': 141550,
                    'condition':'Poor',
                    'productivity':100.0,
                }
            },
            'Land_data':{
                'cultivated land':228421,
                'terre_au_repo':134772,
                'unused land':19644  
            }
        },
        'ANNABA':{
            'Products':{
                'Wheat':{
                    'lands_surface':14967,
                    'production': 420910,
                    'condition':'Average',
                    'productivity':30.85,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':359,
                    'production': 132615,
                    'condition':'Above average',
                    'productivity':369.4,
                },
                'Tomatoes':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Greenpepper':{
                    'lands_surface':337,
                    'production':50425,
                    'condition':'Below average',
                    'productivity':149.6,
                },
                'Aubergines':{
                    'lands_surface':146,
                    'production': 19663,
                    'condition':'Below average',
                    'productivity':134.7,
                },
                'Onions':{
                    'lands_surface':259,
                    'production':47650,
                    'condition':'Below average',
                    'productivity':184.0,
                },
                'Carrots':{
                    'lands_surface':196,
                    'production':28012,
                    'condition':'Poor',
                    'productivity':142.9,
                },
                'Lemon':{
                    'lands_surface':48,
                    'production': 4525,
                    'condition':'Average',
                    'productivity':205.7,
                },
                'Olive':{
                    'lands_surface':969,
                    'production': 14665,
                    'condition':'Below average',
                    'productivity':19.1,
                },
                'Apple':{
                    'lands_surface':150,
                    'production': 18127,
                    'condition':'Below average',
                    'productivity':140.5,
                }
            },
            'Land_data':{
                'cultivated land':36360,
                'terre_au_repo':11090,
                'unused land':2786  
            }
        },
        'GUELMA':{
            'Products':{
                'Wheat':{
                    'lands_surface':79629,
                    'production': 2541890,
                    'condition':'Average',
                    'productivity':33.75,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':331,
                    'production': 103409,
                    'condition':'Above average',
                    'productivity':312.7,
                },
                'Tomatoes':{
                    'lands_surface':184,
                    'production': 67490,
                    'condition':'Below average',
                    'productivity':366.8,
                },
                'Greenpepper':{
                    'lands_surface':72,
                    'production':9590,
                    'condition':'Below average',
                    'productivity':133.2,
                },
                'Aubergines':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Onions':{
                    'lands_surface':914,
                    'production':310920,
                    'condition':'Above average',
                    'productivity':340.2,
                },
                'Carrots':{
                    'lands_surface':7,
                    'production':1860,
                    'condition':'Below average',
                    'productivity':265.7,
                },
                'Lemon':{
                    'lands_surface':27,
                    'production':4850,
                    'condition':'Average',
                    'productivity':202.1,
                },
                'Olive':{
                    'lands_surface':9531,
                    'production':72275,
                    'condition':'Below average',
                    'productivity':14.0,
                },
                'Apple':{
                    'lands_surface':300,
                    'production': 40003,
                    'condition':'Below average',
                    'productivity':156.4,
                }
            },
            'Land_data':{
                'cultivated land':131755,
                'terre_au_repo':5583,
                'unused land':26405 
            }
        }
    ###############################################################
},
########RANIA'S PART############
     
        'CONSTANTINE':{
            'Products':{
                'Wheat':{
                    'lands_surface':79982,
                    'production': 2393198,
                    'condition':'ideal ',
                    'productivity':60.6,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':101,
                    'production': 30850,
                    'condition':'Above average',
                    'productivity':307.0,
                },
                'Tomatoes':{
                    'lands_surface':23,
                    'production': 4600,
                    'condition':'Below average',
                    'productivity':204.4,
                },
                'Greenpepper':{
                    'lands_surface':44,
                    'production':4425,
                    'condition':'Below average',
                    'productivity':100.6,
                },
                'Aubergines':{
                    'lands_surface':9,
                    'production': 800,
                    'condition':'Poor',
                    'productivity':88.9,
                },
                'Onions':{
                    'lands_surface':662,
                    'production':147220,
                    'condition':'average',
                    'productivity':222.4,
                },
                'Carrots':{
                    'lands_surface':49,
                    'production':5240,
                    'condition':'poor',
                    'productivity':106.9,
                },
                'Lemon':{
                    'lands_surface':5,
                    'production':55,
                    'condition':'Below average',
                    'productivity':110.0,
                },
                'Olive':{
                    'lands_surface':672,
                    'production':11380,
                    'condition':'poor',
                    'productivity':8.2,
                },
                'Apple':{
                    'lands_surface':160,
                    'production': 28700,
                    'condition':'average',
                    'productivity':249.1,
                }
            },
            'Land_data':{
                'cultivated land':115701,
                'terre_au_repo':9289,
                'unused land':0 
            }
        }
    ,
        ' MEDEA':{
            'Products':{
                'Wheat':{
                    'lands_surface':81693,
                    'production': 1451479,
                    'condition':'Below average',
                    'productivity':17.6,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':331,
                    'production': 103409,
                    'condition':'Above average',
                    'productivity':312.7,
                },
                'Tomatoes':{
                    'lands_surface':184,
                    'production': 67490,
                    'condition':'Below average',
                    'productivity':366.8,
                },
                'Greenpepper':{
                    'lands_surface':368,
                    'production':21940,
                    'condition':'Poor',
                    'productivity':59.6,
                },
                'Aubergines':{
                    'lands_surface':67,
                    'production': 9170,
                    'condition':'Below average',
                    'productivity':136.9,
                },
                'Onions':{
                    'lands_surface':914,
                    'production':310920,
                    'condition':'Above average',
                    'productivity':340.2,
                },
                'Carrots':{
                    'lands_surface':289,
                    'production':42450,
                    'condition':'Poor',
                    'productivity':146.9,
                },
                'Lemon':{
                    'lands_surface':4,
                    'production':580,
                    'condition':'Below average',
                    'productivity':145.0,
                },
                'Olive':{
                    'lands_surface':8814,
                    'production':57523,
                    'condition':'Below average',
                    'productivity':15.1,
                },
                'Apple':{
                    'lands_surface':3680,
                    'production': 539761,
                    'condition':'below average',
                    'productivity':188.3,
                }
            },
            'Land_data':{
                'cultivated land':191292,
                'terre_au_repo':134475,
                'unused land':104054 
            }
        } ,
        'MOSTAGANEM':{
            'Products':{
                'Wheat':{
                    'lands_surface':17382,
                    'production': 342076,
                    'condition':'Above average',
                    'productivity':40.0,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':16189,
                    'production': 5245110,
                    'condition':'above average',
                    'productivity':324.0,
                },
                'Tomatoes':{
                    'lands_surface':2396,
                    'production': 1327485,
                    'condition':'average',
                    'productivity':554.2,
                },
                'Greenpepper':{
                    'lands_surface':1231,
                    'production':456450,
                    'condition':'above average',
                    'productivity':370.8,
                },
                'Aubergines':{
                    'lands_surface':749,
                    'production': 329165,
                    'condition':'ideal',
                    'productivity':439.6,
                },
                'Onions':{
                    'lands_surface':1775,
                    'production':624300,
                    'condition':'Above average',
                    'productivity':351.7,
                },
                'Carrots':{
                    'lands_surface':813,
                    'production':209415,
                    'condition':'below average',
                    'productivity':257.6,
                },
                'Lemon':{
                    'lands_surface':254,
                    'production':69692,
                    'condition':'average',
                    'productivity':279.3,
                },
                'Olive':{
                    'lands_surface':8142,
                    'production':212252,
                    'condition':'average',
                    'productivity':24.6,
                },
                'Apple':{
                    'lands_surface':1032,
                    'production': 77568,
                    'condition':'Poor',
                    'productivity':78,
                }
            },
            'Land_data':{
                'cultivated land':116066,
                'terre_au_repo':5323,
                'unused land':7400 
            }
        }
        ,
        'MSILA':{
            'Products':{
                'Wheat':{
                    'lands_surface':11350,
                    'production': 261050,
                    'condition':'average',
                    'productivity':23.0,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':915,
                    'production': 281010,
                    'condition':'above average',
                    'productivity':307.1,
                },
                'Tomatoes':{
                    'lands_surface':375,
                    'production': 142800,
                    'condition':'below average',
                    'productivity':380.8,
                },
                'Greenpepper':{
                    'lands_surface':97,
                    'production':32100,
                    'condition':'above average',
                    'productivity':330.9,
                },
                'Aubergines':{
                    'lands_surface':66,
                    'production': 21200,
                    'condition':'above average',
                    'productivity':321.2,
                },
                'Onions':{
                    'lands_surface':1070,
                    'production':322400,
                    'condition':'Above average',
                    'productivity':301.3,
                },
                'Carrots':{
                    'lands_surface':2350,
                    'production':940000,
                    'condition':'Above average',
                    'productivity':400.0,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production':0,
                    'condition':'poor',
                    'productivity':0.0,
                },
                'Olive':{
                    'lands_surface':10442,
                    'production':173215,
                    'condition':'Below average',
                    'productivity':12.2,
                },
                'Apple':{
                    'lands_surface':250,
                    'production': 7750,
                    'condition':'Poor',
                    'productivity':55.0,
                }
            },
            'Land_data':{
                'cultivated land':119993,
                'terre_au_repo':157565,
                'unused land':0 
            }
        },
        'MASCARA':{
            'Products':{
                'Wheat':{
                    'lands_surface':42900,
                    'production': 512050,
                    'condition':'Below average',
                    'productivity':11.8,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':14609,
                    'production': 3878400,
                    'condition':'average',
                    'productivity':265.5,
                },
                'Tomatoes':{
                    'lands_surface':350,
                    'production': 86600,
                    'condition':'below average',
                    'productivity':247.4,
                },
                'Greenpepper':{
                    'lands_surface':631,
                    'production':146500,
                    'condition':'average',
                    'productivity':233.1,
                },
                'Aubergines':{
                    'lands_surface':105,
                    'production': 22300,
                    'condition':'average',
                    'productivity':212.4,
                },
                'Onions':{
                    'lands_surface':3764,
                    'production': 1962400,
                    'condition':'average',
                    'productivity':521.4,
                },
                'Carrots':{
                    'lands_surface':350,
                    'production':67900,
                    'condition':'poor',
                    'productivity':194.0,
                },
                'Lemon':{
                    'lands_surface':84,
                    'production':12400,
                    'condition':'Below average',
                    'productivity':149.4,
                },
                'Olive':{
                    'lands_surface':16166,
                    'production':794250,
                    'condition':'above average',
                    'productivity':53.4,
                },
                'Apple':{
                    'lands_surface':519,
                    'production': 29500,
                    'condition':'Poor',
                    'productivity':72.4,
                }
            },
            'Land_data':{
                'cultivated land':231708,
                'terre_au_repo':76323,
                'unused land':17054
            }
        },
        'OUARGLA':{
            'Products':{
                'Wheat':{
                    'lands_surface':2584,
                    'production': 86515,
                    'condition':' ideal',
                    'productivity':50.75,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':22512,
                    'production': 1650164,
                    'condition':'above average',
                    'productivity':70.1,
                },
                'Potatoes':{
                    'lands_surface':1976,
                    'production': 583873,
                    'condition':'average',
                    'productivity':295.5,
                },
                'Tomatoes':{
                    'lands_surface':218,
                    'production': 51057,
                    'condition':'below average',
                    'productivity':233.9,
                },
                'Greenpepper':{
                    'lands_surface':9,
                    'production':3531,
                    'condition':'ideal',
                    'productivity':406.7,
                },
                'Aubergines':{
                    'lands_surface':110,
                    'production': 31316,
                    'condition':'average',
                    'productivity':285.6,
                },
                'Onions':{
                    'lands_surface':517,
                    'production':86511,
                    'condition':'below average',
                    'productivity':167.3,
                },
                'Carrots':{
                    'lands_surface':151,
                    'production':30757,
                    'condition':'below average',
                    'productivity':204.0,
                },
                'Lemon':{
                    'lands_surface':17,
                    'production':672,
                    'condition':'poor',
                    'productivity':81,
                },
                'Olive':{
                    'lands_surface':1269,
                    'production':8457,
                    'condition':'Below average',
                    'productivity':17.2,
                },
                'Apple':{
                    'lands_surface':14,
                    'production': 229,
                    'condition':'Poor',
                    'productivity':23.1,
                }
            },
            'Land_data':{
                'cultivated land':28995,
                'terre_au_repo':25521,
                'unused land':884050 
            }
        } ,
        'ORAN':{
            'Products':{
                'Wheat':{
                    'lands_surface':5474,
                    'production': 38149,
                    'condition':'poor',
                    'productivity':7.0,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':193,
                    'production': 45873,
                    'condition':'average',
                    'productivity':237.4,
                },
                'Tomatoes':{
                    'lands_surface':232,
                    'production': 69842,
                    'condition':'below average',
                    'productivity':300.9,
                },
                'Greenpepper':{
                    'lands_surface':131,
                    'production':18643,
                    'condition':'below average',
                    'productivity':142.7,
                },
                'Aubergines':{
                    'lands_surface':22,
                    'production': 4612,
                    'condition':'average',
                    'productivity':207.6,
                },
                'Onions':{
                    'lands_surface':39,
                    'production':5750,
                    'condition':'below average',
                    'productivity':147.4,
                },
                'Carrots':{
                    'lands_surface':16,
                    'production':2065,
                    'condition':'poor',
                    'productivity':129.1,
                },
                'Lemon':{
                    'lands_surface':33,
                    'production':2387,
                    'condition':'Below average',
                    'productivity':103.8,
                },
                'Olive':{
                    'lands_surface':7400,
                    'production':152593,
                    'condition':'Below average',
                    'productivity':14.7,
                },
                'Apple':{
                    'lands_surface':84,
                    'production': 697,
                    'condition':'Poor',
                    'productivity':22.5,
                }
            },
            'Land_data':{
                'cultivated land':75964,
                'terre_au_repo':10180,
                'unused land':6479 
            }
        } ,
        'EL-BAYADH':{
            'Products':{
                'Wheat':{
                    'lands_surface':3492,
                    'production': 81765,
                    'condition':'above average',
                    'productivity':47.8,
                },
                'Corn':{
                    'lands_surface':12,
                    'production': 900,
                    'condition':'above average',
                    'productivity':75.0,
                },
                'Dates':{
                    'lands_surface':477,
                    'production': 824,
                    'condition':'below average',
                    'productivity':39.2,
                },
                'Potatoes':{
                    'lands_surface':2366,
                    'production': 684290,
                    'condition':'average',
                    'productivity':289.2,
                },
                'Tomatoes':{
                    'lands_surface':137,
                    'production': 47895,
                    'condition':'below average',
                    'productivity':349.6,
                },
                'Greenpepper':{
                    'lands_surface':56,
                    'production':5953,
                    'condition':'below average',
                    'productivity':106.3,
                },
                'Aubergines':{
                    'lands_surface':35,
                    'production': 10795,
                    'condition':'above average',
                    'productivity':310.6,
                },
                'Onions':{
                    'lands_surface':538,
                    'production':284675,
                    'condition':'ideal',
                    'productivity':529.1,
                },
                'Carrots':{
                    'lands_surface':205,
                    'production':48065,
                    'condition':'below average',
                    'productivity':234.5,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production':0,
                    'condition':'poor',
                    'productivity':0.0,
                },
                'Olive':{
                    'lands_surface':1191,
                    'production':15882,
                    'condition':'poor',
                    'productivity':9.8,
                },
                'Apple':{
                    'lands_surface':108,
                    'production': 6455,
                    'condition':'Poor',
                    'productivity':64.6,
                }
            },
            'Land_data':{
                'cultivated land':25282,
                'terre_au_repo':51750,
                'unused land':550 
            }
        } ,
        'ILLIZI':{
            'Products':{
                'Wheat':{
                    'lands_surface':33,
                    'production': 926,
                    'condition':'average',
                    'productivity':28.0,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':1254,
                    'production': 713,
                    'condition':'below average',
                    'productivity':30.2
                },
                'Potatoes':{
                    'lands_surface':3,
                    'production': 417,
                    'condition':'Below average',
                    'productivity':150.0,
                },
                'Tomatoes':{
                    'lands_surface':16,
                    'production': 1766,
                    'condition':'Poor',
                    'productivity':110.0,
                },
                'Greenpepper':{
                    'lands_surface':3,
                    'production':365,
                    'condition':'below average',
                    'productivity':110.0,
                },
                'Aubergines':{
                    'lands_surface':0,
                    'production': 131,
                    'condition':'below average',
                    'productivity':110.0,
                },
                'Onions':{
                    'lands_surface':67,
                    'production':6689,
                    'condition':'below average',
                    'productivity':100.0,
                },
                'Carrots':{
                    'lands_surface':21,
                    'production':2321,
                    'condition':'poor',
                    'productivity':110.1,
                },
                'Lemon':{
                    'lands_surface':57,
                    'production':2338,
                    'condition':'Below average',
                    'productivity':103.8,
                },
                'Olive':{
                    'lands_surface':137,
                    'production':39,
                    'condition':'poor',
                    'productivity':0.9,
                },
                'Apple':{
                    'lands_surface':16,
                    'production': 346,
                    'condition':'Poor',
                    'productivity':28.8,
                }
            },
            'Land_data':{
                'cultivated land':2280,
                'terre_au_repo':418,
                'unused land':17650 
            }
        } ,
        'B.B.ARRERIDJ':{
            'Products':{
                'Wheat':{
                    'lands_surface':64701,
                    'production': 882622,
                    'condition':'Below average',
                    'productivity':14.05,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':82,
                    'production': 20525,
                    'condition':'average',
                    'productivity':250.3,
                },
                'Tomatoes':{
                    'lands_surface':144,
                    'production': 19935,
                    'condition':'Poor',
                    'productivity':138.7,
                },
                'Greenpepper':{
                    'lands_surface':50,
                    'production':4360,
                    'condition':'Poor',
                    'productivity':88.1,
                },
                'Aubergines':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Onions':{
                    'lands_surface':389,
                    'production':71640,
                    'condition':'below average',
                    'productivity':184.2,
                },
                'Carrots':{
                    'lands_surface':33,
                    'production':4970,
                    'condition':'poor',
                    'productivity':150.6,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production':0,
                    'condition':'poor',
                    'productivity':0.0,
                },
                'Olive':{
                    'lands_surface':26319,
                    'production':382316,
                    'condition':'average',
                    'productivity':21.7,
                },
                'Apple':{
                    'lands_surface':166,
                    'production': 3743,
                    'condition':'Poor',
                    'productivity':23.8,
                }
            },
            'Land_data':{
                'cultivated land':116618,
                'terre_au_repo':69821,
                'unused land':10556 
            }
        } ,
        'BOUMERDES':{
            'Products':{
                'Wheat':{
                    'lands_surface':3765,
                    'production': 105690,
                    'condition':'average',
                    'productivity':29.25,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':2486,
                    'production': 772507,
                    'condition':'above average',
                    'productivity':310.7,
                },
                'Tomatoes':{
                    'lands_surface':496,
                    'production': 266412,
                    'condition':'averge',
                    'productivity':536.9,
                },
                'Greenpepper':{
                    'lands_surface':315,
                    'production':76601,
                    'condition':'average',
                    'productivity':243.4,
                },
                'Aubergines':{
                    'lands_surface':367,
                    'production': 82764,
                    'condition':'average',
                    'productivity':225.8,
                },
                'Onions':{
                    'lands_surface':2277,
                    'production':616210,
                    'condition':'average',
                    'productivity':270.7,
                },
                'Carrots':{
                    'lands_surface':398,
                    'production':95565,
                    'condition':'below average',
                    'productivity':240.4,
                },
                'Lemon':{
                    'lands_surface':288,
                    'production':49310,
                    'condition':'average',
                    'productivity':201.2,
                },
                'Olive':{
                    'lands_surface':8348,
                    'production':37303,
                    'condition':'poor',
                    'productivity':4.5,
                },
                'Apple':{
                    'lands_surface':328,
                    'production': 103548,
                    'condition':'above average',
                    'productivity':323.8,
                }
            },
            'Land_data':{
                'cultivated land':42518,
                'terre_au_repo':4786,
                'unused land':23954 
            }
        } ,
        'EL-TARF':{
            'Products':{
                'Wheat':{
                    'lands_surface':21815,
                    'production': 550626,
                    'condition':'average',
                    'productivity':24.7,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0,
                },
                'Potatoes':{
                    'lands_surface':591,
                    'production': 203600,
                    'condition':'above average',
                    'productivity':344.8,
                },
                'Tomatoes':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'Poor',
                    'productivity':0.0,
                },
                'Greenpepper':{
                    'lands_surface':180,
                    'production': 25290,
                    'condition':'below average',
                    'productivity':140.5,
                },
                'Aubergines':{
                    'lands_surface':43,
                    'production': 6000,
                    'condition':'below average',
                    'productivity':139.5,
                },
                'Onions':{
                    'lands_surface':1230,
                    'production':207980,
                    'condition':'below average',
                    'productivity':169.1,
                },
                'Carrots':{
                    'lands_surface':0,
                    'production':0,
                    'condition':'poor',
                    'productivity':0.0,
                },
                'Lemon':{
                    'lands_surface':159,
                    'production':23390,
                    'condition':'average',
                    'productivity':233.9,
                },
                'Olive':{
                    'lands_surface':3371,
                    'production':57830,
                    'condition':'average',
                    'productivity':21.3,
                },
                'Apple':{
                    'lands_surface':153,
                    'production': 21495,
                    'condition':'below average',
                    'productivity':175.5,
                }
            },
            'Land_data':{
                'cultivated land':47684,
                'terre_au_repo':20789,
                'unused land':1340 
            }
        },








    
    ###############################################################
    ###############################################################
        
    ###############################################################
    ###############################################################
        
        'TINDOUF':{
            'Products':{
                'Wheat':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':464,
                    'production': 11330,
                    'condition':'Below average',
                    'productivity':27.3,
                },
                'Potatoes': {
                    'lands_surface': 5,
                    'production': 840,
                    'condition': 'Below average',
                    'productivity': 168.0
                },
                'Tomatoes': {
                'lands_surface': 7,
                'production': 4440,
                'condition': 'Above average',
                'productivity': 672.7
                },
                'Greenpepper': {
                    'lands_surface': 2,
                    'production': 900,
                    'condition': 'Ideal',
                    'productivity': 500.0
                },
                'Aubergines':{
                    'lands_surface': 0,
                    'production': 400,
                    'condition': 'Ideal',
                    'productivity': 2500.0
                },
                'Onions': {
                'lands_surface': 9,
                'production': 1955,
                'condition': 'Average',
                'productivity': 230.0
                },
                'Carrots': {
                    'lands_surface': 3,
                    'production': 813,
                    'condition': 'Below average',
                    'productivity': 250.0
                },
                'Lemons': {
                    'lands_surface': 0,
                    'production': 0,
                    'condition': 'NULL',
                    'productivity': 0.0
                },
                'Olives': {
                    'lands_surface': 148,
                    'production': 0,
                    'condition': 'Ideal',
                    'productivity': 'Poor'
                },
                'Apples': {
                    'lands_surface': 0,
                    'production': 0,
                    'condition': 'NULL',
                    'productivity': 0.0
                }

            },
            'Land_data':{
                'cultivated land':805,
                'terre_au_repo':67,
                'unused land':1628
            }
        },
        'TISSEMSILT':{
            'Products':{
                'Wheat':{
                    'lands_surface':60500,
                    'production': 1053147,
                    'condition':'Below average',
                    'productivity':17.2,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 275,
                    'production': 71816,
                    'condition': 'Average',
                    'productivity': 261.6
                },
                'Tomatoes': {
                    'lands_surface': 112,
                    'production': 28884,
                    'condition': 'Below average',
                    'productivity': 257.9
                },
                'Greenpepper': {
                    'lands_surface': 37,
                    'production': 1263,
                    'condition': 'Poor',
                    'productivity': 34.1
                },
                'Aubergines':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Onions': {
                    'lands_surface': 263,
                    'production': 70180,
                    'condition': 'Average',
                    'productivity': 266.8
                },
                'Carrots': {
                    'lands_surface': 15,
                    'production': 833,
                    'condition': 'Poor',
                    'productivity': 57.4
                },
                'Lemons': {
                            'lands_surface': 0,
                            'production': 0,
                            'condition': 'NULL',
                            'productivity': 0.0
                },
                'Olives': {
                            'lands_surface': 8370,
                            'production': 92000,
                            'condition': 'Below average',
                            'productivity': 14.0
                },
                'Apples': {
                            'lands_surface': 1232,
                            'production': 66886,
                            'condition': 'Poor',
                            'productivity': 54.3
                }

                
            },
            'Land_data':{
                'cultivated land':110901,
                'terre_au_repo':34556,
                'unused land':1628
            }
        },
        'EL-OUED':{
            'Products':{
                'Wheat':{
                    'lands_surface':8200,
                    'production': 260640,
                    'condition':'Above average',
                    'productivity':36.2,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':38147,
                    'production': 2752100,
                    'condition':'Above average',
                    'productivity':72.1,
                },
                'Potatoes': {
                    'lands_surface': 37000,
                    'production': 12140000,
                    'condition': 'Above average',
                    'productivity': 328.1
                },
                'Tomatoes': {
                    'lands_surface': 3397,
                    'production': 2398000,
                    'condition': 'Above average',
                    'productivity': 705.9
                },          
                'Greenpepper': {
                    'lands_surface': 119,
                    'production': 42700,
                    'condition': 'Above average',
                    'productivity': 358.8
                },
                'Aubergines':{
                    'lands_surface': 151,
                    'production': 38435,
                    'condition': 'Average',
                    'productivity': 254.5
                },
                'Onions': {
                    'lands_surface': 2000,
                    'production': 600000,
                    'condition': 'Above average',
                    'productivity': 300.0
                },
                'Carrots':{
                    'lands_surface':648,
                    'production': 74607,
                    'condition':'Poor',
                    'productivity':115.2,
                },
                'Lemon':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Olive':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Apple':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                }
            },
            'Land_data':{
                'cultivated land':89176,
                'terre_au_repo':7300,
                'unused land':253400

            }
        },
        'KHENCHELA':{
            'Products':{
                'Wheat':{
                    'lands_surface':57500,
                    'production': 1010000,
                    'condition':'Average',
                    'productivity':20.15,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':812,
                    'production': 83870,
                    'condition':'Above average',
                    'productivity':71.2,
                },
                'Potatoes': {
                    'lands_surface': 114,
                    'production': 26930,
                    'condition': 'Average',
                    'productivity': 237.3
                },
                'Tomatoes': {
                    'lands_surface': 304,
                    'production': 136700,
                    'condition': 'Average',
                    'productivity': 449.7
                },          
                'Greenpepper': {
                    'lands_surface': 146,
                    'production': 35132,
                    'condition': 'Average',
                    'productivity': 240.6
                },
                'Aubergines':{
                    'lands_surface': 10,
                    'production': 4000,
                    'condition': 'Ideal',
                    'productivity': 400.0
                },
                'Onions': {
                    'lands_surface': 282,
                    'production': 46740,
                    'condition': 'Below average',
                    'productivity': 166.0
                },
                'Carrots': {
                            'lands_surface': 442,
                            'production': 68083,
                            'condition': 'Poor',
                            'productivity': 154.0
                },
                'Lemons': {
                            'lands_surface': 0,
                            'production': 0,
                            'condition': 'NULL',
                            'productivity': 0.0
                },
                'Olives': {
                            'lands_surface': 4428,
                            'production': 95691,
                            'condition': 'Below average',
                            'productivity': 15.3
                },
                'Apples': {
                            'lands_surface': 5485,
                            'production': 1466355,
                            'condition': 'Above average',
                            'productivity': 346.7
                }

            },
            'Land_data':{
                'cultivated land':141633,
                'terre_au_repo':115794,
                'unused land':77718
            }
        },
        'SOUK-AHRAS':{
            'Products':{
                'Wheat':{
                    'lands_surface':120856,
                    'production': 1890579,
                    'condition':'Below average',
                    'productivity':16.35,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 159,
                    'production': 41465,
                    'condition': 'Average',
                    'productivity': 260.6
                },
                'Tomatoes': {
                    'lands_surface': 311,
                    'production': 86520,
                    'condition': 'Below average',
                    'productivity': 278.2
                },          
                'Greenpepper': {
                    'lands_surface': 119,
                    'production': 4985,
                    'condition': 'Poor',
                    'productivity': 42.1
                },
                'Aubergines':{
                    'lands_surface': 13,
                    'production': 332,
                    'condition': 'Poor',
                    'productivity': 25.5
                },
                'Onions': {
                    'lands_surface': 1200,
                    'production': 176882,
                    'condition': 'Below average',
                    'productivity': 147.4
                },
                'Carrots': {
                            'lands_surface': 10,
                            'production': 400,
                            'condition': 'Poor',
                            'productivity': 40.0
                },
                'Lemons': {
                            'lands_surface': 0,
                            'production': 0,
                            'condition': 'NULL',
                            'productivity': 0.0
                },
                'Olives': {
                            'lands_surface': 8136,
                            'production': 102144,
                            'condition': 'Below average',
                            'productivity': 15.5
                },
                'Apples': {
                            'lands_surface': 444,
                            'production': 24336,
                            'condition': 'Poor',
                            'productivity': 56.5
                }

            },
            'Land_data':{
                'cultivated land':195453,
                'terre_au_repo':58155,
                'unused land':26909
            }
        },
        'TIPAZA':{
            'Products':{
                'Wheat':{
                    'lands_surface':12909,
                    'production': 329079,
                    'condition':'Average',
                    'productivity':27.85,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 1517,
                    'production': 488908,
                    'condition': 'Above average',
                    'productivity': 322.3
                },
                'Tomatoes': {
                    'lands_surface': 2492,
                    'production': 1539070,
                    'condition': 'Above average',
                    'productivity': 617.7
                },
                'Greenpepper': {
                    'lands_surface': 711,
                    'production': 285800,
                    'condition': 'Ideal',
                    'productivity': 402.1
                },
                'Aubergines':{
                    'lands_surface': 459,
                    'production': 143708,
                    'condition': 'Above average',
                    'productivity': 313.1
                },
                'Onions': {
                    'lands_surface': 656,
                    'production': 180949,
                    'condition': 'Average',
                    'productivity': 275.8
    },
                'Carrots': {
                            'lands_surface': 281,
                            'production': 119870,
                            'condition': 'Average',
                            'productivity': 426.6
                },
                'Lemons': {
                            'lands_surface': 476,
                            'production': 97121,
                            'condition': 'Average',
                            'productivity': 262.8
                },
                'Olives': {
                            'lands_surface': 2096,
                            'production': 42244,
                            'condition': 'Below average',
                            'productivity': 10.9
                },
                'Apples': {
                            'lands_surface': 727,
                            'production': 169935,
                            'condition': 'Average',
                            'productivity': 250.8
                }

            },
            'Land_data':{
                'cultivated land':56095,
                'terre_au_repo':5706,
                'unused land':0
            }
        },
        'MILA':{
            'Products':{
                'Wheat':{
                    'lands_surface':88321,
                    'production': 2280300,
                    'condition':'Average',
                    'productivity':30.7,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 1169,
                    'production': 456590,
                    'condition': 'Above average',
                    'productivity': 390.6
                },
                'Tomatoes': {
                    'lands_surface': 210,
                    'production': 71806,
                    'condition': 'Below average',
                    'productivity': 341.2
                },
                'Onions': {
                    'lands_surface': 440,
                    'production': 122520,
                    'condition': 'Average',
                    'productivity': 278.5
                },
                'Greenpepper': {
                    'lands_surface': 122,
                    'production': 34436,
                    'condition': 'Average',
                    'productivity': 282.8
                },
                'Aubergines':{
                    'lands_surface': 17,
                    'production': 7244,
                    'condition': 'Ideal',
                    'productivity': 424.1
                },
                'Carrots': {
                            'lands_surface': 783,
                            'production': 261928,
                            'condition': 'Below average',
                            'productivity': 334.5
                },
                'Lemons': {
                            'lands_surface': 5,
                            'production': 0,
                            'condition': 'Poor',
                            'productivity': 0.0
                },
                'Olives': {
                            'lands_surface': 9778,
                            'production': 138489,
                            'condition': 'Below average',
                            'productivity': 16.3
                },
                'Apples': {
                            'lands_surface': 619,
                            'production': 47880,
                            'condition': 'Poor',
                            'productivity': 82.8
                }

            },
            'Land_data':{
                'cultivated land':150011,
                'terre_au_repo':87546,
                'unused land':16444
            }
        },
        'AIN-DEFLA':{
            'Products':{
                'Wheat':{
                    'lands_surface':60161,
                    'production': 691593,
                    'condition':'Average',
                    'productivity':29.05,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 17008,
                    'production': 6062127,
                    'condition': 'Above average',
                    'productivity': 356.4
                },
                'Tomatoes': {
                    'lands_surface': 595,
                    'production': 512750,
                    'condition': 'Ideal',
                    'productivity': 861.8
                },
                'Onions': {
                    'lands_surface': 1860,
                    'production': 1162040,
                    'condition': 'Ideal',
                    'productivity': 624.8
                },
                'Greenpepper': {
                    'lands_surface': 101,
                    'production': 13580,
                    'condition': 'Below average',
                    'productivity': 133.9
                },
                'Aubergines':{
                    'lands_surface': 56,
                    'production': 13851,
                    'condition': 'Average',
                    'productivity': 247.3
                },

                'Carrots': {
                            'lands_surface': 4,
                            'production': 960,
                            'condition': 'Below average',
                            'productivity': 240.0
                },
                'Lemons': {
                            'lands_surface': 31,
                            'production': 4325,
                            'condition': 'Below average',
                            'productivity': 141.3
                },
                'Olives': {
                            'lands_surface': 6769,
                            'production': 190001,
                            'condition': 'Average',
                            'productivity': 21.7
                },
                'Apples': {
                            'lands_surface': 691,
                            'production': 117799,
                            'condition': 'Below average',
                            'productivity': 180.5
                }

            },
            'Land_data':{
                'cultivated land':151418,
                'terre_au_repo':30258,
                'unused land':15963
            }
        },
        'NAAMA':{
            'Products':{
                'Wheat':{
                    'lands_surface':790,
                    'production': 8184,
                    'condition':'Below average',
                    'productivity':15.15,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':253,
                    'production': 6505,
                    'condition':'Below average',
                    'productivity':29.7,
                },
                'Potatoes': {
                    'lands_surface': 423,
                    'production': 103440,
                    'condition': 'Average',
                    'productivity': 244.5
                },
                'Tomatoes': {
                    'lands_surface': 75,
                    'production': 20514,
                    'condition': 'Below average',
                    'productivity': 273.5
                },
                'Onions': {
                    'lands_surface': 323,
                    'production': 62479,
                    'condition': 'Below average',
                    'productivity': 193.4
                },
                'Greenpepper': {
                    'lands_surface': 105,
                    'production': 9741,
                    'condition': 'Poor',
                    'productivity': 92.8
                },
                'Aubergines':{
                    'lands_surface': 71,
                    'production': 7612,
                    'condition': 'Below average',
                    'productivity': 107.2
                },

                'Carrots': {
                            'lands_surface': 274,
                            'production': 45804,
                            'condition': 'Poor',
                            'productivity': 167.5
                },
                'Lemons': {
                            'lands_surface': 1,
                            'production': 25,
                            'condition': 'Poor',
                            'productivity': 50.0
                },
                'Olives': {
                            'lands_surface': 2067,
                            'production': 8058,
                            'condition': 'Poor',
                            'productivity': 3.7
                },
                'Apples': {
                            'lands_surface': 26,
                            'production': 998,
                            'condition': 'Poor',
                            'productivity': 41.6
                }

            },
            'Land_data':{
                'cultivated land':12406,
                'terre_au_repo':15877,
                'unused land':60
            }
        },
        'A.TEMOUCHENT':{
            'Products':{
                'Wheat':{
                    'lands_surface':33,
                    'production': 9100,
                    'condition':'Ideal',
                    'productivity':275.8,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 244,
                    'production': 72455,
                    'condition': 'Average',
                    'productivity': 296.9
                },
                'Tomatoes': {
                    'lands_surface': 957,
                    'production': 341574,
                    'condition': 'Below average',
                    'productivity': 356.9
                },
                'Onions': {
                    'lands_surface': 1945,
                    'production': 439790,
                    'condition': 'Average',
                    'productivity': 226.1
                },
                'Greenpepper': {
                    'lands_surface': 281,
                    'production': 65444,
                    'condition': 'Average',
                    'productivity': 232.8
                },
                'Aubergines':{
                    'lands_surface': 120,
                    'production': 28755,
                    'condition': 'Average',
                    'productivity': 240.3
                },
                'Carrots': {
                            'lands_surface': 1283,
                            'production': 274420,
                            'condition': 'Below average',
                            'productivity': 213.9
                },
                'Lemons': {
                            'lands_surface': 2,
                            'production': 185,
                            'condition': 'Below average',
                            'productivity': 123.3
                },
                'Olives': {
                            'lands_surface': 5124,
                            'production': 117568,
                            'condition': 'Below average',
                            'productivity': 16.5
                },
                'Apples': {
                            'lands_surface': 224,
                            'production': 6502,
                            'condition': 'Poor',
                            'productivity': 29.6
                }

            },
            'Land_data':{
                'cultivated land':166317,
                'terre_au_repo':14677,
                'unused land':14616
            }
        },
        'GHARDAIA':{
            'Products':{
                'Wheat':{
                    'lands_surface':6060,
                    'production': 235000,
                    'condition':'Above average',
                    'productivity':38.8,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':11359,
                    'production': 604000,
                    'condition':'Average',
                    'productivity':52.9,
                },

                'Potatoes': {
                    'lands_surface': 490,
                    'production': 143000,
                    'condition': 'Average',
                    'productivity': 291.8
                },
                'Tomatoes': {
                    'lands_surface': 30,
                    'production': 4359,
                    'condition': 'Poor',
                    'productivity': 145.3
                },
                'Onions': {
                    'lands_surface': 715,
                    'production': 132400,
                    'condition': 'Below average',
                    'productivity': 185.2
                },

                'Greenpepper': {
                    'lands_surface': 76,
                    'production': 13600,
                    'condition': 'Below average',
                    'productivity': 178.9
                },
                'Aubergines':{
                    'lands_surface': 160,
                    'production': 33590,
                    'condition': 'Average',
                    'productivity': 209.9
                },
                'Carrots': {
                            'lands_surface': 300,
                            'production': 43480,
                            'condition': 'Poor',
                            'productivity': 144.9
                },
                'Lemons': {
                            'lands_surface': 420,
                            'production': 34440,
                            'condition': 'Below average',
                            'productivity': 107.6
                },
                'Olives': {
                            'lands_surface': 1880,
                            'production': 25818,
                            'condition': 'Below average',
                            'productivity': 13.3
                },
                'Apples': {
                            'lands_surface': 251,
                            'production': 10339,
                            'condition': 'Poor',
                            'productivity': 49.0
                }

            },
            'Land_data':{
                'cultivated land':26715,
                'terre_au_repo':37670,
                'unused land':172
            }
        },
        'RELIZANE':{
            'Products':{
                'Wheat':{
                    'lands_surface':99929,
                    'production': 193101,
                    'condition':'Below average',
                    'productivity':14.75,
                },
                'Corn':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Dates':{
                    'lands_surface':0,
                    'production': 0,
                    'condition':'NULL',
                    'productivity':0,
                },
                'Potatoes': {
                    'lands_surface': 2718,
                    'production': 795240,
                    'condition': 'Average',
                    'productivity': 292.6
                },
                'Tomatoes': {
                    'lands_surface': 308,
                    'production': 96815,
                    'condition': 'Below average',
                    'productivity': 314.8
                },
                'Onions': {
                    'lands_surface': 392,
                    'production': 69970,
                    'condition': 'Below average',
                    'productivity': 178.5
                },
                'Greenpepper': {
                    'lands_surface': 105,
                    'production': 13828,
                    'condition': 'Below average',
                    'productivity': 132.3
                },
                'Aubergines':{
                    'lands_surface': 78,
                    'production': 10230,
                    'condition': 'Below average',
                    'productivity': 131.2
                },
                'Carrots': {
                            'lands_surface': 100,
                            'production': 9300,
                            'condition': 'Poor',
                            'productivity': 93.0
                },
                'Lemons': {
                            'lands_surface': 136,
                            'production': 34600,
                            'condition': 'Average',
                            'productivity': 254.4
                },
                'Olives': {
                            'lands_surface': 7079,
                            'production': 430633,
                            'condition': 'above average',
                            'productivity': 44.1
                },
                'Apples': {
                            'lands_surface': 182,
                            'production': 24491,
                            'condition': 'Below average',
                            'productivity': 134.9
                }

            },
            'Land_data':{
                'cultivated land':210316,
                'terre_au_repo':71559,
                'unused land':9450
            }
        },
        }
#
"""
state = {
    'wilaya_1' = {
        'Products' = {
            p_1 = {
                'productivity'
                'condition'
            }
        }
    }

}
"""



for key in state['wilayas']: #here key is wilaya name
    for value2 in state['wilayas'][key]['Products']: #here value2 are product names 
        value = state['wilayas'][key]['Products'][value2]#value is the actual state

        if value2 == "Wheat":
            if value['productivity'] < 10:
                if value['condition'] != 'Poor' and value['condition'] != 'NULL':
                     print(key," EROOR WHEAT")
            elif value['productivity'] >= 10 and value['productivity'] < 20:
                 if value['condition'] != 'Below average':
                      print(key," ERROR WHEAT")
            elif value['productivity'] >= 20 and value['productivity'] < 35:
                 if value['condition'] != 'Average':
                      print(key," ERROR WHEAT")
            elif value['productivity'] >= 35 and value['productivity'] < 50:
                 if value['condition'] != 'Above average':
                      print(key," ERROR WHEAT")
            elif value['productivity'] >= 50:
                 if value['condition'] != 'Ideal':
                      print(key," ERROR WHEAT")
##########################
        if value2 == "Corn" or value2 == "Dates":
            if value['productivity'] < 20:
                if value['condition'] != 'Poor' and value['condition'] != 'NULL':
                     print(key," ERROR CornDate")
            elif value['productivity'] >= 20 and value['productivity'] < 40:
                 if value['condition'] != 'Below average':
                      print(key," ERROR CornDate")
            elif value['productivity'] >= 40 and value['productivity'] < 60:
                 if value['condition'] != 'Average':
                      print(key," ERROR CornDate")
            elif value['productivity'] >= 60 and value['productivity'] < 80:
                 if value['condition'] != 'Above average':
                      print(key," ERROR CornDate")
            elif value['productivity'] >= 80:
                 if value['condition'] != 'Ideal':
                      print(key," ERROR CornDate")
##########################
        if value2 == "Potatoes" or value2 == "Greenpepper" or value2 == "Aubergines"or value2 == "Onions"or value2 == "Lemon"or value2 == "Apple":
            if value['productivity'] < 100:
                if value['condition'] != 'Poor' and value['condition'] != 'NULL':
                     print(key,value2," ERROR potatoeGreenAUOnLemApp")
            elif value['productivity'] >= 100 and value['productivity'] < 200:
                 if value['condition'] != 'Below average':
                      print(key,value2," ERROR potatoeGreenAUOnLemApp")
            elif value['productivity'] >= 200 and value['productivity'] < 300:
                 if value['condition'] != 'Average':
                      print(key,value2," ERROR potatoeGreenAUOnLemApp")
            elif value['productivity'] >= 300 and value['productivity'] < 400:
                 if value['condition'] != 'Above average':
                      print(key,value2," ERROR potatoeGreenAUOnLemApp")
            elif value['productivity'] >= 400:
                 if value['condition'] != 'Ideal':
                      print(key,value2," ERROR potatoeGreenAUOnLemApp")
##########################
        if value2 == "Tomatoes" or value2 == "Carrots":
            if value['productivity'] < 200:
                if value['condition'] != 'Poor' and value['condition'] != 'NULL':
                     print(key,value2," ERROR Carrots Tomatoes")
            elif value['productivity'] >= 200 and value['productivity'] < 400:
                 if value['condition'] != 'Below average':
                      print(key,value2," ERROR Carrots Tomatoes")
            elif value['productivity'] >= 400 and value['productivity'] < 600:
                 if value['condition'] != 'Average':
                      print(key,value2," ERROR Carrots Tomatoes")
            elif value['productivity'] >= 600 and value['productivity'] < 800:
                 if value['condition'] != 'Above average':
                      print(key,value2," ERROR Carrots Tomatoes")
            elif value['productivity'] >= 800:
                 if value['condition'] != 'Ideal':
                      print(key,value2," ERROR Carrots Tomatoes")
##########################
        if value2 == "Olive":
            if value['productivity'] < 10:
                if value['condition'] != 'Poor' and value['condition'] != 'NULL':
                     print(key," ERROR Olives")
            elif value['productivity'] >= 10 and value['productivity'] < 20:
                 if value['condition'] != 'Below average':
                      print(key," ERROR Olives")
            elif value['productivity'] >= 20 and value['productivity'] < 40:
                 if value['condition'] != 'Average':
                      print(key," ERROR Olives")
            elif value['productivity'] >= 40 and value['productivity'] < 60:
                 if value['condition'] != 'Above average':
                      print(key," ERROR Olives")
            elif value['productivity'] >= 60:
                 if value['condition'] != 'Ideal':
                      print(key," ERROR Olives")
