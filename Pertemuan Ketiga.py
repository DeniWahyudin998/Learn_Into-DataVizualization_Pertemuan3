##Python Function

def my_function(p, l):
    "Function untuk mengitung luas"
    print(p * l)
my_function(2,4)
 
############################################################
   
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return
 
############################################################
   

##Calling a Function
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")
 
############################################################
   

##Pass by reference vs value
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = ([10,20,30]);
mylist = ([40,50,60]);
changeme( mylist );
print("Values outside the function: ", mylist)
 
############################################################
   

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print("Values outside the function: ", mylist)
 
############################################################
   
##Function Arguments
##Required arguments
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme()

 
############################################################
   

##Keyword arguments
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = "Hacktiv8")

def printme( str ):
   "This prints a passed string into this function"
   print(str)
   return;

# Now you can call printme function
printme(str = 123)

 
############################################################
   

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=4, name="a" )

# Function definition is here
def printinfo( name, nilai_1 , nilai_2 , nilai_3 , nilai_4 ,nakhir ):
   "This prints a passed info into this function"
   
   print("Name: ", name)
   print("Nilai 1: ", nilai_1)
   print("Nilai 2: ", nilai_2)
   print("Nilai 3: ", nilai_3)
   print("Nilai 4: ", nilai_4)
   nakhir = (nilai_1*0.1)+(nilai_2*0.2)+(nilai_3*0.3)+(nilai_4*0.4)
   print("Nilai Akhir: ", nakhir)
   return;

# Now you can call printinfo function
printinfo( name="Deni Wahyudin", nilai_1 = 100, nilai_2 = 80, nilai_3 = 75, nilai_4 = 88, nakhir= 0 )
 
############################################################
   

##Default arguments
# Function definition is here
def printinfo( name, age = 26 ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age: ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

############################################################

##Variable-length arguments
def functionname([formal_args] #var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]


# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(vartuple)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

##############################################################

##The Anonymous Functions
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

#def sum(arg1, arg2):
#    arg1 + arg2
    
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# Function definition is here
sum = lambda arg1, arg2, arg3, arg4 : arg1 + arg2 + arg3 + arg4;

#def sum(arg1, arg2):
#    arg1 + arg2
    
# Now you can call sum as a function
print("Nilai Akhir : ", sum( 10, 20, 30, 40 ))

#########################################################

##The return Statement
# Function definition is here
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    total2 = total + arg1
    print("Inside the function : ", total)
    return total2

# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)

#######################################################

##Scope of Variables
##Global vs. Local variables

total = 0; 

def sum( arg1, arg2 ):

   total = arg1 + arg2; 
   print("Inside the function local total : ", total)
   return total;

def min():
    

    sum( 10, 20 );
print("Outside the function global total : ", total)


jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing

jumlahHewan()
jumlahKelinci()

jumlahKucing = 20
jumlahAnjing = 10

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing


jumlahKelinci()
jumlahHewan()

jumlahKucing = 20

def jumlahHewan():
    jumlahAnjing = 30
    return jumlahKucing + jumlahAnjing

def jumlahKelinci():
    return jumlahKucing + jumlahKucing


(jumlahKelinci(),
jumlahHewan(),
jumlahKelinci() + jumlahHewan()
)

#######################################################