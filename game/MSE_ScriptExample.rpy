## Motion Sells Emotion: an ATL animation pack for Ren'Py, by EdgesSystem ######
## https://edgessystem.itch.io/motion-sells-emotion ############################
## This work is licensed under Creative Commons Attribution 4.0 International ##
## https://creativecommons.org/licenses/by/4.0/ ################################

## This file contains examples/instructions for how to use these animations.
## For the animations themselves, go to MSE_transforms.rpy

layeredimage man:
    group base auto if_not "dancing":  ## 'if_not "dancing" ' required for ballroom dancing
        attribute front default
    always "mandancing_front" if_any "dancing" ## required for ballroom dancing
    group face auto
    attribute dancing "mandancing_back" ## required for ballroom dancing

## These images are used in ballroom dancing
image mandancing_front:
    animation
    "man_base_front.png"
    alpha 1
    tempo
    alpha 0
    tempo
    alpha 1
    tempo
    repeat
image mandancing_back:
    animation
    "man_base_back.png"
    alpha 0
    tempo
    alpha 1
    tempo
    alpha 0
    tempo
    repeat

layeredimage woman:
    group base auto if_not "dancing":  ## 'if_not "dancing" ' required for ballroom dancing
        attribute front default
    always "womandancing_front" if_any "dancing" ## required for ballroom dancing
    group face auto
    attribute dancing "womandancing_back" ## required for ballroom dancing

## These images are used in ballroom dancing
image womandancing_front:
    animation
    "woman_base_front.png"
    alpha 0
    tempo
    alpha 1
    tempo
    alpha 0
    tempo
    repeat
image womandancing_back:
    animation
    "woman_base_back.png"
    alpha 1
    tempo
    alpha 0
    tempo
    alpha 1
    tempo
    repeat
## This image is used in
image womanbouncing_front:
    animation
    "woman_base_front.png"
    alpha 0
    2*wallbounce
    block:
        alpha 0
        3*wallbounce
        alpha 1
        3*wallbounce
        repeat



label MSEExample:

    scene black
    menu:
        "Shot lengths and positions":
            jump shot_lengths
        "Bowing":
            jump bow
        "Walking, running, pacing":
            jump walk_to
        "Jump, jump, jump!":
            jump jumps
        "Object animations":
            menu:
                "Falling leaf/paper":
                    jump leaf
                "Pickup":
                    jump pickup
        "Looping Animations":
            menu:
                "Loop around screen":
                    jump looparound
                "Vibrating":
                    jump vibrate
                "Bouncing off the walls (zoomies)":
                    jump zoomies
                "Ghostly flicker/flickering lights":
                    jump flicker
        "Ballroom Dancing":
            jump ballroom_dancing
        "See-saw":
            jump seesaw

label shot_lengths:
    show man:
        full
        farleft
        toright
        subpixel True
    show woman:
        offscreenleft
        full
        toright

        subpixel True
    # ALWAYS enable subpixel for sprites or backgrounds that will be doing a
    # lot of moving. This removes the visual jitter.
    "The man will remain on the far left side of the screen as the camera zooms in. The woman will move from left to right."

    show woman:
        ease 1.0 left
    "Full Shot ('full' and 'left')"

    show woman:
        parallel:
            ease 1.0 centerleft
        parallel:
            ease 1.0 medlong
    show man:
        ease 1.0 medlong
    "Medium Long Shot ('medlong' and 'centerleft')"

    show woman:
        parallel:
            ease 1.0 center
        parallel:
            ease 1.0 medium
    show man:
        ease 1.0 medium
    "Medium Shot ('medium' and 'center')"

    show woman:
        parallel:
            ease 1.0 rightish
        parallel:
            ease 1.0 medclose
        toleft
    show man:
        ease 1.0 medclose
    "Medium Close Shot ('medclose' and 'rightish')\nSprites should (usually) face in the direction they're walking, so wait until after the movement to turn her around."

    show woman:
        parallel:
            ease 1.0 right
        parallel:
            ease 1.0 close
    show man:
        ease 1.0 close
    "Close Shot ('close' and 'right')\nYou might notice at this point that the sprites are getting a little crunchy. Make your sprites 5000px tall or more to avoid this."

    show woman:
        ease 1.0 closeshort
    "It is difficult to get both tall and short sprites in a close framing while maintaining scale, so fudge the short one's position a little with 'closeshort' instead of 'close'."

    show woman:
        toright
        ease 1.0 offscreenright
    "Again, sprites should face the direction they're walking, so turn her around before she walks off to the right."

    jump start

label bow:
    show man:
        center
        medlong
        toleft
        pause 0.5
        bowleft(3)
    show man as man2:
        rightish
        medium
        toleft
        pause 0.5
        bowleft(2)
    show man as man3:
        medclose
        farright
        toleft
        pause 0.5
        bowleft
    "Three men bow to the left. You can add a number between 0 and 3 to change the depth of the bow."
    show man as man2:
        ease 0.5 alpha 0.1
    show man as man3:
        ease 0.5 alpha 0.1
    "The wider the shot, the stranger this can look, since the legs could be visible."
    show man:
        ease 0.5 alpha 0.1
    show man as man2:
        ease 0.5 alpha 1.0
    "Try to keep bows to medium shots and closer so the legs are hidden below the window."
    show man:
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            unpose
    show man as man2:
        unpose
    show man as man3:
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            unpose
    "And don't forget to make them stand up straight with 'unpose' when you're done."
    jump start

label walk_to:
    show man:
        medlong
        left
        toright
        walkto(center)
    "The walkto animation takes a sprite from anywhere on screen, and makes it walk to any 'location'. By default, the walk will take five 'steps' with a 'walktime' of two seconds, but you can adjust these."
    show woman:
        offscreenleft
        medlong
        toright

        walkto(rightish)
    "You can also adjust the 'bounce' and 'sway'. Mix and match them to show a variety of energy levels."
    show man:
        walkto(leftish)
    "A sprite will not automatically turn to face the direction they are walking, allowing backwards walking."
    show woman:
        toleft
        walkto(offscreenleft,10,2,3,5)
    "It is highly recommended to turn sprites in the direction they're going {i}most{/i} of the time, however. Especially when they're running."
    hide woman
    show man:
        pacing
    "Pacing goes from any position, to the rightish position, then over to the leftish position, and loops from there. It accepts all the same numbers as walkto, but instead of a location, you can adjust how long it will 'wait' before turning to pace again."

    show man:
        center
        toleft
        pacing
    "The first pace assumes nothing about the position on screen, so you might have to face the sprite in the right direction to avoid moonwalking."
    show man:
        center
        toright
        walkloop
    "If you want a sprite to continuously walk, use walkloop instead. You can adjust its 'stepspeed', 'bounce', and 'sway'."
    show man:
        parallel:
            walkloop
        parallel:
            loopfromleft
    "Pairing this with loopfromleft or loopfromright, either on the sprite itself or on the background, can give great results."

    jump start

label jumps:
    show man:
        full
        center
        block:
            jump
            pause 2
            repeat
    "The jump animation has a short windup, then a jump. You can adjust its 'windup', 'power', and 'airtime'."
    show man:
        full
        leftish
        block:
            toright
            leapto(rightish)
            pause 2
            toleft
            leapto(leftish)
            pause 2
            repeat
    "The leapto animation takes a sprite from anywhere on screen, and makes it leap to any 'location'. You can adjust its 'windup', 'power', and 'airtime', too."
    jump start

label leaf:
    show leafpaper:
        fallingleaf
        2
        repeat
    "By default, the item falls from the center of the screen (0.5,0.5). To define another location, adjust its 'startpos' with a tuple."
    jump start

label pickup:
    show woman:
        medlong
        leftish
        toright
    show man:
        medlong
        centerright
        toleft
    "Pickup is an animation in two parts―one for the character, and one for the item."
    show woman:
        pickup
        2
        repeat
    show leafpaper:
        itempickup((0.3,0.6))
        2
        repeat
    show man:
        pickup
        2
        repeat
    show leafpaper as paper2:
        itempickup
        2
        repeat
    "By default, the item goes to the center of the screen (0.5,0.5). To define another location, adjust its 'location' with a tuple. You can also adjust the 'depth' the character must crouch to pick it up."
    jump start

label looparound:
    show man:
        full
        toright
        loopfromleft
    "A man walks from left to right, then waits a moment and comes back around."
    show man:
        loopfromleft(2,3)
    "You can adjust the timings to make him run instead, and wait a different amount of time between loops."
    show woman:
        full
        toleft
        loopfromright
    "There is also a right to left version."
    show text "This can be applied to any displayable, including text, which can be used to make a news scroll type feature.":
        loopfromright(20, 21)
    show text "You can even stagger different lines of text by changing the initial delay." as text2:
        ypos 0.6
        loopfromright(20, 21, 10)
    show text "Scroll speed will differ based on width." as text3:
        ypos 0.7
        loopfromright(20, 21, 20)

    hide man
    hide woman
    "* Text as a displayable is separate from the usual textbox, and will not show up in text history."
    jump start

label zoomies:
    show woman:
        full
        center
        zoomies
    show man:
        full
        center
    show womanbouncing_front:
        full
        center
        zoomies
    "By default, zoomies are set to a rate of 0.2. You can set the variable 'zoomies_rate' if you want something a little less (or a little more?) chaotic."
    jump start

label vibrate:
    show man:
        full
        center
        vibrate
    "By default, vibrating is quite mild."
    show man:
        alpha 0.2
        vibrate(10)
    "But you can increase it. Be very careful with this, as fast movements with high contrast could trigger seizures."
    jump start

label flicker:
    show man:
        medclose
        center
        flicker
    "The flicker animation has some randomness to it. You can adjust its 'rate', 'min' transparency, and 'max' transparency."
    "Be very careful with this, as flickering lights could trigger seizures. Especially avoid any flicker rates that happen approximately 3 times per second. (rate=0.2-0.4)"
    jump start

label ballroom_dancing:
    show man:
        center
        medlong
    show woman:
        center
        medlong
    "To start a ballroom dance, place both dancers at center stage with a medium long shot; lead first, then follower."
    show mandancing_back:
        center
        medlong
    "Then place a fluctuating duplicate of the lead dancer's back sprite, as outlined in the image definitions."
    show man dancing at waltz_lead
    show woman dancing at waltz_follow
    show mandancing_back at waltz_lead
    "Then set them all dancing. It is crucial that you do everything without interruption, or they will desynchronize and it will be very obvious that there is a duplicate."
    hide man
    hide woman
    hide mandancing_back
    show man:
        center
        medlong
    show woman:
        center
        medlong
    show mandancing_back:
        center
        medlong
    show man dancing at waltz_lead
    show woman dancing at waltz_follow
    show mandancing_back at waltz_lead

    "When done correctly, the two characters should seamlessly dance around each other."

    jump start
    # This ends the game.

label seesaw:
    show man:
        seesaw_left
    show woman at seesaw_right
    "By default, the seesaw is set to a rate of 3, and a vertical offset of 0. You can set the variables 'seesaw_rate' and 'seesaw_height' if you've got a pair of exhuberent kids to keep in frame."
    jump start




return
