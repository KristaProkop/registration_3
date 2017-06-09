#For each new partnership, add an entry in FORMDICT and specify target in URLS

FIELDS = ['first_name', 'last_name', 'email']

# FORMDICT = {
#     "tmobile":{
#         'pages': {
#           0: [FIELDS[0], FIELDS[1], FIELDS[2]], 
#           1: [FIELDS[2]],
#         },
#         "heading": "First, create your ShopRunner login.",
#         "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
#         },

#     "sprint":{
#         'pages': {
#           0: [FIELDS[0], FIELDS[1]],
#         },
#         "heading": "ShopRunner welcomes Sprint Customers!",
#         "subheading": "Sign up for a free account",
#         },
# }    

FORMDICT = {
    "default":{
        'fields': ( FIELDS[0], FIELDS[1], FIELDS[2] ),
        "heading": "Create your ShopRunner login.",
        "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
        },

    "tmobile":{
        'fields': ( FIELDS[0], FIELDS[1], FIELDS[2] ),
        "heading": "First, create your ShopRunner login.",
        "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
        },

    "sprint":{
        'fields': ( FIELDS[0], FIELDS[1] ),
        "heading": "ShopRunner welcomes Sprint Customers!",
        "subheading": "Sign up for a free account",
        },
}    

URLSDICT = {
  '/tmobile/': FORMDICT['tmobile'],
  '/modal_demo/1/': FORMDICT['sprint'],
  '/from/somewhere/else/tmobile/': FORMDICT['tmobile'],
  '/sprint/': FORMDICT['sprint'],
  '/main/': FORMDICT['tmobile'],
}

