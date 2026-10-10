# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Remember: Sound cues 
## Chest opening: Furniture3_overwrite 
## General sfx, Organs, 
## Inserting token, Glass 1 or 2 

## window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.0)

define you = Character("You")
define player_m = Character ("You", window_background="mall_gui/textbox.png")
define megan = Character("Megan", window_background="mall_gui/textbox.png", callback = name_callback, cb_name = "megan")
define brian = Character("Brian", window_background="mall_gui/textbox.png", callback = name_callback, cb_name = "brian")
define megan_b = Character("The Bride", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#ffff", callback = name_callback, cb_name = "megan")
define brian_s = Character("The Pumpkin",  window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#e9820dff", callback = name_callback, cb_name = "brian")
define neil = Character("Neil", window_background="mall_gui/textbox.png", callback = name_callback, cb_name = "neil")
define neil_v = Character("Count Blud", window_background = Image("gui/textbox.png", xalign = 0.5, yalign = 1.1), color = "#b91313ff", callback = name_callback, cb_name = "neil")
define mystery = Character("???", callback = name_callback, cb_name = "???")
default spooky = False  
default mall = ""
define red = '#f31b1b'
define green = '#38ff7b'
define creak = "SFX/Furniture3_Overwrite-Save-Question.wav"
define solve = "SFX/Glass1_Save-Game-Question.wav"
define tink = "SFX/Glass3_Click-Dialogue.wav"
define paper = "SFX/Cloth_Overwrite-Save-Question.wav"
define unlock = "SFX/Glass3_Confirm-Question.wav"
define gurgle = "SFX/freesound_community-viscious-liquid-gurgling-54710"
define demon = "demon.png"
define nova = "nova.png"
define vega = "vega.png"
define larissa = "larissa.png"
define kiddo = "kiddo.png"

image megan phone = At('megan phone.png', sprite_highlight('megan'))
image megan default = At('megan default.png', sprite_highlight('megan'))
image brian default = At('brian default.png', sprite_highlight('brian'))
image brian panic = At('brian panic.png', sprite_highlight('brian'))
image neil default = At('neil default.png', sprite_highlight('neil'))
image neil sad = At('neil sad.png', sprite_highlight('neil'))
label cheatcodes: 
    
    menu: 
        "Mainhall start":
            jump mainhall_start
        
        "Ballroom":
            jump ballroom_start
        "Hallway start":
            jump hallway_start
        "end":
            jump end
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
   
    #jump cheatcodes
    play music starreaction

    scene shops_closed

    "For most inside the Salem Mall, the day was almost done. But for you, the night had just begun."

    "Up the stairs, turn right, turn right, keep going past the three beauty salons and one comic shop, and there you were."
    
    "Your pride and joy. A rather nondescript storefront, painted black, with no windows and a few framed posters on the wall."

    "It currently looked like it had been thrown up by the ghost of Spirit Halloween, thanks to the mall decorators." 

    "Cheap bat banners 'borrowed' from the Spirit Halloween, cobwebs made of cheap nylon, and a couple of limp green streamers. Someone had even stuck stickers onto the wall."

    "Above was a large sign, in neon and had taken almost half of your budget. {b}{color=[green]} LOCK&KEY ESCAPE ROOMS.{/color}{/b}"

    "Below was a smaller poster, designed with more enthusiasm than experience-{i}{b}COMING SOON: {color=[red]} COUNT BLUD'S MYSTERY MANSION!{/color}{/b}{/i}"

    "Below it, in smaller text: {size=-5}Opening {u}31st October, 8pm.{/u}"

    "It was now October 31th, 2026. 7pm."

    "In one hour, the doors of the mall would open again for the Mall's Annual Halloween Night."
    
    "In one hour, the newest addition to L&K would be opened."

    "And in one hour, because of a scheduling error, traffic delays, and what would only ever be described as the Ceiling Incident-"

    "-YOU, the owner of the room would have to finish the final runthrough tonight."
    
    "If you didn't?"
    
    "You would have to either A: delay the opening of the Halloween Themed Escape Room to the day AFTER the biggest Halloween event of the year." 
    
    "Or B: open it and face the possibility of an angry mob should something go horribly wrong."

    "A full year of begging for funds, planning, designing, hiring, and dealing with a particularly hungry safety inspector, would all go down the drain."
    
    "Your lease would be gone, and your store would probably join the row of pastels."

    "Deep breath."

    "You got this."

    scene regal_hallway_light with fade
    play music communisumbra

    "The walls were made of the finest styrofoam you could salvage from the local depo. Pillars made of balsam wood. Every detail was thinned at the top to give the illusion of high vaulted ceilings."

    "You were quite proud of how everything came out."

    "Quickly, you check your notes."

    "1: Check the Lights."

    "You press a hidden switch on the walls."
   
    scene regal hallway

    "Perfect."

    "Huh? What was that odd glow in the corner?" 

    show megan phone

    "Her pale face looked even more ghastly backlit by her phone screen. Her eyes and cheeks, smudged using dollar store makeup, looked even more sunken and hollow. To complete the effect was her wild hair and tattered white dress."
    
    "Unfortunately, the bored, half-lidded expression she had on ruined the effect quite badly."

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
    show megan default: 
        pickup
        2
    "Megan hands out a neatly folded envelope to you. It was sealed with fake wax, and had been dyed with tea around the edges to look a little old."

    show megan default 

    megan "Printer finally started working."

    menu: 
        "Thanks Megan, I'll wire you the money later.":
            "Megan gives you a short nod."

    megan "Do I have to say the thing?"

    menu: 
        "Don't make her say the thing.":
            player_m "It's alright. I'll be doing it anyway."
            "Megan gives you a nod."
        "It {i}is{/i} the final runthrough.":
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

    neil_v "IN HERE, YOU SHALL BECOME MY NEXT {sc} {color=[red]} SAAAAAACRIFICE! {/color}{/sc}"

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

    brian "I think I tripped over a cable while I was walking in."

    brian "Sorry!"

    neil "Curse you Brian and your large feet!"

    "The sigh that goes through creates feedback."

    neil "Can we start, please?"

    "7:15."

    "You meet Megan's gaze, and she hands you another walkie-talkie."

    "Letter in hand, you turn towards the door."

    "Click!"

    player_m "Neil?"

    neil "Yes?"

    menu: 
        "It's time.":
            $ spooky = True 
            you "Time to get spooky."



    jump mainhall_start

label mainhall_start: 
    scene mainhall no megan
    play music doll
    "Soft, flickering light greeted you through the door. On cue, the music started from various hidden bluetooth speakers."
    show megan default: 
        offscreenleft
        normal
        walkto(center, 5, 2, 1, 1)
    

    megan "'scuse."

    "Megan trots past you to take her place by the wall."
   

    megan_b "{i}You should have never come here, strange traveler.{/i}"
    "Her voice is super flat."
    megan_b "{i}This is the lair of the Great Vampire Lord Count Blud{/i}"
    megan_b "{i}I was lured in once too, but I became his sacrifice, now I am trapped.{/i}"
    megan_b "{i}There is a way out of here. Unlike me, you are mortal. Find the sun lantern, confront Count Blud and we shall be freed.{/i}"
    megan_b "{i}Unfortu-"

    neil_v "WELCOME TO MY {bt=h5-s0.5-p10.0} HAUNTED MANSION!{/bt}"

    neil_v "IN HERE, YOU SHALL BECOME MY NEXT {sc} {color=[red]} SAAAAAACRIFICE! {/color}{/sc}"
    neil_v "NOW THAT YOU ARE TRAPPED, YOU SHALL NEVER ESCAAAAAAAPE! MY POWERS ARE LEGENDARY!!" 

    "Megan clicked her tongue, but kept quiet." 

    "Clearly, he'd practiced this, it was better to play along for now."

    neil_v "YOU'll NEVER FIGURE OUT THE THREE PIECES OF MY {bt=h5-s0.5-p10.0} SECRET INCANTATION {/bt} TO OPEN THE DOOR!"

    neil_v "TONIGHT, ME AND MY BRETHEREN SHALL FEAST!"

    "Click."

    show megan phone 

    megan "What he said." 
    
    megan_b "{i}Maybe there's a hint in that letter.{/i}"

    jump mainhall 
    
label mainhall: 
    hide megan 
    call screen mainhall 

##Keys and important flags for Mainhall 

define chestKey = "UREM"
default chestisLocked = True 
default chestKey_try = ""
default gargoyleisLocked = True 
define gargoyleKey = ["red", "blue", "red", "purple"]
default gargoyleKey_try = []
default tabletCollected = 0 

label letter: 
    "Each word inside the letter was wriiten as clearly as possible."
    "{i} Dear Unfortunate So{color=[red]}U{/color}l,"
    "{i} If you are reading this, then I fea{color=[red]}R{/color} the worst has come to pass.{/i}"
    "{i} Fear not, if you are unsure where to start, the hint is close at hand.{/i}"
    "{i}Signed, a fri{color=[red]}E{/color}nd."
    "{i}PS, do not trust the bride, she {color=[red]}M{/color}erely wants more company."
    jump mainhall

label chest:
    scene chest 
    "There's a large chest. It's been rather roughly painted gold, but the material is genuine wood."
    if chestisLocked == True: 
        "There's a large lock keeping the chest shut. It's one of those word-based ones, with four turning dials."
        "Try the code?"
        menu: 
            "Yes.":
                jump chest_code
            "No":
                jump mainhall 
    else: 
        menu: 
            "Leave it alone.":
                jump mainhall 

label chest_code: 
    python: 
        chestKey_try = renpy.input("Enter the Code")
        chestKey_try = chestKey_try.strip()
        chestKey_try = chestKey_try.upper()
    if chestKey_try == chestKey: 
        "The lock becomes heavier under your fingers as the lock loosens. You put it to the side."
        menu: 
            "Open the chest.":
                play sound creak volume 1.5
                "Using two hands, you push the lid open."
                "Inside the chest lays a broken piece of tablet lays at the bottom."
                $ chestisLocked = False 
                $ tabletCollected += 1
                menu: 
                    "Take the tablet.":
                        "It is cool underneath your fingertips."
                        jump mainhall 
    else: 
        "Nothing. It looks like you got the wrong code."
        megan "Didn't you set the code yourself?"
        "You remain silent."
        menu: 
            "Leave?":
                "You leave the chest alone for now."
                jump hallway
            "Try again":
                jump chest_code
    
default hascheckedPainting = False 
                

label paintings:
    ##TODO: Make this an imagemap? 
    scene paintings
    "A row of paintings."
    menu: 
        "Look at the first painting.": 
            "It's a picture of a desolate landscape with a red moon, a dark blue mountain in the background, and a dark night sky with yellow stars."
            menu: 
                "Check behind the painting?":
                    "With careful hands, you flip the landscape over, but you see nothing."
            jump paintings 
        "Look at the second painting.": 
            "Here is a regal garden filled with red roses, white lilies, and purple wolfsbane."
            menu: 
                "Check the painting?":
                    scene painting_back 
                    "Oh! You found something! You've collected a tablet piece."
                    $ tabletCollected += 1
                    menu: 
                        "Take the tablet.":
                            jump paintings
                
            jump paintings
        "Look at the third painting.": 
            "A portrait of an extremely pale man. He wears a red brooch, a black cape, and has a white dagger in his hands."
            menu: 
                
                "Check behind the painting?":
                    "You turn it over, but find nothing."
            jump paintings 
        "Go back.":
            jump mainhall 
    return 

label gargoyle: 
    if gargoyleisLocked:
        scene gargoyle_tablet
    else:
        scene gargoyle_notablet
    "A gargoyle stands on a stone podium."
    "You made it yourself using paper-mache and some stuff you salvaged."
    "With a curved beak, large wings, and hooked claws, it was suitably an impressive piece. You based it on a certain cartoon you watched as a kid."
    if gargoyleisLocked == True: 
        "There's something in it's jaws, a section of a stone tablet."
    menu gargoylelook: 
        "Check the base.":
            scene gargoyle_close
            "Below the gargoyle, is a row of buttons with images on them."
            "From right to left, was an engraving of a moon, a rose, a gem and another flower."
            jump gargoylelook
        "Try a code." if gargoyleisLocked:
            jump gargoyle_code
        "Leave.": 
            jump mainhall 

define codenumber = 0 

label gargoyle_code: 
    menu: 
        "Press the red button.": 
            $ gargoyleKey_try.append("red")
            $ codenumber += 1 
            if codenumber ==4: 
                jump gargoylecheck
            else: 
                jump gargoyle_code

        "Press the blue button.":
            $ gargoyleKey_try.append("blue")
            $ codenumber += 1 
            if codenumber ==4: 
                jump gargoylecheck
            else: 
                jump gargoyle_code

        "Press the green button.":
            $ gargoyleKey_try.append("green")
            $ codenumber += 1 
            if codenumber ==4: 
                jump gargoylecheck
            else: 
                jump gargoyle_code
        "Press the purple button.":
            $ gargoyleKey_try.append("purple")
            $ codenumber += 1 
            if codenumber == 4: 
                jump gargoylecheck 
            else: 
                jump gargoyle_code
        "Leave.":
            jump mainhall 
    
label gargoylecheck: 
    if gargoyleKey == gargoyleKey_try:
        "The tablet loosens from the gargoyle's grip. You take it out easily."
        $ gargoyleisLocked = False 
        scene gargoyle_notablet
        $ tabletCollected += 1 
        $ mainhall = "images/mainhall/mainhall_gargoyle.png"
        jump mainhall 
    else: 
        "The gargoyle remains still."
        $ codenumber = 0 
        $ gargoyleKey_try = []

label carpet: 
    "There is a large carpet under the table with an alternating red-yellow-green-red pattern, and embroidered blue roses at the center."
    jump mainhall 

default mainhall_Doors = True
default mh_incantation = "RED RIVERS RUN DEEP TONIGHT"
define mh_incantation_try = ""

label mainhall_Doors: 
    scene mainhall doors
    "Impressively thick and detailed, the doors stand in front of you."
    if mainhall_Doors: 
        "Right now, they are closed."
        menu: 
            "Speak the incantation.":
                jump MainhallDoors_Code
            "Leave it be for now.":
                jump mainhall 

label MainhallDoors_Code: 
    python: 
        mh_incantation_try = renpy.input("Speak!")
        mh_incantation_try = mh_incantation_try.upper()
    if mh_incantation_try == mh_incantation:
        jump mainhall_End
    else: 
        "You try the door, but it doesn't budge. Maybe you did it wrong?"
        $ mh_incantation_try = ""
        menu: 
            "Try again.":
                jump MainhallDoors_Code
            "Leave.":
                jump mainhall

default tabletplaced = False 
        
label table: 
    #TODO: Drag and Drop?
    scene table_notablet
    "The large wooden table dominates the room. There are strange burns all over the front. Some of them end abruptly, forming a rectangle in their negative space."
    menu: 
        "Put the tablets down on the table." if tabletCollected == 3: 
            scene table_withtablet
            "You put all three tablets on the table, and arrange them."
            "Together, they spell out the words. 'Red Rivers Run Deep Tonight.'"
            $tabletCollected = 0   
            menu: 
                "Leave the table":
                    jump mainhall 
        "Read the letter.":
            jump letter
        "Go back.": 
            jump mainhall 


default brideHints = 0

label Megan: 
    if gargoyleisLocked:
        scene mainhall no megan 
    else: 
        scene mainhall no megan gargoyle
    show megan phone 
    "Megan looks at you as you approach and stuff her phone back in her pocket."
    show megan default 
    you "We need to run through your lines."
    "Megan raised an eyebrow. Then she shrugs." 
    megan_b "{i}Do you need a hint? The vampire lord changes the incantation every time."
    menu: 
        "Yes.": 
            "Megan rolls her eyes, but proceeds anyway."
            jump BrideHints
        "No.": 
            jump mainhall 



label BrideHints: 
    if brideHints == 0: 
        megan_b "{i}That letter you came in with, I recognise its seal. Perhaps it contains a clue?"
        megan "I see why we have a color printer in the back now." 
        megan "Glad that's not out of my paycheck."
        $ brideHints += 1
        menu: 
            "Much appreciated, Megan":
                "Megan gives a short nod, and starts looking at her phone again."
                jump mainhall
            
    elif brideHints == 1: 
        megan_b "{i}I've seen those paintings move and shake sometimes, as if they are alive. Perhaps you should take a closer look."
        megan "Hey, do I have to clean off fingerprints off those frames every time they check them?"
        $ brideHints += 1 
        menu: 
            "Only after the session":
                megan "Ew."
                jump mainhall
    elif brideHints == 2: 
        megan_b "{i} The great beast contains part of the code in its mouth. It seems to have a fondness for the paintings in this gallery.{/i}"
        megan "Have to admit, I like the gargoyle."
        megan "Once this is all over, you mind if I take it home? I can use it to scare the neighbors."
        $ brideHints += 1 
        menu: 
            "It's going to be on for a while.":
                megan "Something to look forward then. "
                jump mainhall
    else: 
        megan "That's all I got for you, boss."
        megan "Unless you want to talk about my salary."
        jump mainhall
    jump Megan  

default mainhallfinished = False 
label mainhall_End:
    scene mainhall finished
    $ mainhallfinished = True
    $ mainhall = "images/mainhall/mainhall finished.png"
    "The moment the three words leave your mouth, the door should have unlocked and swing open on its own, as if by a ghost."
    "Instead-"
    play music haunted_hijinks
    neil_v "HOW?! HOW COULD YOU HAVE FIGURED OUT MY SECRET PASSWORD!? {bt=h5-s0.5-p10.0}INCONCEIVABLE!!!"
    "He sounds a little different, as if he had something in his mouth."
    neil_v "COULD IT BE?! CURSE YOU, MY FORMER BRIDE!" 
    "Megan ignores him."
    neil_v "NO MATTER! EVEN WITH HELP, THERE'S NO WAY YOU SHALL DEFEAT MEE!" 
    neil_v "{bt=h5-s0.5-p10.0}MUAHAHAHAHAHAHAHA{/bt}-ack."
    play music shenanigans
    neil "*Cough*! *Cough*!"
    you "You alright there?"
    megan "Did you steal my peppermints?"
    neil "I-hrk! NO CANDY CAN-gack-STOP ME! I SHALL {bt=h5-s0.5-p10.0}RETUUUURN.{/bt}"
    megan "Open the door Neil."
    "Silence."
    "The double doors unlock with an audible click. Then the PA system turned off."
    megan "I'm going to make him pay later."
    "Probably literally."
    megan "See ya, Boss. Catch you after my mandated 15 minute break."
    jump hallway_start



default haveGem = False 
default bookcaseCode = "69463"
define bookcaseCode_try = ""
default endRoute = ""
    

label hallway_start:
    scene hallway 
    play music monster_musuem
    "The long, thin hallway stretches out far in front of you. The door on the other side was flanked by two small boxes." 
    "And there, standing on the side of the room trying to right a chair, was a long, lanky figure."
    "His pumpkin mask eyes glow with an eerie light, and his suit is slightly wrinkled."
    show brian default 
    show hallway no brian
    brian "Hey boss! Er-Oh, sorry. One sec." 
    show brian default:
        bowright
    "He finally turns the chair upright, then straightens his back."
    show brian default: 
        unpose
    brian_s "{i}Ah! Another guest for the master?"
    brian_s "{i}Poor soul, much like the pale megan-{b}madam{/b}-{/i} shit-"
    brian_s "{i}Much like the pale madam next door, you have been trapped here. I assume she's tasked you with getting the Sun Lantern?"
    "The pumpkin headed servant shook his head."
    brian_s "{i}Don't be fooled, she's merely distracting you. She is a lonely spectre." 
    brian_s "{i}You should find the moon dagger instead! It is his main source of power. Without it, he will have nothing.{/i}" 
    brian_s "{i}Who knows, perhaps you may even become the new count!{/i}"
    brian_s "{i}I'm quite tired of his Lord Count Blud myself,"
    brian_s "{i}The master is quite clever, however. He's encased both artefacts in magical containers, there is only one way to do so, the Blood Ruby." 
    "He gestures behind you, where a large glass gem resides inside a glass case." 
    "Underneath, in large industrial text, was the phrase: DO NOT BREAK!"
    brian_s "{i}I would open the case itself, but avast-alas, I have no way to open it myself!"
    stop music 
    play sound tink
    "Something falls out of his pocket. A thick, heavy looking key that looks like it would perfectly fit the lock on the glass case."
    show brian default: 
        bowright
    "He pauses, unblinking, looks down." 
    show brian default: 
        unpose
    "Then looks back up."    
    
    show brian default: 
        pickup(5, 0.2)
    
    "Then he lunges for the key with all the grace of an american linebacker and shoves it into his pocket."
    brian_s "{i}P-perhaps you can find it? Remember though, the Ruby can only be used once! Choose wisely who you side with.{/i}"
    "After a brief pause, he rights himself."
    brian "How was that? I finally managed to remember most of my lines!"
    brian "Neil helped me practice." 
    menu:
        "Good job.": 
            "Brian gives you a bright smile."
            brian "Thanks!"
        "You're supposed to stay in character.": 
            brian "Whoops! Sorry boss, I got excited."
        "Did you forget to put the key back?":
            brian "...yes."
            brian "I'll put it back in the bookshelf later."
    brian_s "I am your humble servant, if you are able to job my memory, perhaps I can help guide your way!"
    hide brian default 
    "Brian quickly starts pretending to dust the furniture."
    jump hallway 

label hallway: 
    call screen hallway

label brian: 
    scene hallway no brian
    show brian default 
    "Brian perks up when you approach him."
    brian "Something up, boss?"
    you "Do you remember the hints?"
    brian "Oh right! Yes I do! You want me to recite them?" 
    menu: 
        "Yes,":
            you "Remember, keep your head straight. Don't give them too much help."
            brian "Got it!"
            jump servant_hints
        "Not right now.":
            brian "Alright, I'll be right here."
            jump hallway 

default servantHints = 0 

label servant_hints: 
    if servantHints ==0: 
        "Brian's head twitches towards the drawer before he realises it."
        brian "Alright, alright. *ahem*"
        brian_s "{i}Are you stuck, dear guest? Fear not, while I do not know the exact location of the key, perhaps a look around the area will do you well?"
        $ servantHints += 1
        menu: 
            "Thanks Brian.":
                brian "Happy to help!"
                jump hallway
    elif servantHints == 2:
        brian_s "{i}Feel free to explore more of the mansion. Especially the MAIN HALL." 
        you "Please don't yell at the customers. This isn't that kind of escape room."
        brian "Okay!"
        $ servantHints +=1
        menu: 
            "Thanks anyways, Brian.":
                "Brian looks happy."
                jump hallway
    elif servantHints == 1: 
        brian_s "{i} The master has a fondness for mirrors. Windows to the soul, he says. And yet, I've never gotten a glimpse of his reflection."
        menu: 
            "Thanks Brian.":
                brian "I quite like this line for some reason, feels spooky."
                jump hallway
    else: 
        "Brian goes very silent."
        brian "Um...I think I ran out of lines."
        brian "I can-uh-get the cheat sheet!" 
        "He starts patting his pockets frantically."
        "Other than a few candy wrappers, nothing comes up."
        brian "Oh, I must have left it in the staff room. But I can run and grab it if you need it." 
        you "I don't think that's necessary."
        "Brian looks very relieved, though he does go and pick up the candy wrappers quickly."
        jump hallway
    jump brian  

default havePaper = False 

label firstdrawer: 
    scene drawer
    "You open the drawer. It opens smoothly. Until it gets halfway. Then it stops."
    scene drawer with vpunch 
    "You try again. Nothing. It feels like the drawer's hit something solid."
    "Immediately, Brian comes over."
    brian "Huh, that's weird."
    brian "Here, let me-"
    ##Shake 
    scene drawer with vpunch 
    ## rattle sound 
    "He grips the handle and tugs a little harder. It doesn't budge."
    scene drawer with hpunch 
    brian "Maybe some paint got in the-Hang on."
    scene drawer with vpunch 
    "The drawer rattles ominously as he yanks harder. And yet still, it doesn't move." 
    brian "COme onnnn-!"
    scene drawer with vpunch 
    show brian default: 
        offscreenleft 
        normal 
        walkto(offscreenright, 1, 0.2, 0, 0)
    play sound creak 
    "The drawer suddenly flies open, and Brian stumbles backwards. Eyes wide, limbs flailing, his back hits the opposite wall." 
    megan "Did Brian fall again?"
    brian "I'm fine! I'll-uh-go sweep a corner." 
    "You watch him move, but he genuinely seems okay. Maybe the pumpkin mask protected his head."
    "Inside the drawer, you only manage to find a piece of paper."

    menu: 
        "Check the paper." if not havePaper:
            "Dear His Most Illustrious Count Blud,"
            "As you have requested, I have taken care to hide the key to the Blood Ruby."
            "It is within the hallways of this castle. I have endeavored a clever plan to keep the code safe in another room."
            "No one shall be able to REVERSE the curse you've casted on this place."
            "Your most loyal servant, the Pumpkin."
            "PS. xis dna derdnuh xis dnasuoht eno"
            menu: 
                "Take the paper.":
                    $ havePaper == True 
                    jump hallway 
                "Leave it in the drawer.":
                    jump hallway 
    jump hallway 

define smallKey = False 

label seconddrawer: 
    "This is a small keyhole in the drawer. You pull on the handle, and it is sufficiently locked."
    menu: 
        "Use the small key" if smallKey: 
            "You use the small key. The drawer, thankfully, opens smoothly." 
            "Brian breathes a sigh of relief."
            jump seconddrawer_open
        "Leave it alone.": 
            jump hallway 
label seconddrawer_open:
    menu: 
        "Look at the clock.":
            "The clock is just a shell. There isn't anything inside. Instead, some of the numbers on the front have small colored paint underneath them."
            "A red dot under the 6, a blue dot under the 3, a yellow dot on the 9, and a green dot on the 4"
            menu clockcheck: 
                "Put down the clock.":
                    "You put the clock back into the shelf."
                    jump drawer 
                "Inspect the clock.":
                    "Underneath, you spot some clumsily carved words. MAIN HALL."
                    jump clockcheck

label mirror: 
    scene mirror
    "The mirror has been polished to an almost perfect shine and hung proudly."
    menu mirrorchoice: 
        "Place the paper to the mirror?" if havePaper:
            "You hold the paper to the mirror, and immediately you see words."
            "Decoded, it writes:"
            "one thousand six hundred and six"
            jump mirrorchoice
        "Leave.":
            jump hallway 

label drawer: 
    scene drawer
    "There is a small drawer shoved to the left wall with two shelves."
    menu: 
        "Try the top handle.":
            jump firstdrawer
        "Try the lower handle.":
            jump seconddrawer 
        "Leave.":
            jump hallway 

label bookcase: 
    scene bookcase
    "Approaching the bookcase reveals obvious signs of most of the books being glued together. That was mostly to reduce cleanup, and because one time Brian bumped his elbow on the bookshelf and toppled every single book onto the floor. On top of him."
    "He was fine, thankfully."
    "The floor on the other hand...It was good they were having a carpet sale at the depo."
    "As you get closer to the bookcase, Brian immediately perks up and, doing his best to be inconspicuous, shuffles closer to you. He keeps glancing at it in intervals."
    menu book: 
        "Look closer at the bookshelf.":
            "Walking to the side, you spot a small keypad with numbers."
            menu tryBookcase: 
                "Try a code?":
                    "Brian gets even closer as you start pressing buttons."
                    "You can almost hear him breathing."
                    you "Uh, Brian-sorry, I can't concentrate with you that close."
                    "Brian immediately walks backwards and almost trips over his own feet."
                    jump bookcase_code
                "Leave the bookcase.":
                    jump hallway 
        "Look closer at the book": 
            "Not all of the books are fake. Some can be taken."
            menu: 
                "Pull out a book.":
                    jump booklist  
                "Leave it be.": 
                    jump book 
    jump hallway 

default havesmallKey = False 
label bookfail: 
    "You open the book, but find nothing. You place it back into the shelf."
    jump booklist 
label booksuccess: 
    "Inside the book, you find one half of the thick tomb has been modified. A small recess, large enough for a tiny key."
    "It's not big enough to fit in the lock. (And you know better than to try.) but maybe it could unlock something else?"
    jump hallway

label booklist: 
    menu: 
        "Demonologie, 1597": 
            jump bookfail
        "Carmilla, 1872":
            jump bookfail 
        "Dracula, 1897":
            jump bookfail
        "Macbeth, 1606":
            jump booksuccess
        "Little Women, 1869,": 
            jump bookfail 
        "Leave it alone.":
            jump book

label bookcase_code: 
    python: 
        bookcaseCode_try = renpy.input("Input Code")
        bookcaseCode_try = bookcaseCode_try.strip()
        bookcaseCode_try = bookcaseCode_try.upper()
    if bookcaseCode_try == bookcaseCode:
        jump hiddenCompartment
    else: 
        "There is a faint negative *beep* as you get the code wrong."
        brian "D'oh! It's okay, you can try again!" 
        "...Urge to give cookie...Rising..."
        $ bookcaseCode_try = ""
        jump tryBookcase



default havebigkey = False
label hiddenCompartment: 
    scene bookcase open
    "The hidden compartment swings open." 
    "It's a tiny little square hole, painted black with a small cushion where the key should have rested."
    brian "Hold on, one sec-"
    scene bookcase open key 
    "He quickly puts the key back on the pillow."
    menu: 
        "Take the key.":
            play sound tink
            $havebigkey = True 
            jump hallway
        "Take the key while staring directly at Brian.":
            "Brian stares back at you."
            brian "I realise now I could have just given it to you."
            you "Yup."
    jump hallway 

label hallwaydoors: 
    "Unlike the first door, this door has two boxes screwed on either side, painted a deep blue with yellow stars."
    you "Brian, you remembered to put the tokens back after you cleaned them, right?"
    brian "Yes Boss!" 
    menu: 
        "Look at the Moon Box":
            jump moonbox
        "Look at the Sun Box":
            jump sunbox

label moonbox: 
    scene hallway_moon
    "This case has a moon carefully painted on it, surrounded by stars. A large teardrop shaped hole sits in the front."
    menu: 
        "Put the gem into the slot" if hasGem: 
            $ endRoute = "moon"
            scene hallway_moon_gem
            ## tink sound 
            "The gem fits perfectly into the hole, and after a little bit of fiddling, it settles inside."
            "You can feel under your fingertips something loosen. And the front lid opens easily."
            jump ballroom_start
        "No":
            "You leave it alone."
            jump hallway 

    jump hallway 
label sunbox:
    scene hallway_sun
    "A sun decorates this case, with squiggly rays against a dark sky. On the front lies a large teardrop shaped hole." 
    menu: 
        "Put the gem in the slot?" if hasGem:
            scene hallway_sun_gem
            $ endRoute = "sun"
            ## tink sound 
            "The gem fits perfectly into the hole, and after a little bit of fiddling, it settles inside."
            "You can feel under your fingertips something loosen. And the front lid opens easily."
            jump ballroom_start
        "No":
            "You leave it alone."
            jump hallway 
    jump hallway 

label gemcase: 
    scene gemcase
    "The gem lies inside large thick glass, nestled comfortably in a small platform. It glitters brilliantly under the warm light."
    "And of course, there was the large, bright red sign hanging above it. DO. NOT. BREAK!"
    "It almost completely fills your vision."
    menu: 
        "Break the glass.":
            "Shiny. Red. Glittering. The Gem calls to you from the void."
            "Give in."
            "Give IN."
            "GIVE IN!"
            scene black
            brian "Hey what are you doing with that lamp-"
            stop music
            "SMASH!"
            "..."
            #Black
            "Not only did you break your own set, you even managed to cut your hand."
            "You had no choice but to delay the opening of your new escape room."
            "Lock n Key studios closed down not a month later."
            "But."
            "You had a shiny new toy with you."
            menu: 
                "End Game?":
                    return
                "Rethink your choices?":
                    jump gemcase
        "Use the key" if havebigkey: 
            "Easy as pie. You take the gem from it's cushion. Each facet refracts the yellow light like glitter and casted pretty glitters over the walls."
            "Brian looks pleased for you too."
            $ hasGem = True 
        "Leave the case.":
            jump hallway
    jump hallway 

label ballroom_start: 
    "The box was empty."
    play music haunted_hijinks fadein 1.0
    "Wait, why...?"
    "You stare at the empty box, the little pedestal where the 'relic' should be. Nothing."
    "You look at Brian."
    "He looks just as confused as you are. Which is even more worrying."
    show brian default at left 
    brian "I know I put it in there, honest!"
    show brian panic at left: 
        jump 
    neil_v "MUAHAHAHAHAHAH~"
    neil_v "FOOLS! DID YOU THINK I WOULD PUT MY RELICS OF POWER IN SUCH FLIMSY SECURITY!?"
    "Megan wandered into the hallway. Her eyes immediately lock onto the empty case."
    megan "Seriously?"
    show megan default at right 
    "She looks mildly more annoyed than she usually does."
    megan "What is he doing this time?"
    brian "I don't know! Um-He said something about wanting to talk to the Boss about adding something before the runthrough." 
    brian "But since the Boss was late, I thought he just forgot about it!"
    brian "What do we do? This isn't in the script at all!"
    megan "What exactly did he say?"
    brian "Uh-uh-a boss fight?"
    "Both you and Megan slowly turn to Brian incredulously. Even he seems to realise what he just said."
    megan "A boss fight? In an escape room?"
    neil_v "IF YOU WISH TO VANQUISH ME, COME TO THE BALLROOM! WHERE WE SHALL HAVE A BATTLE FOR THE AGESSS!"
    "Obviously, physically fighting the vampire was not part of the game. You had no idea how he'd planned this, or even if there was a plan."
    you "Megan, can you try and find him?"
    "Megan nodded, and glided to the staff door at the other end of the hallway." 
    megan "It's locked."
    "Damn it."
    you "Try the other entrance, around the back."
    hide megan default 
    "Megan groaned, but obeyed. Her tattered wedding trailed fluttered as she disappeared through the main hall."
    "Meanwhile, Brian was pacing in tight little circles."
    brian "What-what do we do, boss?"
    you "Come with me." 
    "Brian gives you a short, quick nod. His feet nervously tapped against the ground as your hand clasped the painted gold handle." 
    "You couldn't blame him. You weren't sure what you'd find on the other side of the door either. But there really was only one way to find out."
    "The door opens smoothly, the air pressure changed, and the temperature dropped a degree."
    "Both you and Brian stepped through the threshold and...."
    scene ballroom
    play music haunted_hijinks
    "Nothing."
    show brian panic 
    brian "Wh-where is he?"
    "There was a tremor in Brian's voice as he tiptoed across the fake marble tiles."
    "THUNK!"
    show brian panic: 
        jump 
    "Brian actually shrieks and jumps a foot in the air."
    show ballroom with vpunch 
    "THUNK THUNK!"
    "Despite it's grand name, the ballroom wasn't actually that large, there weren't many places for Neil to hide." 
    show ballroom with hpunch 
    "MMMmph! MMMPH!!"
    "Except one."
    "The coffin. Originally, once the puzzle was complete, Neil was meant to open the door to 'confront' the players, then depending on whether they used the Sun Lantern or the Moon dagger, they would be lead to two different endings."
    "It connected straight into a smaller room, where Neil could wait or go to the staff room. So why...?"
    show ballroom with hpunch 
    ## thunk sound 
    "*Thunk!* *Thunk!*"
    "Something was hitting the lid of the wood."
    show ballroom with vpunch 
    neil "Help! I'm stuck!!"
    "Well that's...anticlimatic."
    show brian panic: 
        offscreenleft 
        normal 
        walkto(centerright)
    "Brian immediately ran to the coffin and started trying to pry the lid open with his fingers."
    brian "Neil, open the door!"
    neil "I can't!"
    brian "I MEANT THE OTHER DOOR!"
    neil "The-the handle is stuck! I can't move it!"
    you "Neil, there's an emergency unlock in the staff room, Megan's heading there. She can let you out."
    "The thumping stops. Too abruptly." 
    neil "..."
    "Your stomach sinks into your gut."
    you "Neil. Did you lock both doors to the staff room?"
    neil "...Yeah."
    "Looks like you have a stuck vampire on your hands."
    "Even if you had the heart to leave him in there, the props he had were the main part of the escape room! You didn't have enough time to change it."
    "You could call the fire department to get him out, "
    "The question wasn't whether you should. The question was..."
    menu: 
        "How?":
            jump ballroom
    jump ballroom 

label ballroom: 
    call screen ballroom 

label coffin:
    scene ballroom coffin  
    "The coffin is rattling rather loudly. Maybe you bolted it a little too tight to the wall."
    "Unfortunately, the entire lid was lined with a strong magnet. Nothing short of a power outage could open it now."
    "Brian is looking at the walls, which is worrying in of itself, while Megan is leaning against a pillar, chilling."
    menu: 
        "Speak to Brian":
            jump brian_ballroom
        "Speak to Megan":
            jump megan_ballroom

label megan_ballroom: 
    scene ballroom 
    show megan default 
    "Megan arrived barely five minutes later, arms folded."
    megan "So Neil's really stuck? Damn." 
    megan "He's really getting into the role now."
    megan "How much oxygen do you think he's used already?"
    you "It's not airtight, there's vents."
    megan "Ah, right. You should probably make sure Brian doesn't try to use them to get to Neil."
    you "Because he'll get stuck?"
    megan "Because he'll get stuck."
    "Megan takes out her phone."
    megan "Say the word, and I'll get the fire truck here. Maybe the police, if you want."
    "It was definitely the most sensible solution. Neil had definitely messed with company property"
    "But..."
    "Megan seems to sense your hesitation."
    megan "Look, I don't particularly care about escape rooms or this company or whatever." 
    megan "But I want to get paid. And I know what'll happen to this place if the trucks come. The mall will cut this place like a tumor."
    megan "So it's your call."
    you "Thanks, Megan. I'll keep it in mind." 
    hide megan default 
    jump ballroom

label brian_ballroom: 
    scene ballroom 
    show brian default 
    brian "Hey Boss!"
    brian "Do you think I can fit in those vents? I've been kind of going ham on the candy, but I think if I take off my mask I can fit in!"
    you "Brian, please no. We can't afford another employee getting stuck."
    brian "Okay."
    brian "Um..Boss?"
    brian "Is it okay if you-uh-give Neil a break?"
    brian "He's-look, we kind of know each other. He's-he's not normally like this."
    brian "He was really quiet and shy."
    brian "And this is his favorite holiday, so maybe-maybe he got too excited?"
    you "I'll...think about it."
    hide brian default 
    jump ballroom 

define pianoKey = [1, 2, 3, 4, 5]
define pianoKey_Try = []
label piano: 
    scene ballroom piano
    "Red paint has been splattered against the keys to look like blood."
    "Some keys have less paint on than others."
    menu: 
        "Play the piano.":
            jump pianoCodeCheck
        "Leave it alone.":
            jump ballroom 
    jump ballroom 

label pianoCodeCheck: 
    "There isn't a chair to sit on, so you have to bend a little awkwardly."
    menu pianoplay: 
        "Press the far left piano key.":
            #play sound piano1
            $ pianoKey_Try.append(1)
            jump pianoplay
        "Press the middle left piano key.":
            #play sound piano2
            $ pianoKey_Try.append(4)
            jump pianoplay 
        "Press the middle key.":
            #play sound piano3
            $ pianoKey_Try.append(3)
            jump pianoplay
        "Press the middle right piano key.":
            #play sound piano4
            $ pianoKey_Try.append(2)
            jump pianoplay
        "Press the far right key.": 
            #play sound piano5
            $ pianoKey_Try.append(5)
            if pianoKey_Try == pianoKey: 
                jump pianoCodeTrue 
            else: 
                jump pianoplay 
        "Give up":
            $ pianoKey_Try = []
            jump ballroom 
label pianoCodeTrue: 
    stop music fadeout 1.0 
    play music communisumbra
    play sound gurgle 
    "The piano starts to play itself, undercut by a low burbling sound coming from the pillar."
    "It seems something has happened."
    jump ballroom 
    
label pianocheck: 
    python: 
        if lens(pianoKey_Try) == 5: 
            if pianoKey_Try == pianoKey: 
                renpy.jump("pianoCodeTrue")
            else: 
                pianoKey_Try = []
                renpy.jump("pianoCodeCheck")
        else: 
            renpy.jump("pianoCodeCheck")
    


define banquetTableKey = ["eye", "fingers", "fruit", "flower"]
default banquetTable_Try = []
default bloodLevel = 0 

label banquetTable:
    scene ballroom banquettable
    "There's a huge array of fake food and body parts on the table. A veritable horror-feast, if you could stomach plaster in your teeth."
    "There are ears, fingers, flowers, and even a large plaster heart on a dish."
    "A scroll lays rolled up on the side."
    menu banquetchoice: 
        "Check the note.":
            ## paper sound 
            "Potion of Weakening."
            "Five servants joined together."
            "An orb, of which all rely, even as it lies."
            "Thin skin reveals tender sweet flesh inside."
            "Add perfumed scent, fresh from the cemetary made to mourn the dead."
            "Add all into the bowl, and bring it to the blood."
            "With it, the vampire will weaken."
            jump banquetchoice
        "Take a closer look at the table.": 
            "You grab a nearby empty bowl for ease."
            jump banquetTry 
        "Finish":
            jump ballroom 
    jump ballroom 

label banquetTry: 
    menu: 
        "Add Eyes.": 
            play sound tink 
            "The little round ball rolls around as you place it on the bowl.." 
            $ banquetTable_Try.append("eye")
            jump banquetTry
        "Add Hand": 
            play sound tink 
            "Another ingredient in the bowl."
            $ banquetTable_Try.append("fingers")
            jump banquetTry
        "Add the Heart": 
            play sound tink 
            "It's quite large, you rest it in the center for balance."
            $ banquetTable_Try.append("heart")
            jump banquetTry
        "Put a fake chocolate.": 
            play sound tink 
            "Even if it was fake, you were starting to feel a little hungry. Hopefully the stores would give you a discount."
            $ banquetTable_Try.append("chocolate")
            jump banquetTry
        "Cont.":
            jump banquetTryCont
        "Finish.": 
            jump banquetTable

label banquetTryCont:
    menu: 
        "Place a Fruit": 
            play sound tink 
            $ banquetTable_Try.append("fruit")
            jump banquetTryCont
        "Take a flower.": 
            play sound tink 
            "You very carefully take a rose from the vase."
            $ banquetTable_Try.append("flower")
            jump banquetTryCont
        "Add Batwings.":
            play sound tink 
            "It feels leathery under your fingers." 
            $ banquetTable_Try.append("batwings")
            jump banquetTryCont
        "Add spiders.":
            play sound tink
            "Gingerly, you pick up a fake spider by its leg."
            $ banquetTable_Try.append("spider")
            jump banquetTryCont
        "Empty the bowl": 
            play sound tink
            "You put all of the ingredients back where they belong." 
            $ banquetTable_Try = []
            jump banquetTryCont
        "Finish":
            jump banquetTable


label pedestalBlood:
    scene ballroom
    "The stone pedestal stands right in the middle of the room. This was important to solving the puzzle, you know."
    "A second, smaller pillar stands near it, with a small round indent perfect for a bowl."
    if bloodLevel == 0:
        scene ballroom bowl01
        "The granite bowl is bone dry. You see the tiniest little spout at the base of the bowl."
    elif bloodLevel == 1: 
        scene ballroom bowl02
        "There's a thin layer of dark red liquid in the bowl."
    elif bloodLevel == 2: 
        scene ballroom bowl04
        "The blood level is full, and burbling too, the hidden pipe was now spewing little compressed air bubbles under the liquid."
        jump pedestalSolve
    menu: 
        "Put bowl of ingredients in the indent." if banquetTable_Try != []: 
            python: 
                for item in banquetTable_Try: 
                    if item not in banquetTableKey: 
                        renpy.jump("pedestalFail")  
                    else: 
                        bloodLevel += 1
                        banquetTable_Try = []
                        renpy.jump("pedestalTrue")
        "Leave the pedestal alone.": 
            jump ballroom
                
    jump ballroom 
label pedestalTrue: 
    "As you place the ingredients down, you hear a small click."
    play sound gurgle
    "Then, burbling fills the room."
    jump pedestalBlood


label pedestalFail: 
    "You wait, but nothing happens. You take the bowl of ingredients back. Best try again." 
    jump pedestalBlood

default sawPM=False 
default sawWrappers = False

label pedestalSolve:
    "The plinth to the right begins to glow slightly. That meant it was active, but..." 
    show megan default at left 
    megan "Huh."
    "Megan and Brian had been busy trying to pry the lid of the coffin open, but to no avail. Now, they wander towards you."
    show brian default at right 
    brian "b-boss, what are you doing?"
    you "I was trying to see if we could open the coffin using the puzzle."
    "Brian's posture straightens as something inside him clicks."
    brian "Oh! That's smart!"
    megan "Not really, Neil took the tokens, remember?"
    brian "Ah. Right."
    brian "Maybe if all four of tried, we could make a gap big enough that he could slide them through?"
    megan "Or chop his fingers off."
    neil "I WOULD LIKE TO KEEP MY FINGERS PLEASE."
    brian "Mmmaybe we could just push it?"
    "Brian immediately sticks his thumb into the hole and presses. Nothing occurs."
    megan "Wouldn't be much of an escape room if the whole thing was just 'push a button.'"
    you "It's not a button, the token is metal, so when you put it into the slot, it allows an electrical charge to turn off the magnets keeping the lid closed."
    "Brian takes his hand out so fast it almost looked like he was shocked."
    brian "An-an electric shock!? That's-that's dangerous!"
    megan "So we need metal."
    brian "A round metal thing. Like a coin?" 
    "You all start turning out your pockets." 
    "Megan's pockets had her phone and a peppermint."
    "You didn't have much, you left most of your things in the locker before arriving. Just a pen and a sheet of paper."
    "Meanwhile Brian had a key, some paper receipts and..."
    megan "Why do you have so many wrappers?"
    brian "I get the munchies when I get bored. So I brought some snacks from home." 
    you "How do you two not have coins?"
    megan "I usually use my phone."
    brian "I left my wallet in the locker...It kept falling out of my pants."
    "You have something here, but what?"
    menu items: 
        "Look at the Key.":
            megan "What's this for?"
            brian "It's the key to my house! I always keep it with me, just in case!"
            "Well, unless you could melt it down under a fake candle, it wasn't going to be entirely helpful."
            "Though..."
            jump items 
        "Look at the peppermint.": 
            $ sawPM = True 
            megan "Don't you dare eat it."
            brian "I've never seen someone like peppermints so much."
            megan "It's literally the only thing keeping me awake right now."
            brian "Concerning!"
            jump items 
        "Look at the wrappers.": 
            $ sawWrappers = True 
            megan "What's with these wrappers? Aren't they kind of thick?"
            brian "Oh, these aren't store stuff, these are homemade! My ma likes to make homemade stuff for Trick or Treating."
            megan "..."
            you "..."
            megan "Somehow that explains a lot." 
            brian "?" 
            jump items
        "You have an idea..." if sawWrappers and sawPM: 
            "This was going to be so dumb."
            megan "What are you planning?"
            you "Brian...give me the wrappers. Megan, I'm sorry, but can I borrow your peppermint?" 
            megan "...Fine."
            "You take the wrappers, then the peppermint, then get to work."
            "Finally, you get a peppermint wrapped in foil!"
            "It would be a terrible conductor, but you didn't need that much of a charge."
            megan "This is the stupidest thing I've ever seen."
            "And yet...As you shove the peppermint into the slot, something behind you guys clicked."
            jump end 

        
        





label end:
    scene ballroom 
    show brian default at left
    show megan default at right
    show neil sad at center: 
        vibrate(10)
        ypos 0.4
    
    "With the final piece in place, the coffin door swings open, and a floppy pile of stick thin limbs and black velvet cloth crumples to the floor."
    show neil sad at center: 
        ypos 0.3
    play music timeforrest
    "Neil gasps, flops over onto his back."
    neil_v "Imp-Impossible-gasp! I am-wheeze-the great Count Blud-!"
    megan "Dude."
    "Neil's eyes take a moment to focus on Megan's face. Then Brian's, and then yours."
    neil "...I messed up big time, didn't I?" 
    brian "Are you okay, Neil?"
    neil "Could be-better. It's stuffy in there." 
    megan "You could have taken off the costume."
    neil "Yeah. I guess."
    brian "I'll go grab some water, there's some at the cooler out front, right?"
    you "Yeah, got it for the receptionists. You'll have to ask them."
    brian "No worries! They like me!"
    "Yeah, he did kind of have the 'cutie patootie' vibe older women seemed to adore."
    "Brian bolts to the door, and vanishes out the front."
    hide brian default 
    show megan default at rightish 
    show neil sad at leftish
    megan "So, boss, what do we do?"
    "You slowly turn to Neil, who gingerly stands up."
    show neil sad: 
        ypos 0.0
    "His hair was stuck to his head, and he was visibly melting."
    you "First off, Neil? Give."
    show neil sad: 
        pickup 
        2
    "Neil automatically hands you the two small discs and the metal key."
    you "Do you understand what you did wrong, Neil?"
    neil "I...should not have hijacked the entire escape room runthrough right before it opened."
    you "and?"
    neil "Stole company property."
    you "and?"
    neil "And...lock myself in a coffin."
    show ballroom with vpunch
    you "...AND?" 
    neil "And-uh-Oh, right. Locked both entrances to the staff room."
    you "You do realise how much of a fire hazard that was, right?"
    neil "Yeah...I'm sorry." 
    neil "It was dumb and stupid and-I panicked. Badly."
    neil "I really like this place, so when you hired me-I got really excited."
    neil "If you fire me...I understand. And even then, I'll-I'll make up for it, somehow."
    you "..."
    you "Look, this place is very important to me too."
    you "That's why what you did was not okay."
    you "Not to mention, you could have gotten hurt." 
    you "That being said, your...antics did reveal more than a few problems with the room."
    you "Security concerns that will have to be rectified later."
    you "So you can work today. But you have to stick to the script."
    you "And afterwards..."
    menu: 
        "Fire Neil": 
            you "You'll be fired."
            "Neil droops, but he seems to nod and understand."
            "Megan looks on with an unreadable expression on her face."
        "Put Neil on cleaning duty.": 
            you "You're on cleaning duty tomorrow, and for the rest of the week."
            neil "So I...get to keep the job?"
            you "And if you actually behave, you might be able to get Count Blud again."
            "Megan shifts and shrugs." 

    megan "A suggestion, Boss?"
    you "Yeah?"
    megan "We haven't finished the runthrough yet."
    "Oh right. You and Megan look at Neil, who had been looking at the coffin."
    neil "Huh? Me?"
    you "You saw what I picked in the hallway, right?"
    "You can see the cogs turning in that young adult's head, before it clicked."
    neil "Ahem."
    show neil sad: 
        jump 
    show neil default: 
        jump
        ypos 0.0
    "He quickly gets into character, hair mussed, but back fully straight."
    if endRoute == "moon": 
        "The vampire stalks towards the halpless captives."
        neil_v "Such fools! How {i}easy{/i} it was to deceive you." 
        neil_v "My servant has always been loyal to me, he shall be greatly rewarded!"
        neil_v "Did you truly think you could stop me?"
        neil_v "Ah, with my Moon Dagger in my midst, I can feel my strength returning to me! The Bride will suffer for her transgressions, but first!"
        neil_v "IT WILL BE EASY TO DEVOUR YOU! MUAHAHAHAH!"
    elif endRoute == "sun": 
        "With a cringe, the vampire collapses onto the floor."
        neil_v "GAH! ZOUNDS! THE SUN LANTERN?!"
        neil_v "How could my servant fail me!? Curse you, Bride!"
        neil_v "My powers! My mansion! I have lived for centuries! How could I, the great COUNT BLUD, be bested by some mere mortals?!"
        neil_v "AGH! I'M MELTING! {sc}MELTING!!!{/sc}" 
        "The vampire collapses onto the floor, and after a little more gasps, lays still."

    megan "..."

    "She claps politely as Neil recomposes himself."

    neil "How did I do? Too much? Not enough?" 

    you "Just right, Neil."
    brian "Uh-guys?!"
    show brian default 
    "Suddenly, Brian is standing at the ballroom entrance. Four cold water bottles somehow dangling from his hands."
    brian "You-uh-there's-pee-pe-"

    megan "Pee?"

    brian "There's people, lots-lots of people!"
    play music swing

    scene shops_warm 

    "The noise greets you before the sight does. A buzzing hum of voices that rise and fall."

    "Outside, you see the source."

    show demon at right 
    show nova at left 

    "A rather sizable crowd was waiting at the front. More than you'd ever seen."

    hide demon 

    show vega at right 
    show nova at left 
    
    "Many of them had halloween costumes on, and all of them looked like they were waiting for something to happen." 

    hide vega
    hide nova

    show kiddo at right 

    show larissa at left 

    show megan default 

    megan "What the hell? Why are there so many?"

    hide megan default 
    show brian default 

    brian "I don't know! Do-oh gosh, are we going to be able to handle this?"

    "Neil looks outside, unusually quiet."
    hide brian default 

    show neil default 

    neil "I uh- may have told my theatre troupe about this place."

    show megan default 

    megan "Is your theatre troupe a small army?"

    hide megan default

    show neil default 

    neil "I might have told them to tell their friends. And family."

    "You stare at the crowd, take a deep breath, and roll your shoulders."

    you "Looks like it'll be a long night."

    hide kiddo
    hide larissa

    show megan default at left
    show brian default at right 

    megan "I better get overtime."

    brian "Let's go!"

    "Neil takes a deep breath and smiles."

    "With a deep breath, you open the doors."

    scene black with fade 

    "All in all, not the worst runthrough you'd ever done."

    "END"

    return 
