import datetime # importuojama datetime biblioteka

name = input("Input you name: ")
age = int(input("How old are you ? : ")) # Kiek metų turi klausiamasis
birthday = input("You birthday was until now (please answer Yes or No) ? : ") # Klausiama ar buvo iki šio laiko gimtadienis

date_now = datetime.datetime.now() # Nustatoma dabartinė data

# Pagal atsakymą kada buvo gimtadienis, tikrinamos sąlygos
if birthday == 'Yes':
    date_of_birth = int(date_now.strftime("%Y")) - age  # int(date_now.strftime("%Y")) Dabartinė data formatuojama taip kad būtų naudojami tik metai
    print(f"{name} you year of birth is {date_of_birth}") # ir atimami tik turimi metai, nes gimtadienis jau buvo šiais metais
if birthday == 'No':
    date_of_birth = int(date_now.strftime("%Y")) - age - 1 # int(date_now.strftime("%Y")) dabartinė data formatuojama taip kad būtų naudojami tik metai
    print(f"{name} you year of birth is {date_of_birth}") # ir atimami turimi metai ir dar vieni metai nes gimtadienio dar nebuvo šiais metais