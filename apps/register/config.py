#For each new partnership, create an entry in FORMDICT and specify associated url in URLSDICT

USER_FIELDS = ['first_name', 'last_name', 'email', 'password']
CREDIT_CARD_FIELDS = ['card_num', 'expiry', 'cvv']


FORMDICT = {
    "default":{
        'user_fields': ( USER_FIELDS[2], USER_FIELDS[3] ),
        'credit_card_fields': (),
        "heading": "Free 2-Day Shipping",
        "subheading": "After your free trial ends, you will be billed one payment of $79 for a 12 month plan or $8.95 for a monthly plan. Your membership will be automatically renewed to the same term until you cancel or set your account to 'do not renew.'",
        "button_text": "add payment",
        },

    "amex":{
        'user_fields': ( USER_FIELDS[0], USER_FIELDS[1], USER_FIELDS[2] ),
        'credit_card_fields': (CREDIT_CARD_FIELDS[0], CREDIT_CARD_FIELDS[1]),
        "heading": "ShopRunner welcomes Amex Customers!",
        "subheading": "Sign up for a free account",
        "button_text": "Verify & enroll now"
        },

    "tmobile":{
        'user_fields': (  USER_FIELDS[0], USER_FIELDS[1], USER_FIELDS[2], USER_FIELDS[3] ),
        'credit_card_fields': (),
        "heading": "Create your ShopRunner login.",
        "subheading": "You will use the email address below to sign in when you see the ShopRunner logo at top online retailers.",
        "button_text": "enroll now",
        },
}   

URLSDICT = {
  '/amex/': FORMDICT['amex'],
  '/tmobile/': FORMDICT['tmobile'],
  '/register/tmobile/': FORMDICT['tmobile']
}

