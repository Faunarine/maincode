# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Define each characters colour by their hair colour once designs are finished.

image namebg = im.Scale("name_bg.png", 1920, 1080)
image house = im.Scale("house.jpeg", 1920, 1080)
image CelWorkD = im.Scale("CelesteWorkDay.png", 1920, 1080)
image CelWorkDA = im.Scale("CelesteWorkDayApproach.png", 1920, 1080)
image CelWorkDM = Movie(play="CelesteWorkDayMainLoop.webm", loops=-1)
image CelWorkDST = im.Scale("CelesteWorkDayMainSpendTime.png", 1920, 1080)
image CelWorkDT = im.Scale("CelesteWorkDayMainTalk.png", 1920, 1080)
image CelWorkE = im.Scale("CelesteWorkEvening.png", 1920, 1080)
image CelWorkEA1 = im.Scale("CelesteWorkEveningApproach1.png", 1920, 1080)
image CelWorkEA2 = im.Scale("CelesteWorkEveningApproach2.png", 1920, 1080)
image CelWorkEA3 = im.Scale("CelesteWorkEveningApproach3.png", 1920, 1080)
image CelWorkEM = Movie(play="CelesteWorkEveningMainLoop.webm", loops=-1)
image CelWorkEST = im.Scale("CelesteWorkEveningMainSpendTime.png", 1920, 1080)
image CelWorkET = im.Scale("CelesteWorkEveningMainTalk.png", 1920, 1080)
# The game starts here.

label start:
scene namebg
$ mc = renpy.input("{i}What is your name?")
$ mc = mc.strip()

"{i}Your name is [mc].
Are you sure? This cannot be changed later."
menu:
    "Yes":
        jump prologue
    "No":
        jump start

return

label prologue:
hide namebg
scene house
with fade
mc "Well, this is it I guess."
mc "This is where I will be living for the foreseeable future."
"{i}My name is [mc]."

jump CelWorkDay

label CelWorkDay:
scene CelWorkD
call screen CelWorkDBut
pause

screen CelWorkDBut:
    imagebutton:
        xpos 447
        ypos 397
        idle "CelWorkButtonDay_idle.png"
        hover "CelWorkButtonDay_hover.png"
        action Jump("CelWorkD1")

label CelWorkD1:
show CelWorkDA
with fade
hide CelWorkD
mc "Hey."
jump CelWorkDMenu
label CelWorkDMenu:
show CelWorkDM
with dissolve
cel "Oh, [mc]! How are you?"
menu:
    "Spend Time":
        jump CelWorkDST
    "Talk":
        jump CelWorkDT
    "Nevermind.":
        jump CelWorkDN

return

label CelWorkDST:

mc "Need someone to keep you company?"
hide CelWorkDM
show CelWorkDST
with dissolve
cel "Sure! I don't have anything better to do anyway."
jump CelWorkEve

label CelWorkDT:
mc "Don't you get bored working here?"
hide CelWorkDM
show CelWorkDT
with dissolve
cel "Yeah, I guess. I don't mind it though..."
mc "Well, let me know if you need anything."
hide CelWorkDT
show CelWorkDST
with dissolve
cel "Sure."
jump CelWorkDay

label CelWorkDN:

mc "Actually, I should go."
cel "See you later, then."
jump CelWorkDay



label CelWorkEve:
scene CelWorkE
call screen CelWorkEBut
pause

screen CelWorkEBut:
    imagebutton:
        xpos 1233
        ypos 697
        idle "CelWorkButtonEve_idle.png"
        hover "CelWorkButtonEve_hover.png"
        action Jump("CelWorkE1")

label CelWorkE1:
show CelWorkEA1
with dissolve
pause
show CelWorkEA2
with dissolve
pause
mc "Hey, Celeste."
show CelWorkEA3
with dissolve
cel "Hi."
jump CelWorkEMenu
label CelWorkEMenu:
show CelWorkEM
with dissolve
cel "What's up?"
menu:
    "Spend Time":
        jump CelWorkEST
    "Talk":
        jump CelWorkET
    "Nevermind.":
        jump CelWorkEN
return

label CelWorkEST:
mc "Need any help around here?"
show CelWorkEST
with dissolve
cel "Yes, please! I could use some company as well."
mc "Sure."
return

label CelWorkET:
mc "What are you doing?"
show CelWorkET
with dissolve
cel "Just checking stock before I close."
mc "Alright."
jump CelWorkEve

label CelWorkEN:
mc "Just looking around."
cel "No worries."
jump CelWorkEve
return
