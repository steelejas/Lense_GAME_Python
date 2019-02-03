from classes import *
#from finalproject_classes import Event
#from finalproject_classes import SCREEN_WIDTH, SCREEN_HEIGHT



##**** SPRITE SETUP ****##

def load(file):
	file = "resources/" + file
	image = pygame.image.load(file)
	return image

spritelist = []

## player

player_image = [load("alex1.png"), load("alex1.png"), load("alex1.png"), load("alex2.png"), load("alex2.png"), load("alex2.png"), load("alex3.png"), load("alex3.png"), load("alex3.png"), load("alex2.png"), load("alex2.png"), load("alex2.png")]
player = Sprite(player_image, (50, 300), True)

playerflip_image = [load("alex1FLIP.png"), load("alex1FLIP.png"), load("alex1FLIP.png"), load("alex2FLIP.png"), load("alex2FLIP.png"), load("alex2FLIP.png"), load("alex3FLIP.png"), load("alex3FLIP.png"), load("alex3FLIP.png"), load("alex2FLIP.png"), load("alex2FLIP.png"), load("alex2FLIP.png")]
playerflip = Sprite(playerflip_image, (50, 300))

## other sprites

invitation_image = [load("envelope.png")]
invitation = Sprite(invitation_image, (348, 280), True)
spritelist.append(invitation)

notifier_image = [load("notif.png")]
notifier = Sprite(notifier_image, (0, 0))
spritelist.append(notifier)

chara1_image = [load("girl.png")]
chara1 = Sprite(chara1_image, (100, 260))
spritelist.append(chara1)

chara2_image = [load("palmtree.png")]
chara2 = Sprite(chara2_image, (340, 250))
spritelist.append(chara2)

chara3_image = [load("theone.png")]
chara3 = Sprite(chara3_image, (440, 260))
spritelist.append(chara3)

## text boxes

player_box_image = [load("purpletext.png")]
other_box_image = [load("yellowtext.png")]
player_box = TextBox(player_box_image, (0, 0), False, WHITE)
other_box = TextBox(other_box_image, (0, 0), False, WHITE)
spritelist.append(player_box)
spritelist.append(other_box)

## splash screens -- DO NOT APPEND

startscreen_image = [load("startscreen.png")]
startscreen = Sprite(startscreen_image, (5, 10), True)
spritelist.append(startscreen)

instructionscreen_image = [load("instructions.png")]
instructionscreen = Sprite(instructionscreen_image, (5, 10))
spritelist.append(instructionscreen)

invitationscreen_image = [load("invitation.png")]
invitationscreen = Sprite(invitationscreen_image, (5, 30))
spritelist.append(invitationscreen)

continuescreen_image = [load("continue.png")]
continuescreen = Sprite(continuescreen_image, (5, 10))
spritelist.append(continuescreen)

endscreen_image = [load("anxiety-end.png")]
endscreen = Sprite(endscreen_image, (5, 10))
spritelist.append(endscreen)

redflash_image = [load("flashes.png"), load("flashes.png"), load("flashes2.png"), load("flashes2.png"), load("flashes3.png"), load("flashes3.png"), load("flashes2.png"), load("flashes2.png"), load("flashes.png"), load("flashes.png"),]
redflash = Sprite(redflash_image, (5, 10))


spritelist.append(player) #this has to go last so they'll be drawn last and be in front of everything else!!
spritelist.append(playerflip)
spritelist.append(redflash)



##**** MAP SETUP ****##

map1_image = load("room.png")
map2_image = load("city.png")
map3_image = load("party.png")
map4_image = load("city.png")
map5_image = load("room.png")
map1 = Map(map1_image, False)
map2 = Map(map2_image, False)
map3 = Map(map3_image, False)
map4 = Map(map4_image, False)
map5 = Map(map5_image, False)

maplist = []
maplist.append(map1)
maplist.append(map2)
maplist.append(map3)
maplist.append(map4)
maplist.append(map5)



##**** EVENT SETUP ****##

''' 
Event attributes:
name
trigger_map -- which map does it happen on?
trigger_range -- within what space the player stand to trigger it? (tuple of x coordinates)

ORDERED EVENTS must be triggered in order, and can only be triggered once
RUNNING EVENTS can be triggered in any order, an unlimited number of times
'''


## MODE 0 EVENTS

## init ordered events
#event_o0a = Event("invitation", map1, (345, 351))
e_door1 = Event("map1 to map2", map1, (500, 510))
e_city_thoughts_1 = Event("city thoughts 1", map2, (397, 403))
e_door2 = Event("map2 to map3", map2, (540, 600))
e_party_greeting = Event("party greeting", map3, (40, 50))
e_door3 = Event("map3 to map4", map3, (0, 10))
e_city_thoughts_2 = Event("city thoughts 2", map4, (500, 506))
e_door4 = Event("map4 to map5", map4, (0, 10))
e_end = Event("end", map5, (0, 60))


## append ordered events
mode0_ordered_events = []
mode0_ordered_events.append(e_door1)
mode0_ordered_events.append(e_city_thoughts_1)
mode0_ordered_events.append(e_door2)
mode0_ordered_events.append(e_party_greeting)
mode0_ordered_events.append(e_door3)
mode0_ordered_events.append(e_city_thoughts_2)
mode0_ordered_events.append(e_door4)
mode0_ordered_events.append(e_end)

## init running events
e_invitation = Event("invitation", map1, (340, 356))
e_party_convo = Event("party convo", map3, (260, 560))

## append running events
mode0_running_events = []
mode0_running_events.append(e_invitation)
mode0_running_events.append(e_party_convo)

mode0_running_events_incomplete = []
for i in range(len(mode0_running_events)):
	mode0_running_events_incomplete.append(mode0_running_events[i])



## MODE 1 EVENTS

## init ordered events
e_city_thoughts_1_1 = Event("city thoughts 1", map2, (80, 86))
e_city_thoughts_2_1 = Event("city thoughts 2", map2, (160, 166))
e_city_thoughts_3 = Event("city thoughts 3", map2, (240, 246))
e_city_thoughts_4 = Event("city thoughts 4", map2, (320, 326))
e_city_thoughts_5 = Event("city thoughts 5", map2, (400, 406))
e_city_thoughts_6 = Event("city thoughts 6", map4, (400, 406))
e_city_thoughts_7 = Event("city thoughts 7", map4, (240, 246))
e_city_thoughts_8 = Event("city thoughts 8", map4, (80, 86))
e_room_thoughts_1 = Event("room thoughts 1", map5, (300, 306))
e_room_thoughts_2 = Event("room thoughts 2", map5, (150, 156))

## append ordered events
mode1_ordered_events = []
mode1_ordered_events.append(e_door1)
mode1_ordered_events.append(e_city_thoughts_1_1)
mode1_ordered_events.append(e_city_thoughts_2_1)
mode1_ordered_events.append(e_city_thoughts_3)
mode1_ordered_events.append(e_city_thoughts_4)
mode1_ordered_events.append(e_city_thoughts_5)
mode1_ordered_events.append(e_door2)
mode1_ordered_events.append(e_party_greeting)
mode1_ordered_events.append(e_door3)
mode1_ordered_events.append(e_city_thoughts_6)
mode1_ordered_events.append(e_city_thoughts_7)
mode1_ordered_events.append(e_city_thoughts_8)
mode1_ordered_events.append(e_door4)
mode1_ordered_events.append(e_room_thoughts_1)
mode1_ordered_events.append(e_room_thoughts_2)
mode1_ordered_events.append(e_end)

## init running events
# (((they're all in the same locations as in mode0)))

## append running events
mode1_running_events = []
mode1_running_events.append(e_invitation)
mode1_running_events.append(e_party_convo)

mode1_running_events_incomplete = []
for i in range(len(mode1_running_events)):
	mode1_running_events_incomplete.append(mode1_running_events[i])



##**** MODE SETUP ****##

mode0 = Mode("none", mode0_ordered_events, mode0_running_events, mode0_running_events_incomplete)
mode1 = Mode("social anxiety", mode1_ordered_events, mode1_running_events, mode1_running_events_incomplete)

modelist = []
modelist.append(mode0)
modelist.append(mode1)
