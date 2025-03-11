import time

class GameState: # for managing gameplay status & used in game save file
    def __init__(self):
        self.playerHealth = "" # not used yet, but its for managing abigail's health 
        self.playerInventory = "" # idk if i will do this one :/
        self.playerScene = "" # not used yet, but its for game save
        self.deathReason = "" # to show the death reason on the game over screen

gameState = GameState()
        
def gameOver(): # Game Over   
    print(f"\nGame Over:")
    time.sleep(1.5)
    print(f"Death due to {gameState.deathReason}")
    time.sleep(3)
    s1 = input('Restart? [yes/no]: ')
    if s1.lower() == 'yes':
        scene1()
    elif s1.lower() == 'no':
        time.sleep(1)
        print('\nName: Abigail')
        time.sleep(1)
        print('Age: 19')
        time.sleep(1)
        print("Status: 00 (Death by Unknown Cause)")
        time.sleep(3)
        exit()
    else:
        print(f"Not {s1}, It's Yes or No")
        start()
    
def scene3():
        print("\nYou carefully step down the stairway and reach the bottom, where a hallway stretches ahead. Walking to the end,\n you find three more hallways—only one of them is the right path.")
        s3q1 = input("[Left, Up, Right]: ")
        if s3q1 == 'Left':
            
        elif s3q1 == 'Up':
            
        elif s3q1 == 'Right':
            
        else:
            print('Invalid choice, try again.')
            scene3()

def scene2(): # Inside
    print('The Entrance is open!')
    time.sleep(1)
    print()
    time.sleep(3)
    print('You pick your flashlight and look around, and you find three stairways, which one do you choose?')
    
    s2q1 = input('[ 1 ] [ 2 ] [ 3 ]: ')
    
    if s2q1 == '1':
        scene3()
        time.sleep(3)
    elif s2q1 == '2' or s2q1 == '3':
        gameState.deathReason = "Paranoia?"
        gameOver()
    else:
        print('Invalid choice, try again.')
        scene2()
        
        
        

def scene1(): # Outside
    s1q1 = input('[Hammer, Pickaxe, Machette]: ')
    if s1q1.lower() == 'hammer':
        time.sleep(1)
        print()
        time.sleep(1)
        print('That worked well!')
        time.sleep(1)
        scene2()
        
    elif s1q1.lower() == 'pickaxe' or s1q1.lower() == 'machette':
        print("That doesn´t seem to work very well.")
        scene1()
    else:
        print('Invalid choice, try again.')
        scene1()
        
        
def start():
    s0 = input('Start? [yes/no]: ')
    if s0.lower() == 'yes':
        time.sleep(1)
        print()
        time.sleep(1)
        print("Dad: I´m Glad You Accepted this mission, Abigail!")
        time.sleep(2.5)
        print('Dad: You will go to The Second Pyramid first then the rest of the city')
        time.sleep(2.5)
        print("Dad: Old Cairo Has Ancient Secrets, Nobody tried to go in these old buildings and temples")
        time.sleep(2.5)
        print("Dad: and you're the one and to explore it")
        time.sleep(2.5)
        print("Abigail: It's a pleasure to go there, Dad <3")
        time.sleep(4.5)
        print("\n---| Old Cairo: Second Pyramid |---\n")
        time.sleep(5)
        print("The Main Entrance seems to be Blocked, You have a few tools you can use to Break it:")
        scene1()
    elif s0.lower() == 'no':
        print("Dad: The Eygptian Secret's will never be uncovered!")
        time.sleep(1)
        print("Abigail: Yeah, Whatever!")
        time.sleep(1)
        print("Dad: *sigh*")
        time.sleep(1)
    else:
        print(f"Not {s0}, It's Yes or No")
        start()

start()