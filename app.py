print('01:'"\nHELLO DANISH HOW ARE YOU.\n")
#strat 
print('02:'"\nDANISH AHMED\n".lower())
print("\ndanish ahmed\n".upper())
print("\ndanish ahmed\n".title())
#end  

#strat  
print('03:'"\nDanish Ahmed"",""said"'"'"Success is not final, failure is not fatal: It is the courage to continue that counts."'"'"\n")
#end

#start
print('04:'"\n""Quaid-e-Azam"",""said"'"'"work work just work"'"'"\n")
#end

#start
print('05:'"\t \n sir zia khan\t \n")
#end

#start
print("\n06:")
print("Addition:", 5 + 3)
print("Subtraction:", 12-4)
print("Multiplication:", 2*4)
print("Division:",32/4)
#end

#start
print('07:'"\n \tconsole.log:5 + 3\t"
"\tconsole.log:10 - 2\t"
"\tconsole.log:4 * 2\t"
"\tconsole.log:32 / 4 \n \t")
#end

#star
print('08:'"\n"'"'"My fauorite no is(03)."'"'"\n")
#end

#start
print('09:'"\nDanish Ahmed","15/02/2024\n""I join the '"'"governer initaitive AI'"'program and i can do my best.")
#end

#start
print("\n10:")
names = ["Munner", "Khan", "Ali", "Shari", "Faizan"]
for name in names:
    print(name)
#end
    
#start    
print("\n11:")
names = ["Munner", "Khan", "Ali", "Shari", "Faizan"]
for name in names:
    print(f"Hello, {name}!have a nice day friend!") 
#end
    
 #start   
print("\n12:")
transpotationmode =["bike","car","bus","airoplane"]
for mode in transpotationmode:
     print(f"I love travel in {mode}!")  
#end
     
#start     
print("\n13:")
guest_list=[
    "hassan",
    "ali",
    "kashif"
]
 
invitation_message = {
     "hassan": "Dear.hassan,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "ali": "Dear.ali,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "kashif": "Dear.kashif,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]"
}

def send_invitation():
    for guest in guest_list:
        if guest in invitation_message:
            print("send invitation to",guest)
            print(invitation_message[guest])
            print("\n")

send_invitation() 
#end

#start
print("\n14:")
guest_list=[
    "hassan",
    "ali",
    "kashif"
]
 
invitation_message = {
     "hassan": "Dear.hassan,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "ali": "Dear.ali,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "kashif": "Dear.kashif,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]"
}

def send_invitation():
    for guest in guest_list:
        if guest in invitation_message:
            print("send invitation to",guest)
            print(invitation_message[guest])
            print("\n")

send_invitation() 

guest_cant_make_it="ali"
print(f"{guest_cant_make_it} can't make it to dinner.\n")
new_guest="amjad"
guest_list[guest_list.index(guest_cant_make_it)]=new_guest
invitation_message[new_guest] = f"Dear.amjad,\n\nI am really,i have a arrange a small party and i forgot you and i suddenlly you come in my brain i request you to come this and join us.\n\n[DANI]"
print("\nSending invitation with updated guest:")
send_invitation()
#end

#start
print("\n15:")
guest_list=[
    "hassan",
    "ali",
    "kashif"
]
 
invitation_message = {
     "hassan": "Dear.hassan,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "ali": "Dear.ali,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]",
     "kashif": "Dear.kashif,\n\nI hope your are fine and small function arrange to my home,and i want you and your family join this event.\n\nRegards,\n[dani]"
}

def send_invitation():
    for guest in guest_list:
        if guest in invitation_message:
            print("send invitation to",guest)
            print(invitation_message[guest])
            print("\n")

send_invitation() 

guest_cant_make_it="ali"
print(f"{guest_cant_make_it} can't make it to dinner.\n")
new_guest="amjad"
guest_list[guest_list.index(guest_cant_make_it)]=new_guest
invitation_message[new_guest] = f"Dear.amjad,\n\nI am really,i have a arrange a small party and i forgot you and i suddenlly you come in my brain i request you to come this and join us.\n\n[DANI]"
print("\nSending invitation with updated guest:")
send_invitation()
print("Hi friend!we have some new invitation.\n")
guest_list.insert(0,"hamza")
guest_list.insert(len(guest_list)//2, "sheri")
guest_list.append("Haider")

invitation_message["hamza"]=f"Dear.hamza,\n\nI am really sorry,i have a arrange a small party and i forgot you and i suddenlly you come in my brain i request you to come this and join us.\n\n[DANI]"
invitation_message["sheri"]=f"Dear.sheri,\n\nI am really sorry,i have a arrange a small party and i forgot you and i suddenlly you come in my brain i request you to come this and join us.\n\n[DANI]"
invitation_message["haider"]=f"Dear.haider,\n\nI am really sorry,i have a arrange a small party and i forgot you and i suddenlly you come in my brain i request you to come this and join us.\n\n[DANI]"

print("\nSending invitation with update guest list:")
send_invitation()
#end

#start  
print("\n16:")
guest_list = [
    "ubaid",
    "owais",
    "abid",
    "anas",
    "sheri",
    "hamza"
]


invitation_messages = {
    "ubaid": "Dear .ubaid,\n\nI am writing to cordially invite you to a dinner gathering. Your groundbreaking research in the field of radioactivity has paved the way for countless scientific advancements. Your dedication to science and your trailblazing spirit continue to inspire generations around the world. It would be an immense pleasure to have you join us for an evening of stimulating conversation and camaraderie. Your presence would truly make the occasion memorable. I hope you can grace us with your company.\n\\n[dani]",
    "owais": "Dear.owais,\n\nIt is with great honor that I extend to you an invitation to join me for dinner. Your contributions to the field of physics have profoundly shaped our understanding of the universe. I would be delighted to engage in stimulating conversation with you over a meal. Your wisdom and intellect continue to inspire generations, and it would be an incredible privilege to have you as my guest. Please let me know if you are able to attend.\n\n[dani]",
    "abid": "Dear.abid ,\n\nI am writing to cordially invite you to a dinner gathering. Your words have touched the hearts of millions and your resilience in the face of adversity is truly admirable. Your insights into the human condition have been a guiding light for many. It would be an immense pleasure to have the opportunity to converse with you and learn from your experiences. Your presence would undoubtedly enrich the evening. I hope you can join us.\n\n[dani]",
    "anas": "Dear.anas ,\n\nIt is with the utmost reverence that I extend this invitation to you. Your genius spans across art, science, and engineering, making you one of the most remarkable individuals in history. Your inventions and artistic masterpieces continue to captivate the world centuries later. I would be deeply honored to host you for dinner and discuss the boundless depths of your intellect. Your presence would make the evening an unforgettable experience. I eagerly await your response.\n\n[dani]",
    "sheri": "Dear.sheri ,\n\nI am writing to invite you to a dinner gathering. Your contributions to the fields of mathematics and physics have revolutionized our understanding of the universe. Your laws of motion and universal gravitation laid the groundwork for modern science. It would be an honor to have you join us for an evening of intellectual discourse and conviviality. I hope you can attend.\n\n[dani]",
    "hamza": "Dear.hamza ,\n\nI am writing to extend to you a cordial invitation to join me for dinner. Your pioneering work in electricity and magnetism has left an indelible mark on the world. Your inventive spirit and visionary ideas continue to inspire countless innovators. It would be a privilege to have you as my guest and to engage in enlightening conversation. I hope you will be able to join us for what promises to be a memorable evening.\n\n[dani]"
}


def send_invitations():
    for guest in guest_list:
        if guest in invitation_messages:
            print("Sending invitation to", guest)
            print(invitation_messages[guest])
            print("\n")

print("Unfortunately,  we can only invite two people for dinner.\n")

while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry {removed_guest}, I'm unable to invite you to dinner.")

print("\nInvitations to the remaining guests:")
send_invitations()

guest_list.clear()
print("Remaining guest list:", guest_list)
#end

#start
print("\n17:")
#list-of-places:
places=["Naran Ghaghan","Marie","Islamabad","Swat","Peshawer"] 

print("orignal order:",places)

print("Alphabetical order",sorted(places))

print("Orignal order after sorting",places)

print("Reversed alphabetical order",sorted(places, reverse=True))

print("Orignal order after reversw sorting",places)

places.reverse()
print("Reverse order:",places)

places.reverse()
print("Reversed again, back to original order:", places)

places.sort()
print("Sorted alphabetically:", places)

places.sort(reverse=True)
print("Sorted in reverse alphabetical order:", places)
#end

#start
print("\n18:")
#guest list
guest_list = ["Hassan", "ALi", "Sheri"]

for guest in guest_list:
    print(f"Dear {guest},\nI would like to invite you to dinner at my place. It would be an honor to have your presence.\nPlease let me know if you can make it!\n")

dinner_guests=["Ali","Hassan","Sheri"]

print("I am inviting", len(dinner_guests),"people for dinner.")
#end

#start
print("\n19:")

fruits = ["Apple","Mango","Anar","Banana","orange"]

print("list of fruit", fruits)
#end

#start
print("\n20:")
#Items
class Fruit:
    def __init__(self, name, color, ):
        self.name = name
        self.color = color

apple = Fruit("Apple", "brown", )
banana = Fruit("Banana", "Yellow", )
lemon = Fruit("Lemon", "Blue", )
grape = Fruit("Grape", "Purple", )

print(vars(apple))
print(vars(banana))
print(vars(lemon))
print(vars(grape))
#end

#start
print("\n21:")
#index
numbers = [11, 22, 33, 44, 55]

try:
    print(numbers[66])
except IndexError as e:
    print("Index Error:", e)

print("\n22:")
x=23
y=30
print("x is equal to y?i think true")
print(x==y)

print("x is less than y?i think true")
print(x<y)

print("x is greater than y?i think true")
print(x>y)

print("x is not equal to y?i think true")
print(x!=y)
#end

#start
print("\n23:")
#testing
string1 = "hello"
string2 = "world"
print("Test for equality with strings: I think False.")
print(string1 == string2)

word1 = "HELLO"
word2 = "hello"
print("Test using the lower case function: I think True.")
print(word1.lower() == word2.lower())

num1 = 10
num2 = 5
print("Numerical test for equality: I think False.")
print(num1 == num2)

print("Numerical test for inequality: I think True.")
print(num1 != num2)

print("Numerical test for greater than: I think True.")
print(num1 > num2)

print("Numerical test for less than: I think False.")
print(num1 < num2)

print("Numerical test for greater than or equal to: I think True.")
print(num1 >= num2)

print("Numerical test for less than or equal to: I think False.")
print(num1 <= num2)

bool1 = True
bool2 = False
print("Test using 'and' operator: I think False.")
print(bool1 and bool2)

print("Test using 'or' operator: I think True.")
print(bool1 or bool2)

numbers = [1, 2, 3, 4, 5]
print("Test whether an item is in an array: I think True.")
print(3 in numbers)

print("Test whether an item is not in an array: I think False.")
print(6 not in numbers)
#end

#start
print("\n24:")
# Alien color variable
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points.")

alien_color = 'red'

if alien_color == 'green':
    print("The player just earned 5 points.")    
#end
    
 #start   
print("\n25:")
alien_color = 'green'

# Checking the alien's color
if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")    

alien_color = 'red'
 

if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")    
#end
        
#start
print("\n26:")
alien_color = 'green'

if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")

alien_color = 'red'

if alien_color == 'green':
    print("The player earned 5 points.")
elif alien_color == 'yellow':
    print("The player earned 10 points.")
else:
    print("The player earned 15 points.")            
#end

#start
print("\n27:")    

age = 35

# Determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
#end

#start
print("\n28:")   
# favorite fruits
favorite_fruits = ["apple", "banana", "orange"]

# Check for certain fruits 
if "apple" in favorite_fruits:
      print("I love apple")

if "banana" in favorite_fruits:
 print("Bananas are deliciou")

if "orange" in favorite_fruits:
     print("Oranges are refresh")
#end

#start
print("\n29:")     
usernames = ["admin", "khan", "shan", "hamd", "anas"]

# print greetings
for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
#end
        
#strat
print("\n30:")
users = ["kkhan","sheri","hamd"]  

if users:
    for user in users:
        print("Hello, " + user + "!")


print("\n31:") 
# current usernames list
current_users = ['khan', 'shan', 'abid', 'ubaid']

# new usernames list
new_users = ['khan', 'SHAN', 'huzaifa', 'hamza', 'ali']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    
    new_user_lower = new_user.lower()
    
    if new_user_lower in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose another one.")
    else:
        print(f"The username '{new_user}' is available.")   
#end

#start
print("\n32:")  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    if num== 4:
        print(f"{num}th")
    if num == 5: 
        print((f"{num}th"))
    if num== 6:
        print((f"{num}th")) 
    elif num== 7:
        print((f"{num}th"))
#end

#start
print("\n33:")        

favorite_pizzas = ["chikhen", "kabab", "BBQ "]

for pizza in favorite_pizzas:
    print("I like", pizza, "pizza.")

print("I really love pizza!")
#end

#start
print("\n34:")
#list of animals
animals=["dog","cat","horse"]
print("Names of animal")
for animal in animals:
    print("animals")


for animal in animals:
  print(f"A {animal} would a great pet:")
  print("\nwhat these animals comman")
#end

#start
print("\n35:")
def make_shirt(size,message):
    """The function should print a sentence summarizing the size of the shirt and the message printed on it.""" 
    print(f"A {size} shirt with print this message:'{message}'")


make_shirt("large","Leo, Ronaldo!")  
#end

#start
print("\n36:")

def make_shirt(size="large", message="I love footall"):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"A {size} shirt with printed this message: '{message}'")

make_shirt()  
make_shirt("medium")  

make_shirt("small", "football is good game!")
#end

#start
print("\n37:")
#city description
def describe_city(city, country="tokyo"):
    """Prints a sentence describing the city and its country."""
    print(f"{city} is in {country}.")

describe_city("london")  
describe_city("Karachi", "Pakistan")  
describe_city("Delhi", "India")
#end

#start
print("\n38:")
def city_country(city, country):
    """Returns a string as 'city, country'."""
    return f"{city}, {country}"

print(city_country("Lahore", "Pakistan"))
print(city_country("Paris", "France"))
print(city_country("bombai", "india"))
#end

#start
print("\n39:")
def make_album(artist, title, tracks=None):
    """Builds a dictionary  a music album."""
    album = {
        'artist': artist,
        'title': title
    }
    if tracks:
        album['tracks'] = tracks
    return album

album1 = make_album("Taylor Swift", 13)
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album("Adele", "21", 11)

print(album1)
print(album2)
print(album3)
#end

#start
print("\n40:")
def show_magicians(magicians):
    """Prints the name of each magician in the array."""
    print("Magicians:")
    for magician in magicians:
        print(magician)

magician_names = ["Ali Cook","Umer Sharif","Zafar Ali","Aijaz Aslam","Asad Bashir Khan"]

show_magicians(magician_names)
#end

#start
print("\n41:")
def show_magicians(magicians):
    """Prints the name of each magician in the array."""
    print("Magicians:")
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the array of magicians by adding 'the Great' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] += " the Great"

magician_names = ["Ali Cook","Umer Sharif","Zafar Ali","Aijaz Aslam","Asad Bashir Khan"]

make_great(magician_names)

show_magicians(magician_names)
#end

#start
print("\n42:")
def show_magicians(magicians):
    """Prints the name of each magician in the array."""
    print("Magicians:")
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the array of magicians by adding 'the Great' to each magician's name."""
    great_magicians = ["Ali Cook","Umer Sharif","Zafar Ali","Aijaz Aslam","Asad Bashir Khan"]
    for magician in magicians:
        great_magicians.append(magician + " the Great")
    return great_magicians

magician_names = []

great_magicians = make_great(magician_names[:])  

show_magicians(magician_names)

show_magicians(great_magicians)
#end