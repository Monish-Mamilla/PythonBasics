# we are using default value for height incase user doesn't supply the input value
def find_cylinder_volume(radius, height=7) :
     
     volume = 3.14 * (radius ** 2) * height

     return volume

# *args is converts into tuple 
def sum_all(*args) :
     
    total = 0

    for num in args  :
          total +=num

    return total 

# **kwargs is convert into Dictonary (key, value pairs)
def company_info(**kwargs) :
    
    # if 'ticker' in kwargs:
    #     print(f"Ticker: {kwargs['ticker']}")
    # if 'ceo' in kwargs:
    #     print(f"CEO: {kwargs['ceo']}")
    
    # if 'revenue' in kwargs:
    #     print(f"Revenue: {kwargs['revenue']}")
    # We will write in short form

    for key in kwargs :
         print(f"{key}  {kwargs[key]}")

# we will use pass when ever you don't return anything
def foo() :
     pass
  
if __name__ == "__main__" :
     
    v1 =  find_cylinder_volume(radius=5)

    print (f"Volume is {v1}")

    v2 = find_cylinder_volume(radius=5,height=6)

    print(f"Volume for the cylinder { v2}")

    total = sum_all(1,2,3,4,5,6,7)

    print(f"Total is {total}")

    company_info(ticker='AAPL',ceo='Tim Cook',revenue="200 billions")
   
    # Lambda's allows to use to create functions in the simple way - here value is the input value
    area = lambda value: value * value

    print(f"Area is {area(5)}")

    # Lambda with two inputs

    sum_two = lambda a,b : a+b

    print(f"Sum of two numbers {sum_two(50,20)}")