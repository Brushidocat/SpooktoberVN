## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("The Mansion of Count Blud")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""

Audio: 
Through the Eyes of the Doll - Clement Panchout  https://clement-panchout.itch.io/
Monster Musuem - Clement Panchout https://clement-panchout.itch.io/ 
Danger - Clement Panchout https://clement-panchout.itch.io/
Shenanigans -  https://fulminisictus.itch.io/
Time to Rest - https://fulminisictus.itch.io/
Swinging That Electro- https://fulminisictus.itch.io/
GOTHIC VISUAL NOVEL SOUNDS - https://rohhsa.itch.io/ (500 Ui sounds what the fu-) 
Haunted Hijinks - Melancholy Marionette, https://melancholy-marionette.itch.io/love-terror-bgm-pack-vol-02, https://melancholy-marionette.itch.io/

Backgrounds: 
"Shopping Backgrounds" by Unicorn Creates (https://unicorncreates.itch.io/) licensed under CC BY 4.0 (http://creativecommons.org/licenses/by/4.0/)
"Regal Hallway" by Knickknack PJ (https://knickknackpj.itch.io/)
Tools: 
Kinetic Text Tags by Daniel Westfall <SoDaRa2595@gmail.com> -https://wattson.itch.io/
RWParallax by Rythen Winds — https://rythen-winds.itch.io/
Fonts: 
Copyright (c) 2011 by Sorkin Type Co (www.sorkintype.com),
with Reserved Font Name "Rye".
Copyright (c) 2010, ParaType Ltd. (http://www.paratype.com/public),
with Reserved Font Names "PT Sans", "PT Serif" and "ParaType".

The {a=https://ayperosia.itch.io/dark-fantasy-ui}Dark Fantasy GUI Kit{/a} is a Ren'Py code template/base project featuring a pre-implemented graphical user interface created by {a=https://bsky.app/profile/ayperosia.bsky.social}Charlie{/a} ({a=https://ayperosia.itch.io/}@ayperosia{/a}).
This kit, alongside others including their {a=https://itch.io/c/5494761/gui-packs-prideful-collection}Prideful Collection kits{/a}, are available for purchase over on {a=https://vgen.co/ayperosia}vgen{/a} and {a=https://ayperosia.itch.io/}itch.io{/a}. 
Or, if something already available does not quite fit your next project, you can {a=https://vgen.co/ayperosia/service/visual-novel-user-interface-gui-design-/553e7a80-1b45-4f7c-b9d9-b510ededb019}order custom GUI via commissions on vgen{/a}, alongside other services like title logo design and game page customisation.

""") ### Hi! Charlie here, please do not remove the text on lines 34-35 about the UI kit,
## it is required to remain (or be copied over to your new project) by the license 
## that you agreed to when purchasing this GUI kit!


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "DarkFantasyGUIKitbyayperosia"


## Sounds and music ############################################################

## These three variables control, among other things, which mixers are shown
## to the player by default. Setting one of these to False will hide the
## appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any
## other number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "DarkFantasyGUIKitbyayperosia-1754665009"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory,
    ## "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to perform in-app purchases. It can be
## found in the Google Play developer console, under "Monetize" > "Monetization
## Setup" > "Licensing".

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
