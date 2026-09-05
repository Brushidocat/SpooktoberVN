# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Remember: Sound cues 
## Chest opening: Furniture3_overwrite 
## General sfx, Organs, 
## Inserting token, Glass 1 or 2 

## window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.0)

define player = Character("You")
define player_m = Character ("You", window_background="mall_gui/textbox.png")
define megan = Character("Megan", window_background="mall_gui/textbox.png")
define brian = Character("Brian", window_background="mall_gui/textbox.png")
define megan_b = Character("The Bride", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.0), color = "#ffff")
define brian_s = Character("The Pumpkin",  window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.0), color = "#e9820dff")
define neil = Character("Neil", window_background="mall_gui/textbox.png")
define neil_v = Character("Count Blud", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.0), color = "#b91313ff")
define mystery = Character("???")
default spooky = False  
default mall = ""
define red = '#f31b1b'
define green = '#38ff7b'

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene shops_closed

    "For most inside the Salem Mall, the day was almost done. But for you, the night had just begun."

    "Up the stairs, turn right, turn right, keep going past the three beauty salons and one comic shop, and there you were. A rather nondescript storefront, painted black. It looked like it had been thrown up by the ghost of Spirit Halloween."

    "The sign was large, in neon and had taken almost half of your budget. {b}{color=[green]} LOCK&KEY ESCAPE ROOMS.{/color}{/b}"

    "Below was a smaller poster, designed with more enthusiasm than experience-{i}{b}COMING SOON: {color=[red]} COUNT BLUD'S MYSTERY MANSION!{/color}{/b}{/i}"

    "Below it, in smaller text: {size=-10}Opening {u}31st October, 8pm.{/u}"

    "It was now October 31th, 2026. 7pm."

    "In one hour, the doors of the mall would open again for the Mall's Annual Halloween Night."
    
    "In one hour, the newest addition to L&K would be opened."

    "And in one hour, because of a scheduling error and what would only ever be described as the Ceiling Incident-"

    "-YOU would have to finish the final runthrough."
    
    "If you didn't?"
    
    "You would have to either delay the opening of the Halloween Themed Escape Room to the day AFTER the biggest Halloween event of the year, or open it and face the possibility of an angry mob should something go horribly wrong."

    "A full year of begging for funds, planning, designing, hiring, and dealing with a particularly disoriented safety inspector, down the drain."
    
    "Your lease would be gone, and your store would probably join the row of pastels."

    "Deep breath."

    "You got this."

    scene regal_hallway_light

    "The walls were made of the finest styrofoam you could salvage from the local depo. Pillars made of balsam wood. Every detail was thinned at the top to give the illusion of high vaulted ceilings."

    "You were quite proud of how everything came out."

    "Quickly, you check your notes."

    "1: Check the Lights."

    "You press a hidden switch on the walls."
   
    scene regal hallway

    "Perfect."

    "Huh? What was that odd glow in the corner?" 

    show megan default 

    "Her pale face looked even more ghastly backlit by her phone screen. Her eyes and cheeks, smudged using dollar store makeup, looked even more sunken and hollow. To complete the effect was her wild hair and tattered white dress."
    
    "Unfortunatley, the bored, half-lidded expression she had on ruined the effect quite badly."

    player_m "Megan?"

    "She doesn't respond immediately. Eventually, her eyes slide towards you, glacially slow. She sighs, turns off her phone, and stuffs it under her dress."

    megan "Hey, boss." 

    "..."

    "..."

    "Looks like it was up to you to address the elephant in the room."

    menu: 
        "Where is everyone?":
            "She grimaces slightly."
            megan "Inside,"
            "She jabs a finger towards the closed door behind her."
            megan "Neil's making weird noises. Brian's cleaning up."
    
    menu: 
        "What are you doing here?":
            megan "Lunch break." 
            "You glance at the clock, which clearly says 7:05."
            megan "Dinner break."
            player_m "Early dinner break."
            megan "Late night."
            "She stares at you pointedly. Fair enough."

    megan "Oh. Right."
    "Megan hands out a neatly folded envelope to you. It was sealed with fake wax, and had been dyed with tea around the edges to look a little old."

    megan "Printer finally started working."

    menu: 
        "Thanks Megan, I'll wire you the money later.":
            "Megan gives you a short nod."

    "Suddenly, there was a staticky crack, then a tinny, hushed voice filters through the speakers. A familiar voice."

    mystery "-I can't find the extension cord-No I need to put it in the middle of the room-it has the best acoustics-"

    "The static cuts off again."

    "You look at Megan, who stares at the ceiling, vaguely irritated."

    play music haunted_hijinks

    "Next thing was music. Music you were very familiar with at this point."

    neil_v "{bt=h5-s0.5-p8.0} WELCOME {/bt} UNFORTUNATE SOUL!"

    megan "Goddamnit Neil."

    ##{sc=[range]}Text{/sc}
    
    "WELCOME TO MY {bt=h5-s0.5-p10.0} HAUNTED MANSION!{/bt}"

    neil_v "IN HERE, YOU SHALL BECOME MY NEXT {sc} {color=red} SAAAAAACRIFICE! {/color}{/sc}"

    "It was the same voice. Only now they'd put on what was admitedly a pretty good Hungarian accent. It was ruined a little bit by the mic peaking on every third syllable." 

    "Megan fishes out her walkie-talkie from the hidden pocket sewn into the dress."

    neil_v "NOW THAT YOU ARE TRAPPED, YOU SHALL NEVER ESCAAAAAAAPE-" 

    megan "Neil, quit it. You're early."

    stop music 

    "The voice stops mid-sentence."

    play music shenanigans

    neil_v "....NO I'M NOOOOOT! I AM COUNT BLUUUD!- "

    megan "Boss isn't in the room."

    "Silence."

    neil_v "THEY ENTERED THE SHOP TEN {bt=h5-s0.5-p10.0}MINUUUUUTES{/bt} AGO! WHAT GIIIVES?" 

    megan "Didn't you check the camera?"

    "Something bumps the microphone with a dull thud. In your mind's eye, you can see the scrawny young adult glancing at the monitors."

    "Thunk!"

    "Must have tripped on his cape." 

    neil_v "THEY ARE LAGGY AS {bt=h5-s0.5-p10.0}SHIIIIIT!{/bt}"

    "Your eyes narrowed. They weren't laggy, you changed them last week." 

    "The walkie-talkie in Megan's hands crackled, and another, more apologetic voice trickled in."

    brian "I think I tripped over them while I was walking in."

    brian "Sorry!"
    
    $ spooky = True 
    "Time to get spooky."



    return
