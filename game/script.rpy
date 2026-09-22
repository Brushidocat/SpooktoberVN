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

    menu: 
        "ChestCode":
            jump chest_code
        ""


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



    jump mainhall_start

label mainhall_start: 
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

    jump mainhall 
    
label mainhall: 
    show screen mainhall 

##Keys and important flags for Mainhall 

define chestKey = "urem"
default chestisLocked = True 
default chestKey_try = ""
default gargoyleisLocked = True 
define gargoyleKey = {"red", "blue", "blue"}
default gargoyleKey_try = {}
default tabletCollected = 0 

label letter: 
    "Each word inside the letter was wriiten as clearly as possible."
    "{i} Dear Unfortunate So{color=red}U{/color}l,"
    "{i} If you are reading this, then I fea{color=red}R{/color} the worst has come to pass.{/i}"
    "{i} Fear not, if you are unsure where to start, the hint is close at hand.{/i}"
    "{i}Signed, a fri{color=red}E{/color}nd."
    "{i}PS, do not trust the bride, she {color=red}M{/color}erely wants more company."

label chest: 
    "There's a large chest. It's been rather roughly painted gold, but the material is genuine wood."
    if chestisLocked == True: 
        "There's a large lock keeping the chest shut. It's one of those word-based locks, with four turning dials."
        "Try the code?"
        menu: 
            "Yes.":
                jump chest_code: 
            "No":
                jump mainhall 

label chest_code: 
    python: 
        chestKey_try = renpy.input()
        chestKey_try = chestKey_try.strip()
        chestKey_try = chestKey_try.upper()
    if chestKey_Attmpet == chestKey: 
        "The lock clicks open and you put it to the side."
        menu: 
            "Open the chest.":
                "Using two hands, you push the lid open."
                "Inside is barren, only a broken piece of tablet lays at the bottom."
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
    
                

label paintings:
    ##TODO: Make this an imagemap? 
    "A row of paintings."
    menu paintings: 
        "Look at the first painting.": 
            "It's a picture of a desolate landscape with a red moon, a dark blue mountain in the background, and a "
            jump paintings 
        "Look at the second painting.": 
            "Here is a regal portrait of a garden filled with white roses, "
            jump paintings
        "Look at the third painting.": 
            "A portrait of an extremely pale man. He wears a red brooch, a black cape, and has a white dagger in his hands."
            jump paintings 
        "Go back.":
            jump mainhall 
    return 

label gargoyle: 
    "A gargoyle stands on a stone podium."
    "You made it yourself using paper-mache and some stuff you salvaged."
    "With a curved beak, large wings, and hooked claws, it was suitably an impressive piece. You based it on a certain cartoon you watched as a kid."
    if gargoyleisLocked == True: 
        "There's something in it's jaws, you can't see it from here though."
    menu: 
        "Check the base.":
            "Below the gargoyle, is a row of buttons with colored images on them."
        "Leave.": 
            jump mainhall 

define codenumber = 0 

label gargoyle_code: 
    if codenumber > 0: 
        menu: 
            "Press the red button.": 
                $ gargoyleKey_try = gargoyleKey_try.append(red)

            "Press the blue button.":

            "Press the green button.":
    else if gargoyleKey == gargoyleKey_try:
        "The tablet loosens from the gargoyle's grip. You take it out easily."

label carpet: 
    jump mainhall 

default mainhall_Doors = True
default mh_incantation = ""
define mh_incantation_try = ""

label mainhall_Doors: 
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
        mh_incantation_try = renpy.input()
        mh_incantation_try = mh_incantation_try.strip()
        mh_incantation_try = mh_incantation_try.upper()
    if mh_incantation_try == mh_incantation:
        jump mainhall_End
    else: 
        "You try the door, but it doesn't budge. Maybe you did it wrong?"
        menu: 
            "Try again.":
                jump MainhallDoors_Code
            "Leave.":
                jump mainhall
        
label table: 
    #TODO: Drag and Drop?
    "The large wooden table dominates the room. There are several scratches all over the front. Some of them end abruptly, forming a rectangle in their negative space."
    menu: 
        "Put the tablets down on the table." if tabletCollected == 3: 
            ##Insert Drag and Drop
        "Go back.": 
            jump mainhall 


default brideHints = 0

label Megan: 
    "Megan looks at you as you approach and stuff her phone back in her pocket."
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
    else if brideHints == 1: 
        megan_b "{i}I've seen those paintings move and shake sometimes, as if they are alive. Perhaps you should take a closer look."
        megan "Hey, do I have to clean off fingerprints off those frames every time they check them?"
        $ brideHints += 1 
    else if brideHints == 2: 
        megan_b "{i} The great beast contains part of the code in its mouth. It seems to have a fondness for the paintings in this gallery.{/i}"
        megan "Have to admit, I like the gargoyle."
        megan "Once this is all over, you mind if I take it home? I can use it to scare the neighbors."
        megan "You sure people'll notice those hints on the paintings?" 
        $ brideHints += 1 
    else: 
        megan "That's all I got for you, boss."
        megan "Unless you want to talk about my salary."
    jump mainhall 

label mainhall_End: 
    "The moment the three words leave your mouth, the door should have unlocked and swing open on its own, as if by a ghost."
    "Instead-"
    neil_v "HOW HOW COULD YOU HAVE FIGURED OUT MY SECRET PASSWORD!? INCONCEIVABLE!!!"
    "He sounds a little different, as if he had something in his mouth."
    neil_v "COULD IT BE?! CURSE YOU, MY FORMER BRIDE!" 
    "Megan ignores him."
    neil_v "NO MATTER! EVEN WITH HELP, THERE'S NO WAY YOU SHALL DEFEAT MEE!" 
    neil_v "MUAHAHAHAHAHAHAHA-ack."
    neil "*Cough*! *Cough*!"
    you "You alright there?"
    neil "I-hrk! NO BREATH MINT CAN-gack-STOP ME! I SHALL RETUUUURN."
    megan "Open the door Neil."
    "Silence."
    "The double doors unlock with an audible click. Then the PA system turned off."
    megan "See ya, Boss. Catch you after the break."
    jump hallway_start



default haveGem == False 
default bookcaseCode = ""
define bookcaseCode_try = ""
define drawerCode = ""
define drawerCode_Try = ""
default endRoute = ""
    

label hallway_start: 
    "Long and thin, the hallway stretches out in front of you. The door on the other side was flanked by two large boxes. One yellow, one blue. And there, standing on the side of the room trying to right a chair, was a long, lanky figure."
    "His pumpkin mask glows faintly like the fake torches in the banisters. His cheap suit is slightly wrinkled."
    brian "Hey boss! Er-Oh, sorry. One sec." 
    "He finally turns the chair upright, then straightens his back."
    brian_s "{i}Ah! Another guest for the master?"
    brain_s "{i}Poor soul, much like the pale megan-madam-{/i} shit-"
    brian_s "{i}Much like the pale madam next door, you have been trapped here. I assume she's tasked you with getting the Sun Lantern?"
    "The pumpkin headed servant shook his head."
    brian_s "{i}Don't be fooled, she's merely distracting you. She is a lonely spectre." 
    brian_s "{i}You should find the moon dagger instead! It is his main source of power. Without it, he will have nothing.{/i}" 
    brian_s "{i}Who knows, perhaps you may even become the new count!{/i}"
    brian_s "{i}I'm quite tired of his Lord Count Blud myself,"
    brian_s "{i}The master is quite clever, however. He's encased both artefacts in magical containers, there is only one key, the Blood Ruby." 
    "He gestures behind you, where a large glass gem resides inside a glass case." 
    "Underneath, in large industrial text, was the phrase: DO NOT BREAK!"
    brian_s "{i}I would open the case itself, but avast-alas, I have no way to open it myself!"
    "Something falls out of his pocket. A thick, heaavy looking key that looks like ti would perfectly fit the lock on the glass case. He pauses, unblinking, looks down, then looks back up. Then lunges for the key and shoves it into his pocket."
    brian_s "{i}P-perhaps you can find it? Remember though, the Ruby can only be used once! Choose wisely who you side with.{/i}"
    "After a brief pause, he rights himself and takes off the mask with a bright smile."
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
    "Brian quickly jams the helmet back on his head. With a quick thunk, the light flickers back on, and he starts pretending to dust the furniture."
    jump hallway 

label hallway: 
    call screen hallway

label brian: 
    "Brian perks up when you approach him."
    brian "Something up, boss?"
    you "Do you remember the hints?"
    brian "Oh right! Yes I do! You want me to recite them?" 
    menu: 
        "Yes,":
            jump servant_hints
        "Not right now.":
            brian "Alright, I'll be right here."
            jump hallway 

default servantHints = 0 

label servant_hints: 
    if servantHints ==0: 
        brian "Alright, alright. *ahem*"
        brian_s "{i}Are you stuck, dear guest? Fear not, while I do not know the exact location of the key, perhaps a look around the area will do you well?"
    else if servantHints == 1:
        brian_s "{i}Feel free to explore more of the mansion. The main hall is always available to you."
    else if servantHints == 2: 
        brian_s "{i} The master has a fondness for mirrors. Windows to the soul, he says. And yet, I've never gotten a glimpse of his reflection."

default havePaper = False 

label firstdrawer: 
    "You open the drawer. It opens smoothly. Until it gets halfway. Then it stops."
    "You try again. Nothing. It feels like the drawer's hit something solid."
    "Immediately, Brian comes over."
    brian "Huh, that's weird."
    brian "Here, let me-"
    ##Shake 
    "He grips the handle and tugs a little harder. It doesn't budge."
    brian "Maybe some paint got in the-Hang on."
    "The drawer rattles ominously as he yanks harder. And yet still, it doesn't move." 
    brian "COme onnnn-!"
    "THUNK!"
    "The drawer suddenly flies open, and Brian stumbles backwards. Eyes wide, limbs flailing, his back hits the opposite wall." 
    megan "Did Brian fall again?"
    brian "I'm fine!"
    "There's a few things inside the second drawer. A piece of paper, and a small wooden clock with numbers on them."
    menu: 
        "Check the paper.":
            "Dear His Most Illustrious Count Blud,"
            "As you have requested, I have taken care to hide the key to the Blood Ruby in a secure place."
            "I have hidden it within the hallways of our castle, and the code closeby."
            "No one shall be able to REVERSE the curse you've casted on this place."
            "Your most loyal servant, the Pumpkin."
            "PS. eerhT ytneveS derdnuH eviF dnasuohT ytnewT."
        "Look at the clock.":
            "The clock is just a shell. There isn't anything inside. Instead, some of the numbers on the front have small colored paint underneath them."
            menu clockcheck: 
                "Put down the clock.":
                    "You put the clock back into the shelf."
                "Inspect the clock.":
                    "Underneath, you spot some clumsily carved words. MAIN HALL."
                    jump clockcheck
    jump hallway 

label mirror: 
    "The mirror has been polished to an almost perfect shine and hung proudly."
    menu: 
        "Place the paper to the mirror?":
            "You hold the paper to the mirror, and immediately you see words."
            "Decoded, it writes:"
            "Twenty Thousand Five Hundred Seventy Three."
        "Leave.":
            jump hallway 

label drawer: 
    "There is a small drawer shoved to the left wall with two shelves."
    menu: 
        "Try the top shelf.":
            jump firstdrawer
        "Try the lower shelf.":
            jump seconddrawer 
        "Leave.":
            jump hallway 

label bookcase: 
    "Approaching the bookcase reveals obvious signs of most of the books being glued together. That was mostly to reduce cleanup, and because one time Brian bumped his elbow on the bookshelf and toppled every single book onto the floor. On top of him."
    "It bulges conspicuously from the wall, and rails are fixed to the top and bottom of it."
    "He was fine, thankfully."
    "The floor on the other hand...It was good they were having a carpet sale at the depo."
    "As you get closer to the bookcase, Brian immediately perks up and, doing his best to be inconspicuous, shuffles closer to you. He keeps glancing at it in intervals."
    menu: 
        "Look at the bookcase closer.":
            "Walking to the side, you spot a small keypad with numbers."
            menu tryBookcase: 
                "Try a code?":
                    jump bookcase_code
                "Leave the bookcase."
    jump hallway 

label bookcase_code: 
    python: 
        bookcaseCode_try = renpy.input()
        bookcaseCode_try = bookcaseCode_try.strip()
        bookcaseCode_try = bookcaseCode_try.upper()
    if bookcaseCode_try == bookcaseCode:
        jump hiddenCompartment
    else: 
        "There is a faint negative *beep* as you get the code wrong."
        "Brian inches a little closer, opens his mouth, then closes it."
        jump tryBookcase




label hiddenCompartment: 
    "The hidden compartment swings open." 
    "It's a tiny little square hole, painted black with a small cushion where the key should have rested."
    brian "Hold on, one sec-"
    "Tink, goes the key back on the pillow."
    menu: 
        "Take the key.":
            jump hallway
        "Take the key while staring directly at Brian.":
            "Brian stares back at you."
            brian "I realise now I could have just given it to you."
    jump hallway 

label moonbox: 
    "This case has a moon carefully painted on it, surrounded by stars. A large teardrop shaped hole sits in the front."
    menu: 
        "Put the gem into the slot" if hasGem: 
            $ endRoute = "moon"
            "The gem fits perfectly into the hole, and after a little bit of fiddling, it settles inside."
            "You can feel under your fingertips something loosen. And the front lid opens easily."
            jump ballroom_start
        "No":
            "You leave it alone."
            jump hallway 

    jump hallway 
label sunbox:
    "A sun decorates this case, with squiggly rays against a dark sky. On the front lies a large teardrop shaped hole." 
            menu: 
                "Put the gem in the slot?" if hasGem:
                    $ endRoute = "sun"
                    "The gem fits perfectly into the hole, and after a little bit of fiddling, it settles inside."
                    "You can feel under your fingertips something loosen. And the front lid opens easily."
                    jump ballroom_start
                "No":
                    "You leave it alone."
                    jump hallway 
    jump hallway 

label gemcase: 
    jump hallway 

label ballroom_start: 
    "The box was empty."
    "Wait, why...?"
    "You stare at the empty box, the little pedestal where the 'relic' should be. Nothing."
    "You look at Brian."
    "He looks just as confused as you are. Which is even more worrying."
    brian "I know I put it in there, honest!"
    neil_v "MUAHAHAHAHAHAH~"
    neil_v "FOOLS! DID YOU THINK I WOULD PUT MY RELICS OF POWER IN SUCH FLIMSY SECURITY!?"
    "Megan wandered into the hallway. Her eyes immediately lock onto the empty case."
    megan "Seriously?"
    "She looks mildly more annoyed than she usually does."
    megan "What is he doing this time?"
    brian "I don't know! Um-He said something about wanting to talk to the Boss about adding something before the runthrough." 
    brian "But since the Boss was late, I thought he just forgot about it!"
    megan "What exactly did he say?"
    brian "Uh-a boss fight?"
    "Both you and Megan slowly turn to Brian incredulously. Even he seems to realise what he just said."
    megan "A boss fight? In an escape room?"
    neil_v "IF YOU WISH TO VANQUISH ME, COME TO THE BALLROOM! WHERE WE SHALL HAVE A BATTLE FOR THE AGESSS!"
    "Obviously, physically fighting the vampire was not part of the game. You had no idea how he'd planned this, or even if there was a plan."
    you "Megan, can you try and find him?"
    "Megan nodded, and glided to the staff door at the other end of the hallway."
    "Brian took a few steps towards where Megan left, paused, then turned to you with wide, panicking eyes."
    brian "What-what should I do, boss?"
    you "Come with me." 
    "Brian gives you a short, quick nod. Tapping his feet nervously as your hand clasped the painted gold handle and pulled." 
    "You couldn't blame him. You weren't sure what you'd find on the other side of the door either. But there really was only one way to find out."
    "The door opens smoothly."
    ##Show ballroom 

    "Nothing."
    "The ballroom wasn't that large, there weren't many places for Neil to hide." 

    "MMMmph! MMMPH!!"
    "Except one."

    "The coffin. It was actually a door to the staff room, connected by a short tube."
    "*Thunk!* *Thunk!*"
    "Something was hitting the lid of the wood."
    neil "Help! I'm stuck!!"
    "Well that's...anticlimatic."
    "Brian immediately ran to the coffin and started trying to pry the lid open with his fingers."
    brian "Neil, open the door!"
    neil "I can't!"
    "Looks like you have a stuck vampire on your hands."
    "Even if you had the heart to leave him in there, the props he had were the main part of the escape room! You didn't have enough time to change it."
    "The question wasn't whether you should. The question was..."
    menu: 
        "How?"
    jump ballroom 

label ballroom: 
    call screen ballroom 

label megan_ballroom: 
    "Megan arrived barely five minutes later, arms folded."
    megan "So Neil's really stuck? Damn." 
    megan "He's really getting into the role now."
    you "You saw it?" 
    megan "He set his walkie-talkie against the mic."
    megan "All I had to do was think 'what would an idiotic theatre kid do to get into his role'?" 
    megan "Plus I could hear him in the hallways."
    megan "How much oxygen do you think he's used already?"
    you "It's not airtight."
    megan "Ah, right. You should probably make sure Brian doesn't try to use the vents to get to Neil."


label piano: 
    "Red paint has been splattered against the keys, "
    jump ballroom 

label banquetTable:

    jump ballroom 

label pedestalSun: 
    jump ballroom 
label pedestalMoon: 
    jump ballroom 







label end: 
    return 
