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
        if mainhallfinished: 
            hotspot (1176, 212, 455, 442) action Jump("hallway") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_door.png") unhovered Hide("the_img")
        else:
            hotspot (11, 203, 402, 642) action Jump("Megan") hovered ShowTransient("the_img", img="mainhall/mhs/mhs_megan.png")unhovered Hide("the_img")
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
        hotspot (270, 553, 339, 501) action Jump("drawer") hovered ShowTransient("the_img", img="hallway/hws/hws_drawer.png")unhovered Hide("the_img")
        hotspot (1136, 13, 451, 1048) action Jump("bookcase") hovered ShowTransient("the_img", img="hallway/hws/hws_bookshelf.png") unhovered Hide("the_img")
        ## Gem Case 
        hotspot (1709, 4, 209, 1075) action Jump("gemcase") hovered ShowTransient("the_img", img="hallway/hws/hws_gemcase.png") unhovered Hide("the_img")
        ## door 
        hotspot (295, 331, 401, 381) action Jump("hallwaydoors") hovered ShowTransient("the_img", img = "hallway/hws/hws_brd.png") unhovered Hide("the_img")
        hotspot (871, 259, 147, 250) action Jump("mirror") hovered ShowTransient("the_img", img="hallway/hws/hws_mirror.png") unhovered Hide("the_img")
        hotspot (0, 0, 268, 1072) action Jump("mainhall") hovered ShowTransient("the_img", img="hallway/hws/hws_mhd.png") unhovered Hide("the_img")



screen ballroom():
    imagemap:
        ground "images/ballroom/ballroom.png" at parallax_shift(z_pos=0.6, sprite = False)
        hotspot (14, 431, 476, 323) action jump("piano") hovered ShowTransient("the_img", img="ballroom/brs/brs_piano.png") unhovered Hide("the_img")
        hotspot (772, 406, 457, 282) action jump("banquetTable") hovered ShowTransient("the_img", img="ballroom/brs/brs_bt.png") unhovered Hide("the_img")
        hotspot (1654, 331, 210, 544) action jump("coffin") hovered ShowTransient("the_img", img="ballroom/brs/brs_coffin.pmg") unhovered Hide("the_img")
        ##Piano 
        ##banquettable 
        ##shoutyman 

screen addFrame(img):
    zorder 100 
    dismiss action Return()
    frame: 
        modal True 
        add img 