import random
#These are all the challenges that app will randomly choose from. Some of this list I made up and some are from Chatgpt. With the prompt of make me about 50 summer challenges that kids can do
def summer_challenges():
    challenges=["Go On A Giant Water Slide", 
                "Build a Sand Castle",
                "Go on a swim in a big lake with friends",
                "Do a big family BQ",
                "Do an act of kindness for a child to make their summer better",
                "Make a lemonade stand with your friends",
                "Do some volunteer work",
                "Cook a new dish",
                "Create a new music list for summer time",
                "Water Balloon Fight",
                "Go on a Family Trip",
                "Try playing a new sport",
                "Have a sleepover with a friend or family",
                "Make heart warming cards to friends and family",
                "Make a photo album which includes family/friends from this summer",
                "Do arts and crafts",
                "Try a painting class",
                "Try having a small summer job",
                "Take a photo of yourself everyday in summer. And track your growth throughout summer",
                "Learn a new talent",
                "Go to the Gym",
                "Do an escape room",
                "Go on a camping trip",
                "Do a mini golf course",
                "The Floor is Lava Obstacle Course",
                "Mystery Food Challenge (Guess the Flavors)",
                "Lego Tower Showdown",
                "Extreme Hide-and-Seek",
                "Super Soap Race",
                "Water Balloon Dodgeball",
                "Outdoor Blanket Fort Movie Night",
                ]
    #This will choose a random option from the 
    return random.choice(challenges)

def main():
    print("Welcome To Random Summer Challenges Generator 2025!!!!")
    while True:
        input("Please press Enter in order to get your Challenges for this SUMMER!!!")
        challenge = summer_challenges()
        print("Your Challenge For This Summer Isssssss: " + challenge)
        redo = input("Would you like to get a new challenge for this Summer: ")
        if redo != "yes":
            print("Have a Great Summer!!! Come Back Again!")
            break

main()