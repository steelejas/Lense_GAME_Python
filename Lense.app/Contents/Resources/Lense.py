import pygame
from classes import *
from constructors import *


pygame.init()
pygame.display.set_caption("Final Project")
done = False


def check_ordered_events(mode, player_loc, player_box, other_box, current_map, spritelist):
    #print("checking ordered events...")
    if len(mode.ordered_events) > 0:
        event = mode.ordered_events[0]

        if event.trigger_map == current_map and event.trigger_range[0] <= player_loc <= event.trigger_range[1]:
            current_map = start_ordered_event(mode, event, player_box, other_box, current_map, spritelist)
    
    return current_map


def check_running_events(mode, player_loc, player_box, other_box, current_map, spritelist, notifier):
    #print("checking running events...")

    notifier.show = False
    
    for i in range(len(mode.running_events)):

        event = mode.running_events[i]
        

        if event.trigger_map == current_map and event.trigger_range[0] <= player_loc <= event.trigger_range[1]:
            
            event_center = (event.trigger_range[0] + event.trigger_range[1]) //2
            notifier.go_to(event_center, 200)
            notifier.show = True
            #draw_scene(current_map, spritelist)
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_x]:
                start_running_event(mode, event, player_box, other_box, current_map, spritelist)

    return current_map


def start_ordered_event(mode, event, player_box, other_box, current_map, spritelist):
    
    #completed = False

    #print("ordered event:", event.name)
    #text(["x"], player_box)
    if mode == mode0:
        if event.name == "map1 to map2":
            if e_invitation in mode.running_events_incomplete:
                text(["(I should check the mail first.)"], player_box)
                player.rect.centerx -= 10
                return current_map
            else:
                current_map = map2
                player.go_to(10, 300)
                invitation.show = False
        elif event.name == "city thoughts 1":
            text(["I wonder if I'll see anyone I know!"], player_box)
        elif event.name == "map2 to map3":
            current_map = map3
            player.go_to(10, 270)
            chara1.show = True
            chara2.show = True
            chara3.show = True
        elif event.name == "party greeting":
            text(["Hey, Alex! Glad you were able", "to come!"], other_box)
            text(["Me too! Thanks for the invite.", "And happy birthday!"], player_box)
            text(["Haha, thanks! Hey, you can finally", "meet my friends! I've told them", "a lot about you."], other_box)
            text(["(Oh! I should go talk to them!)"], player_box)
            text(["Awesome! I'll go say hi."], player_box)
        elif event.name == "map3 to map4":
            if e_party_convo in mode.running_events_incomplete:
                text(["Wait, Alex!," "Have you talked to my friends yet?", "They were looking forward to meeting you."], other_box)
                text(["(I should at least say hi", "before I leave.)"], other_box)
                player.rect.centerx += 10
                return current_map
            else:
                text(["Bye, Alex!"], other_box)
                text(["Bye, Amanda! Happy birthday!"], player_box)
                current_map = map4
                player.go_to(590, 300)
                chara1.show = False
                chara2.show = False
                chara3.show = False
        elif event.name == "city thoughts 2":
            text(["(That was fun. It's always nice", "seeing Amanda. And her friends", "were pretty cool!)"], player_box)
            text(["(Maybe we could all hang out again", "sometime.)"], player_box)
        elif event.name == "map4 to map5":
            current_map = map5
            player.go_to(500, 300)
            invitation.show = True
        elif event.name == "end":
            text(["(Time for bed...)"], player_box)
            current_map = "next"

    elif mode == mode1:
        if event.name == "map1 to map2":
            if e_invitation in mode.running_events_incomplete:
                text(["(I should check the mail first.)"], player_box)
                player.rect.centerx -= 10
                return current_map
            else:
                current_map = map2
                player.go_to(10, 300)
                invitation.show = False
        elif event.name == "city thoughts 1":
            text(["(It's kind of cold out here. Am I wearing", "the right thing?)"], player_box)
            text(["(But what if it's cold in her house?)"], player_box)
        elif event.name == "city thoughts 2":
            text(["(What if her friends don't like me?)"], player_box)
        elif event.name == "city thoughts 3":
            text(["(I bet they've known each other for a", "long time. I probably won't fit in.)"], player_box)
        elif event.name == "city thoughts 4":
            text(["(What would I even talk about with them?)"], player_box)
        #elif event.name == "city thoughts 5":
            #text(["(thoughts"], player_box)
            #text(["(more thoughts)"], player_box)
        elif event.name == "map2 to map3":
            current_map = map3
            player.go_to(10, 270)
            chara1.show = True
            chara2.show = True
            chara3.show = True
        elif event.name == "party greeting":
            text(["(There are so many people here...)"], player_box)
            text(["Hey, Alex! Glad you were able", "to come!"], other_box)
            text(["(Does she mean that?", "It's not like we talk often.", "She probably invited me", "out of obligation.)"], player_box)
            text(["Me too! Thanks for the invite.", "And happy birthday!"], player_box)
            text(["(Wait, she's 'glad I could come'?", "Did she think I would skip out?", "Is that my reputation?)"], player_box)
            text(["Haha, thanks! Hey, you can finally", "meet my friends! I've told them", "a lot about you."], other_box)
            flash(redflash, current_map, spritelist)
            text(["(What? What has she told them?)"], player_box)
            #text(["(thoughts)"], player_box)
            text(["Awesome! I'll go say hi."], player_box)
            text(["(Do they even want to meet me?)"], player_box)
        elif event.name == "map3 to map4":
            if e_party_convo in mode.running_events_incomplete:
                text(["Wait, Alex!," "Have you talked to my friends yet?", "They were looking forward to meeting you."], other_box)
                flash(redflash, current_map, spritelist)
                text(["(Ack! What am I doing?"], player_box)
                text(["It looks rude for me to leave now.", "She invited me, I have to at least", "stay a little while."], player_box)
                player.rect.centerx += 10
                return current_map
            else:
                text(["Bye, Alex!"], other_box)
                text(["Bye, Amanda! Happy birthday!"], player_box)
                current_map = map4
                player.go_to(590, 300)
                chara1.show = False
                chara2.show = False
                chara3.show = False
        elif event.name == "city thoughts 6":
            text(["(Ugh. Did I leave too soon? I'm being", "so rude, aren't I.", "I bet she hates me now.)"], player_box)
        elif event.name == "city thoughts 7":
            text(["(Her friends probably thought I was so", "weird.)"], player_box)
        elif event.name == "city thoughts 8":
            text(["(Amanda didn't mention her gift when I", "left! She didn't like it. Ugh, I knew I", "picked the wrong thing.)"], player_box)
        elif event.name == "map4 to map5":
            current_map = map5
            player.go_to(570, 300)
            invitation.show = True
        elif event.name == "room thoughts 1":
            text(["(I hope I didn't bother anyone at", "her party.)"], player_box)
        elif event.name == "room thoughts 2":
            text(["(Ugh, I bet she thinks I'm a", "bad friend.)"], player_box)
        elif event.name == "end":
            #print("hey")
            text(["(Time for bed...)"], player_box)
            current_map = "next"
        

    mode.ordered_events.pop(0)
    return current_map


def start_running_event(mode, event, player_box, other_box, current_map, spritelist):
    
    #completed = False

    #print("running event:", event.name)
    if mode == mode0:
        if event.name == "invitation":
            splash_screen(invitationscreen)
            text(["(It's an invitation!)"], player_box)
            text(['"Today’s my 19th birthday, and you’re', 'invited! The party will take place at', 'my house in approximately 2 minutes."'], other_box)
            text(['"See you there, neighbor!', '', '--Amanda"'], other_box)
            text(["(Wow! She’s 19 already? It’s been", "awhile since I’ve seen her. I can’t", "wait to catch up!)"], player_box)
            text(["(Maybe I can finally meet those", "friends that she always talked about.)"], player_box)
            text(["(I should probably bring a gift, huh?", "I don’t know what she wants, but gift", "cards are always appreciated, right?)"], player_box)
            text(["(Oh, it’s starting soon!", "", "I better head over now.)"], player_box)
        if event.name == "party convo":
            text(["Hi! I'm Alex, Amanda's neighbor.", "What are you guys up to?"], player_box)
            #text(["x"], player_box)
            text(["We were just talking about our", "favorite PIXAR movies."], other_box)
            text(["I'm a huge Finding Nemo fan,", "Kristi likes Inside Out,", "and Rhea LOVES Monsters Inc.!"], other_box)
            text(["What about you?"], other_box)
            text(["Toy Story has always had a", "special place in my heart."], player_box)

    elif mode == mode1:
        if event.name == "invitation":
            splash_screen(invitationscreen)
            text(["(It's an invitation!)"], player_box)
            text(['"Today’s my 19th birthday, and you’re', 'invited! The party will take place at', 'my house in approximately 2 minutes."'], other_box)
            text(['"See you there, neighbor!', '', '--Amanda"'], other_box)
            text(["(It's her birthday already?)"], player_box)
            text(["(Do I have to go?", "I probably won't know anyone there.", "It'll just be awkward.)"], player_box)
            text(["(I have to bring a gift, too, don't I?", "But I don't know what she wants!", "What if she doesn't like my gift?"], player_box)
            text(["(Maybe I just shouldn't go...)"], player_box)
            text(["(No, I should go.", "She'll think I'm really rude if I just", "ignore her invitation.)"], player_box)
        if event.name == "party convo":
            text(["Hi! I'm Alex, Amanda's neighbor.", "What are you guys up to?"], player_box)
            #text(["x"], player_box)
            flash(redflash, current_map, spritelist)
            text(["(Was that too forward?", "I don't know them.", "Do they think I'm being creepy?)"], player_box)
            text(["We were just talking about our", "favorite PIXAR movies."], other_box)
            flash(redflash, current_map, spritelist)
            text(["(Oh no, did I barge into their", "conversation?", "That sounded curt, didn't it? Are they", "annoyed? They must think I'm so rude.)"], player_box)
            text(["I'm a huge Finding Nemo fan..."], other_box)
            flash(redflash, current_map, spritelist)
            text(["(My legs keeps shaking.", "God, why won’t it stop?)"], player_box)
            text(["...Kristi likes Inside Out..."], other_box)
            flash(redflash, current_map, spritelist)
            text(["(Amanda isn’t even talking to me.", "I shouldn't have even come.)"], player_box)
            text(["...and Rhea LOVES Monsters Inc.!"], other_box)
            flash(redflash, current_map, spritelist)
            text(["(Ugh, my hands are all sweaty.", "Can they tell?)"], player_box)
            text(["What about you?"], other_box)
            flash(redflash, current_map, spritelist)
            text(["(What? Ack, they asked me a question!)"], player_box)
            text(["Toy Story has always had a", "special place in my heart."], player_box)
            flash(redflash, current_map, spritelist)
            text(["(Was that an OK answer?", "I worded that weirdly, didn't I.)"], player_box)
            flash(redflash, current_map, spritelist)
            text(["(Is it weird to like Toy Story?", "Are they judging me?)"], player_box)
            flash(redflash, current_map, spritelist)
            text(["(Is that a disapproving look?", "They're all staring at me.)"], player_box)
            text(["(Ugh, I should leave.", "I'm embarrassing myself.", "This was a terrible idea.)"], player_box)
    
    if event in mode.running_events_incomplete:
        event_index = mode.running_events_incomplete.index(event)
        mode.running_events_incomplete.pop(event_index)
    return current_map
                



def text(text, box):
    box.show = True
    box.text = text
    box.update()
    pygame.display.update()
    wait()
    box.show = False
    pygame.time.delay(100)


def wait():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                waiting = False
    #print("pressed")
    return


def splash_screen(screen):
    screen.show = True
    screen.draw()
    pygame.display.update()
    wait()
    screen.show = False

def flash(flashimage, current_map, spritelist):
    for i in range(2):
        flashimage.show = True
        draw_scene(current_map, spritelist)
        pygame.time.delay(100)
        flashimage.show = False
        draw_scene(current_map, spritelist)
        pygame.time.delay(100)




def draw_scene(current_map, spritelist):
    screen.fill([255, 255, 255])
    ## clear screen
    current_map.draw()
    ## draw all shown sprites
    for i in range(len(spritelist)):
        spritelist[i].draw()
    ## update screen
    pygame.display.flip()

def end_game(endscreen):
    splash_screen(endscreen)


def gameloop(mode, maplist, spritelist, current_map):

    player_loc = player.rect.centerx #current x location of player
    playerflip.go_to(player_loc, player.rect.bottom)

    
    ## get arrow key presses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and player_loc <= SCREEN_WIDTH - 50:
        playerflip.show = False
        player.show = True
        move = 5
        player.next_frame()
    elif pressed[pygame.K_LEFT] and player_loc >= 0:
        move = -5
        playerflip.show = True
        player.show = False
        playerflip.next_frame()
    else:
        player.frame = 0
        move = 0
    

    ## move (player or map, depending on if it's a scrolling map)
    if current_map.scrolling:
        current_map.rect.x -= move
    else:
        player.rect.x += move
        playerflip.rect.x += move
    move = 0

    

    ## check for events        
    check_running_events(mode, player_loc, player_box, other_box, current_map, spritelist, notifier)
    current_map = check_ordered_events(mode, player_loc, player_box, other_box, current_map, spritelist)
    
    if current_map is not "next":
        draw_scene(current_map, spritelist)

    return current_map

##**** SETUP ****##

splash_screen(startscreen)
splash_screen(instructionscreen)

mode = mode0
current_map = map1
move = 0

draw_scene(current_map, spritelist)

##**** GAME LOOP ****##

while not done:

    ## event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    current_map = gameloop(mode, maplist, spritelist, current_map)

    if current_map == "next":
        #print(current_map)
        nextmode_index = modelist.index(mode) + 1
        if nextmode_index == len(modelist):
            #end_game(spritelist)
            splash_screen(endscreen)
            done = True
        else:
            splash_screen(continuescreen)
            mode = modelist[nextmode_index]
            current_map = map1
            invitation.show = True

    ## limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE