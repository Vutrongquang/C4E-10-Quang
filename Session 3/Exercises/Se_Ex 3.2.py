
sheep_size = [5, 7, 300, 24, 90, 50, 75]

your_name = input("Your name: ")

print("Hello, my name is ", your_name, "and, these are my ship sizes", sheep_size)

##for x in range (4):
##    print("Month", x)
##    i = 50

while True:
    
    month_no = int(input("Month No = "))
    for i in range (month_no):

        print("MONTH: ", month_no)
        
        add_sheep = [x + month_no * 50 for x in sheep_size]
        print("One month has passed, now here is my flock", add_sheep)
        
        biggest_sheep = max(add_sheep)
        print("my biggest sheep has size", biggest_sheep, "let's sheer it")

        add_sheep.remove(biggest_sheep)
        print("After shearing, here is my flock", add_sheep)

    print ("My flock has size in total: ", sum(add_sheep))
    print ("I would get", sum(add_sheep) * 2,"$")
