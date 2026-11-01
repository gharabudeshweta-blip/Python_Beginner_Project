import random 
subjects =[
    "Sharukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A mumbai Cat",
    "A group of monkeys",
    "Auto Rickshow Driver from Delhi" 
]

actions =[
   "lunches",
   "cancels",
   "dances with",
   "eats",
   "Declares war on",
   "orders",
   "celebrates"
]

place_or_things =[
    "at Red Fort",
    "in mumbai local Train",
    " a plate of samosa ",
    "inside parliment",
    "at Ganga Ghat",
    "during IPL match",
    "India Gate"
]

while True:
    subject=random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(place_or_things)

    headline=f"BREAKING NEWS: {subject} {action} {place_or_thing}"

    print("\n"+ headline)

    user_input =input("\n Do you want another headline? (yes/no)".strip())
    if user_input =="no":
        break
print('\n Thanks for using the fake news Headline Generator.Have a fun day!')
