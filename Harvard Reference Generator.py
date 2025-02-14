#welcome to the harvard Generator:

import time

Author = input("Authors name's first intial and their surname:")
Year_of_publication = int(input("Year of Publication:"))
Title_of_website_article = input("Please enter the Title of website/ Articel: ")

viewdate = int(input("The date you viewed the article:"))
month = int(input("Please input the month you read this article:"))

Year = int(input("Please input the Year you read this article:"))

URL_or_titleofthebook = input("Please enter the URL or the title of the book:") 

print()
time.sleep(1.2)

if month == 1:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"January",Year,",",URL_or_titleofthebook)

elif month == 2:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"February",Year,",",URL_or_titleofthebook)

elif month == 3:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"March",Year,",",URL_or_titleofthebook)

elif month == 4:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"April",Year,",",URL_or_titleofthebook)

elif month == 5:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"May",Year,",",URL_or_titleofthebook)

elif month == 6:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"June",Year,",",URL_or_titleofthebook)

elif month == 7:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"July",Year,",",URL_or_titleofthebook)    


elif month == 8:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"August",Year,",",URL_or_titleofthebook)        

elif month == 9:    
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"september",Year,",",URL_or_titleofthebook)     

elif month == 10:    
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"October",Year,",",URL_or_titleofthebook)     

elif month == 11:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"November",Year,",",URL_or_titleofthebook)     

elif month == 12:
    print("-----------------------------------------------------------")
    print(Author,",",Year_of_publication,",",Title_of_website_article, ",",
URL_or_titleofthebook,",","Viewed on",viewdate,"December",Year,",",URL_or_titleofthebook)     

else:
    print("Your month is invalid there are only 12 months")
