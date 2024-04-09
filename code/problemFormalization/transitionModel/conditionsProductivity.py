"""
this files contains a dictionnary used to map each condition with the right productivity

we use the random function and we give it a range to simulate what happens in real life: if good conditions
are provided for the plants we can predict the range of the productivity (rondement) but not the exact number
"""
import random


map_condition_productivity  = { 
        'Wheat': {
            'poor': random.uniform (0,10), 
            'below average': random.uniform (10,20),
            'average': random.uniform (20,35),
            'above average': random.uniform (35,50),
            'ideal': random.uniform (50,90),
        },
        'Corn': {
            'poor': random.uniform (0,20),
            'below average': random.uniform (20,40),
            'average': random.uniform (40,60),
            'above average':random.uniform (60,80),
            'ideal': random.uniform(80,150)
        },
        'Dates': {
            'poor': random.uniform (0,20),
            'below average':random.uniform (20,40),
            'average': random.uniform (40,60),
            'above average': random.uniform (60,80),
            'ideal': random.uniform(80,180)
        },
        'Potatoes': {
            'poor': random.uniform (0,100),
            'below average':random.uniform (100,200), 
            'average':random.uniform (200,300),
            'above average': random.uniform (300,400),
            'ideal': random.uniform(400,500)
        },
        'Tomatoes': {
            'poor': random.uniform (0,200),
            'below average':random.uniform (200,400),
            'average': random.uniform (400,600),
            'above average':random.uniform (600,800), 
            'ideal': random.uniform(800,1000)
        },
        'Greenpepper': {
            'poor': random.uniform (0,100),
            'below average': random.uniform (100,200),
            'average': random.uniform (200,300),
            'above average': random.uniform (300,400),
            'ideal': random.uniform(400,500)
        },
        'Aubergines': {
            'poor':random.uniform(0,100),
            'below average':random.uniform(100,200), 
            'average':random.uniform(200,300),
            'above average':random.uniform(300,400),
            'ideal':random.uniform(400,600),
        },
        'Onions': {
            'poor':random.uniform(0,100), 
            'below average':random.uniform(100,200),
            'average':random.uniform(200,300),
            'above average':random.uniform(300,400),
            'ideal':random.uniform(400,600)
        },
        'Carrots': {
            'poor':random.uniform(0,200), 
            'below average':random.uniform(200,400),
            'average':random.uniform(400,600),
            'above average':random.uniform(600,800), 
            'ideal':random.uniform(800,1000)
        },
        'Lemon': {
            'poor':random.uniform(0,100), 
            'below average':random.uniform(100,200), 
            'average':random.uniform(200,300),
            'above average':random.uniform(300,400),
            'ideal':random.uniform(400,500),
        },
        'Apple': {
            'poor':random.uniform(0,100), 
            'below average':random.uniform(100,200),
            'average':random.uniform(200,300),
            'above average':random.uniform(300,400),
            'ideal':random.uniform(400,500)
        }

}

    
        