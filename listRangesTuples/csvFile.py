import csv, math, xlsx
book= open("book.csv")
reader = csv.reader(book)  
for item in reader:
        Serial_number, organization_name, url, What_Univelcity_can_offer, Benefit_of_Organization, Offer_avialable  = item
        print(f"Origin:{Serial_number}, destination: {organization_name}, duration:{What_Univelcity_can_offer}")