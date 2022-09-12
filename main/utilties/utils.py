def format_card(card):
    '''
        formating the card gets rid of all unnecessary charecters
        like spaces dash comma basiclly anything non-decimal.
    '''
    formatted_card = ''
    for i in range(len(card)):
        if card[i].isdecimal():
            formatted_card += card[i]
    return formatted_card

def format_float(num):
    '''
        it returns 2 decimal point digit.
    '''
    return float(str(num)[:4:])

# get the currency and amount
def extract(money, index):
    '''
        Extract currency and  money from input string
    '''
    li_money = list(money)
    li_money.pop(li_money.index('$'))
    money = ''
    for i in li_money:
        money += i
    return float(money)

def validate_card(card):
    '''Using Luhn algorithm
        by doubling every odd number and break down every
        double digit number after doubling and sum the total doubled numbers
        and sum all even numbers then the total of odd and even together and
        validate by mod 10(divisible by ten).
    '''
    doubled_nums = 0
    even_nums = 0

    # remove unnecessary charecters
    card = format_card(card)

    # Apply Luhn algorithm
    for i in range(len(card)):
        # Check if index is odd adn double every odd number
        if (i+1)%2 != 0:
            # add each digit in double digits
            if int(card[i])*2 >= 10:
                doubled_nums += int(str(int(card[i])*2)[0])
                doubled_nums += int(str(int(card[i])*2)[1])
            else:
                # add single digits
                doubled_nums += int(card[i])*2
        else:
            # Keep each even number and add it
            even_nums += int(card[i])
    # Adding even and odd totals
    result = doubled_nums + even_nums

    # Check mod 10
    if result%10 == 0:
        return True
    else:
        return False

def get_card_info(card):
    '''
        Look up the Card Number in database and retrive account info
    '''
    for account in fake_credit:
        if account['CardNumber'] == card:
            return account
        else:
            return {}

# Fake generated accounts to simulate actual cards
fake_credit = [{
        "IssuingNetwork": "VISA",
        "CardNumber": "4325-8497-9560-9817",
        "Bank": "ARAB BANK PLC",
        "Name": "Donat Yuan",
        "Address": "43 rue Lon Dierx",
        "Country": "PALESTINIAN TERRITORY, OCCUPIED",
        "MoneyRange": "635",
        "CVV": 189,
        "Expiry": "04/2026",
        "Pin": 2938
    },
    {
        "IssuingNetwork": "VISA",
        "CardNumber": "4585 9051 3062 5309",
        "Bank": "ARAB BANK PLC",
        "Name": "Fatima Chandler",
        "Address": "1375 Halsey Avenue",
        "Country": "PALESTINIAN TERRITORY, OCCUPIED",
        "MoneyRange": "807",
        "CVV": 767,
        "Expiry": "05/2027",
        "Pin": 5179
    },
    {
    "IssuingNetwork": "VISA",
    "CardNumber": "4585896840572610",
    "Bank": "ARAB BANK PLC",
    "Name": "Nayumi McAuley",
    "Address": "7 Gilshennan Valley",
    "Country": "PALESTINIAN TERRITORY, OCCUPIED",
    "MoneyRange": "$593",
    "CVV": 610,
    "Expiry": "02/2023",
    "Pin": 7972
    }]
