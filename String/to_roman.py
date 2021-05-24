def convertRoman(n):
    #Code here
    roman_values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_string = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    result = n
    roman = ""
    while result > 0:
        for index,i in enumerate(roman_values):
            if result >= i and result >= 0:
                result -= i
                roman += roman_string[index]
                break
            elif result <= 0:
                break
    return roman

if __name__ == "__main__":
    n = int(input())
    print(convertRoman(n))
