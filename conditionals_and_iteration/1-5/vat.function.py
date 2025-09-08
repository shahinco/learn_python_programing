def calculate_price_with_vat(price, vat):
    return price * (100 + vat) / 100

price = input("Please add the price: ")
vat = input("What is VAT procentage? ")

print(f"final price: " calculate_price_with_vat() )