def round_off(number:float, place:int):
    """
    upto $place decimal places
    """
    place -= 1
    number_part, decimal_part = list(str(number).split('.'))
    # print("Number part:", number_part, " Decimal part:", decimal_part)
    decimal_part = list(decimal_part)
    
    m_place = decimal_part[place]
    m_1_place = decimal_part[place+1]
    
    if int(m_1_place) > 5:
        decimal_part[place] = str(int(m_place) + 1)
    
    elif int(m_1_place) < 5:
        pass
    
    elif int(m_1_place) == 5:
        if int(m_place) % 2 == 0:  # number is even
            pass
        else:  # number is odd
            decimal_part[place] = str(int(m_place)+1)
    
    return float(number_part + "." + "".join(decimal_part[:place+1]))

def round_off_significant_digit(number, signification_digit):
    if "." in str(number):
        number = str(number)[:signification_digit+2]  # +1 for the decimal symbol
        if len(number.split('.')[-1]) > 0:
            return round_off(number, len(number) - signification_digit - 1)
        else:
            return int(number.split('.'))[0]
    else:
        return number

dec_place = 2
nr, dec_place = 23.246, 2
# nr, dec_place = 0.025355, 4
# nr, dec_place = 12.372, 3
# nr, dec_place = 6300, 3
# ans = round_off(nr, dec_place)
# print(f"rounded off to {dec_place} places: {ans}")
ans = round_off_significant_digit(nr, dec_place)
print(f"Rounded off to {dec_place} significant digits:", ans)