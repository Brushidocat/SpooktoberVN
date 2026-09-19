## Make some investigations screen. Will need to make a custom one for each crimescene/

screen mainhall():
    imagemap: 
        ground "images/mainhall.jpg" at parallax_shift(z_pos = 0.6,sprite = False)
        ##hotspot (9, 650, 634, 402) 
        ## action Jump("house") tooltip "My house! (Not really)" hovered ShowTransient("the_img", img="investigations1_hover1.png") unhovered Hide("the_img")
        ##Chest 
        ##hotspot (9, 650, 634, 402) 
        ## action Jump("chest") tooltip "A large, conspicuous chest." hovered ShowTransient("the_img", img="investigations1_hover1.png") unhovered Hide("the_img")
        ## Paintings
        ## Gargoyle 
        ## Door 
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" xalign 0.5 yalign 0.5

screen the_img(img): 
    add img at parallax_shift(z_pos = 0.6,sprite = False)
  
##TODO: Make a small framed image, should be modular. 

screen hallway(): 
    imagemap: 
        ground "images/mainhall.jpg" at parallax_shift(z_pos=0.6, sprite = False)
        ## Drawer 
        ## Sun box 
        ## Moon Box 
        ## Staff Door 
        ## Bookcase 
        ## Gem Case 


screen ballroom():
    imagemap:
        ground "images/mainhall.jpg" at parallax_shift(z_pos=0.6, sprite = False)
        ##Piano 
        ##banquettable 
        ##shoutyman 

screen addFrame(img):
    zorder 100 
    dismiss action Return()
    frame: 
        modal True 
        add img 