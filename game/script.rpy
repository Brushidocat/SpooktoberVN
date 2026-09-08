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
define megan_b = Character("The Bride", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#ffff")
define brian_s = Character("The Pumpkin",  window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#e9820dff")
define neil = Character("Neil", window_background="mall_gui/textbox.png")
define neil_v = Character("Count Blud", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#b91313ff")
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

    "Up the stairs, turn right, turn right, keep going past the three beauty salons and one comic shop, and there you were."
    
    "Your pride and joy. A rather nondescript storefront, painted black. It currently looked like it had been thrown up by the ghost of Spirit Halloween, thanks to the mall decorators."

    "Above was a large sign, in neon and had taken almost half of your budget. {b}{color=[green]} LOCK&KEY ESCAPE ROOMS.{/color}{/b}"

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

    megan "Do I have to say the thing?"

    menu: 
        "Don't make her say the thing.":
            player_m "It's alright. I'll be doing it anyway."
            "Megan gives you a nod."
        "It is the final runthrough.":
            megan "Not really part of my job description."
            player_m "It's in case something happens, I'll give you a raise."
            "Megan takes a big sigh."
            megan "{i}Ah, you've made it.{/i}"
            megan "{i}We have a new delivery for you. It has to be handed in-person-"
            megan "Do we have to do this every time? These people are literally paying us to do this." 
            player_m "It's to get them into the role. Helps them buy into the illusion."
            "{i} This is true! It's called The Magic Circle! It's also used in DnD and in most video games."
            megan "Whatever you say."
            megan "{i}We've had some complaints about the house though. Be careful.{/i}"

    "Suddenly, there was a staticky crack, then a tinny, hushed voice filters through the speakers. A familiar voice."

    mystery "-I can't find the extension cord-No I need to put it in the middle of the room-it has the best acoustics-"

    "The static cuts off again."

    "You look at Megan, who stares at the ceiling, vaguely irritated."

    play music haunted_hijinks

    "Next thing was music. Music you were very familiar with at this point."

    neil_v "{bt=h5-s0.5-p8.0} WELCOME {/bt} UNFORTUNATE SOUL!"

    megan "Goddamnit Neil."

    ##{sc=[range]}Text{/sc}
    
    neil_v "WELCOME TO MY {bt=h5-s0.5-p10.0} HAUNTED MANSION!{/bt}"

    neil_v "IN HERE, YOU SHALL BECOME MY NEXT {sc} {color=red} SAAAAAACRIFICE! {/color}{/sc}"

    "It was the same voice. Only now they'd put on what was admitedly a pretty good Hungarian accent. It was ruined a little bit by the mic peaking on every third syllable." 

    "Megan fishes out her walkie-talkie from the hidden pocket sewn into the dress."

    neil_v "NOW THAT YOU ARE TRAPPED, YOU SHALL NEVER ESCAAAAAAAPE-" 

    megan "You're early."

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

    neil "Curse you Brian and your large feet!"

    "The sigh that goes through creates feedback."

    neil "Can we start, please?"

    "7:15."

    "You meet Megan's gaze, and she hands you another walkie-talkie."

    "Letter in hand, you turn towards the door."

    "Click!"
    
    $ spooky = True 

    player_m "Neil?"

    neil "Yes?"

    menu: 
        "It's time.":
            $ spooky = True 
            player "TIme to get spooky."



    jump mainhall 

label mainhall: 
    scene mainhall 
    play music monster musuem fadein 0.5
    "Soft, flickering light greeted you through the door. On cue, the music started from various hidden bluetooth speakers."

    megan "'scuse."

    "Megan trots past you to take her place by the wall."

    megan_b "{i}You should have never come here, strange traveler.{/i}"
    "Her voice is super flat."
    megan_b "{i}This is the lair of the Great Vampire Lord Count Blud{/i}"
    megan_b "{i}I was lured in once too, but I became his sacrifice, now I am trapped.{/i}"
    megan_b "{i}There is a way out of here. Unlike me, you are mortal. Find the sun lantern, confront Count Blud and we shall be freed.{/i}"
    megan_b "{i}Unfortu-"

    neil_v "WELCOME TO MY {bt=h5-s0.5-p10.0} HAUNTED MANSION!{/bt}"

    neil_v "IN HERE, YOU SHALL BECOME MY NEXT {sc} {color=red} SAAAAAACRIFICE! {/color}{/sc}"

    "Megan clicked her tongue, but kept quiet." 

    "Clearly, he'd practiced this, it was better to play along for now."

    neil_v "FOOLISH MORTALS! YOU SHALL NEVER ESCAPE MY LAIR~"

    neil_v "TONIGHT, ME AND MY BRETHEREN SHALL FEAST!"

    neil_v "YOU'll NEVER FIGURE OUT THE THREE PIECES OF MY {bt=h5-s0.5-p10.0} SECRET INCANTATION {/bt} TO OPEN THE DOOR!"

    "Click."

    megan "Right, what he said." 
    
    megan_b "{i}Maybe there's a hint in that letter.{/i}"

    show screen mainhall 

##Keys and important flags for Mainhall 

default chestKey = "UREM"
default chestisLocked = True 
default attemptedKey = ""
default gargoyleisLocked = True 
default gargoyleKey = 1, 2, 3,



label letter: 
    "Each word inside the letter was wriiten as clearly as possible."
    "{i} Dear Unfortunate So{color=red}U{/color}l,"
    "{i} If you are reading this, then I fea{color=red}R{/color} the worst has come to pass.{/i}"
    "{i} Fear not, if you are unsure where to start, the hint is close at hand.{/i}"
    "{i}Signed, a fri{color=red}E{/color}nd."
    "{i}PS, do not trust the bride, she {color=red}M{/color}erely wants more company."

label chest: 
    "There's a large chest. It's been rather roughly painted gold, but the material is genuine wood."
    if chestisLocked=True: 
        "There's a large lock keeping the chest shut."
        "Try the code?"
        menu: 
            "Yes.": 
                

label paintings: 
    "A row of paintings."

label gargoyle: 
    "A massive gargoyle."
    "You made it yourself using paper-mache and some stuff you salvaged."
    if gargoyleisLocked = True: 
        "There's something in it's jaws, you can't see it from here though."

default mhDoorisLocked = True

label mainhall_Doors: 
    "Impressively thick and detailed, the doors stand in front of you."
    if mainhall_Doors: 
        "Right now, they are closed."
        "Speak the incantation?"
    

default brideHints = 0

label Bride_Hints: 
    "Megan looks at you as you approach and stuff her phone back in her pocket." 
    if brideHints == 0: 
        megan_b "{i}Do you need a hint? The vampire lord changes the incantation every time."
        megan "Chest hint is in the letter. Had to use the colored ink." 
        megan "Glad that's not out of my paycheck."
        $ brideHints += 1
    else if brideHints == 1: 
        megan_b "{i}Everything you need is here, I believe. I would help, but alas, I cannot."
        megan "Hey, do I have to clean off fingerprints from those paintings every time?"
    else if brideHints == 2: 
        megan_b "{i} The great beast contains part of the code in its mouth. It seems to have a fondness for the paintings in this gallery.{/i}"
        megan "Have to admit, I like the gargoyle."
        megan "Once this is all over, you mind if I take it home? I can use it to scare the neighbors."
        megan "You sure people'll notice those hints on the paintings?" 
    else: 
        megan "That's all I got for you, boss."
        megan "Unless you want to talk about my salary."

label mainhall_End: 
    "The moment the three words leave your mouth, the door "

        



label hallway: 
    "Long and thin, the hallway stretches out in front of you. And there, standing on the side of the room trying to right a chair, was a long, lanky figure."
    "His pumpkin mask glows faintly like the fake torches in the banisters"
    brian "Hey boss! Er-Oh, sorry. One sec." 
    "He finally turns the chair upright, then straightens his back."
    brian_s "{i}Ah! Another guest for the master?"
    brain_s "{i}Poor soul, much like the pale megan-madam-{/i} shit-"
    brian_s "{i}Much like the pale madam next door, you have been trapped here. I assume she's tasked you with getting the Sun lantern?"
    brian_s "{i}Don't be fooled, she's merely trying to distract you."
    brian_s "{i}You should find the-the...."
    "Silence. Brian looks at you blankly for a moment. He grabs something from his pocket and reads it." 
    brian_s "{i}Moon dagger!{/i}"








label end: 
    return 
