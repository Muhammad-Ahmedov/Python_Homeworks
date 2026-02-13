# Lesson 1 Homework by Ahmedov Muhammad
# Attention the information balow mightn't be satisfying because it's only my understanding towards python (by the way I am only at beginner level now)

print("Questions")
print("1. Why do you think companies analyze large volumes of data?")
print("2. If analyzing and sorting large data manually in Excel is difficult, how do you think Python can help solve this problem?")
print("3. Imagine you work at a sales company that receives data about 10,000 customer transactions daily. How would you analyze this data?")
print ("4. In your opinion, what tasks can Python be useful for in BI processes? (e.g., data cleaning, visualization, etc.)")
print("5. If you wanted to compare a company's profit year by year, how could this be done using Python?")
print("6. If you don't know Python, what difficulties might you face when working with large datasets?")

print("Which question  would you like to ask from me?")
choice = input("Choose a question number (1-6):" )

if choice == "1":
    print("Companies analyze large volume of data mainly because this helps them to understand trend and ups and downs of chart. So they can change the way they sell or promote products to become bestseller or overtake their rivals")

elif choice == "2":
    print("Unlike Excel when one needs to write data and compare them manually, people can write corresponding code in python once, which helps them to analyze large volume of date automatically without mistakes and overlooks of minor details.")

elif choice == "3":
    print("First of all, I would use websites such as `pandas` for data manipulation, `matplotlib` or `seaborn` for visualization and then I would write a code which further analyzes and sorts them out by dates and months and years. Next I would convert that trends to charts to us see properly. As a result I can receive charts by only running the same code once every morning. ")

elif choice == "4":
    print("I think python can be used for data cleaning, reporting, visualisation, automation and businnes desicion support.")

elif choice == "5":
    print ("By using python to write code and `pandas` for data manipulation, `matplotlib` or `seaborn` for visualization, I can load yearly data and sort them out and even create graphs such as line graph")

elif choice == "6":
    print("If I don't understand coding in python language, I would need to use Excel in place of it. But, I would need more manpower to complete the task one code will do. Some of which are doing repetitive tasks every day from morning to evening. And more than that Excel couldn't proccess tha data if it were to exceed 2 million")

else:
    print("Please choose a number from 1 to 6")


print("This is an examplary code that I created")

profit1 = int(input("Last year's profit:" ))
profit2 = int(input("This year's profit:" ))

Total = profit1 + profit2
Diffrence = profit2 - profit1
Avarage = Total / 2

print("Total income in last couple years:", Total )
print("The diffrence between both years:", Diffrence)
print("The avarage sales of years:", Avarage)

if Diffrence > 0:
    print("There is an increase in sales")
elif Diffrence == 0:
    print("The profits remained unchanged")

else:
    print("There is a decrease in sales compared to last year" )

