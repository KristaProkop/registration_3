#For each new partnership, create an entry in FORMDICT and specify associated url in URLSDICT

USER_FIELDS = ['first_name', 'last_name', 'email', 'password']
CREDIT_CARD_FIELDS = ['card_num', 'expiry', 'cvv']


FORMDICT = {
    "default":{
        'user_fields': ( USER_FIELDS[2], ),
        'credit_card_fields': (),
        "heading": "Create your ShopRunner login.",
        "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
        },

    "amex":{
        'user_fields': ( USER_FIELDS[0], USER_FIELDS[1], USER_FIELDS[2] ),
        'credit_card_fields': (CREDIT_CARD_FIELDS[0], CREDIT_CARD_FIELDS[1]),
        "heading": "ShopRunner welcomes Amex Customers!",
        "subheading": "Sign up for a free account",
        },

    "tmobile":{
        'user_fields': (  USER_FIELDS[0], USER_FIELDS[1], USER_FIELDS[2], USER_FIELDS[3] ),
        'credit_card_fields': (),
        "heading": "Create your ShopRunner login.",
        "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
        },
}   

URLSDICT = {
  '/amex/': FORMDICT['amex'],
  '/tmobile/': FORMDICT['tmobile'],
}

