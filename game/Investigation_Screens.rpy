## Make some investigations screen. Will need to make a custom one for each crimescene/
default mainhall = "images/mainhall/mainhall.png"

screen mainhall():
    imagemap: 
        ground mainhall at parallax_shift(z_pos = 0.6,sprite = False)
        ##hotspot (9, 650, 634, 402) 
        ## action Jump("house") tooltip "My house! (Not really)" hovered ShowTransient("the_img", img="investigations1_hover1.png") unhovered Hide("the_img")
        
        ##hotspot (9, 650, 634, 402) 
        ## action Jump("chest") tooltip "A large, conspicuous chest." hovered ShowTransient("the_img", img="investigations1_hover1.png") unhovered Hide("the_img")
        ## Paintings
        hotspot (196, 196, 777, 295) action Jump("paintings") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_painting.png")unhovered Hide("the_img")
        
        ## Door 
        hotspot (1176, 212, 455, 442) action Jump("mainhall_Doors") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_door.png") unhovered Hide("the_img")

        ##Chest 
        hotspot (404, 552, 229, 138) action Jump("chest") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_chest.png") unhovered Hide("the_img")
        ## Gargoyle 
        hotspot (976, 268, 134, 351) action Jump("gargoyle") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_gargoyle.png") unhovered Hide("the_img")

        #table
        hotspot (643, 593, 935, 471) action Jump("table") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_table.png") unhovered Hide("the_img")
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" xalign 0.5 yalign 0.5

screen the_img(img): 
    add img at parallax_shift(z_pos = 0.6,sprite = False)
  
##TODO: Make a small framed image, should be modular. 

screen hallway(): 
    imagemap: 
        ground "images/hallway/hallway.png" at parallax_shift(z_pos=0.6, sprite = False)
        ## Drawer 
        ## Sun box 
        ## Moon Box 
        ## Staff Door 
        ## Bookcase 
        ## Gem Case 


screen ballroom():
    imagemap:
        ground "images/ballroom/ballroom.png" at parallax_shift(z_pos=0.6, sprite = False)
        ##Piano 
        ##banquettable 
        ##shoutyman 

screen addFrame(img):
    zorder 100 
    dismiss action Return()
    frame: 
        modal True 
        add img 