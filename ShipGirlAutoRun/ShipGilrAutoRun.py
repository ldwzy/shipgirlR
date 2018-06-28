import cv2
import numpy
from PIL import ImageGrab
import time
from enum import Enum
import frame_estimate
from AutoClick import auto_input

'''simple for the code
########################################################
#ai = auto_input()
#ai.mouse_click(1380, 350)
#main_img = cv2.imread('res/main.png')
#template_img = cv2.imread('res/chuzheng.png')
#print frame_estimate.can_match(main_img, template_img)
########################################################
'''

#bbox = (136, 60, 1800, 990)
bbox = (170, 76, 1766, 977)
mid_box = (968, 525)
main_topleft = (136, 60)
current_status = None
#ai = None
BADLY_HURT = False

class Current_Surface(Enum):
    unkonwn_surface = 0
    main_surface = 1
    map_select = 2
    fleet_select = 3
    
    batttle_result = 4
    
    

def get_screen():
    current_im = ImageGrab.grab(bbox)
    current_im_cv2 = cv2.cvtColor(numpy.asarray(current_im), cv2.COLOR_RGB2BGR)
    return current_im_cv2
    #cv2.imshow('Detected', current_im_cv2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()    
    
def screen_can_match(template_img):
    current_screen = get_screen()    
    (isMatched, current_x, current_y) = frame_estimate.can_match(current_screen, template_img)
    return isMatched, current_x, current_y
    
    
def get_current_status():   
    current_im = ImageGrab.grab(bbox)
    current_im_cv2 = cv2.cvtColor(numpy.asarray(current_im), cv2.COLOR_RGB2BGR)
    template_img = cv2.imread('res/chuzheng.png') 
    (ismatched, matched_x, matched_y) =  frame_estimate.can_match(current_im_cv2, template_img)
    if ismatched == True:
        current_status = Current_Surface(1)
    else:
        current_status = Current_Surface(0)     
    return  current_status, matched_x, matched_y

def chuzheng_operation():
    global current_status
    expedition = (1380, 350)
    
    #(current_status, get_x, get_y) = get_current_status()
    #if current_status == Current_Surface.main_surface :
    #    ai = auto_input()
    #    ai.mouse_click(get_x + main_topleft[0], get_y + main_topleft[1])    
    #    
    #else :
    #    print 'chuzheng_operation failed'    
    ai = auto_input()
    ai.mouse_click(expedition[0], expedition[1])
    time.sleep(4)    
    #ai.mouse_click(140, 910)
    #time.sleep(4) 

def map_select():
    global current_status
    global mid_box
    chapter_orie  = (970, 835)

    ai = auto_input()
    #ai.mouse_click(chapter_orie[0] + main_topleft[0], chapter_orie[1] + main_topleft[1])
    ai.mouse_click(1108, 902)
    
    time.sleep(2.5)
    #ai.mouse_click(mid_box[0] + main_topleft[0], mid_box[1] + main_topleft[1])
    ai.mouse_click(1090, 484)
    time.sleep(3.5)
    
    #print 'chuzheng_operation failed'

def battle_prepare():
    global BADLY_HURT
    global current_status
    global mid_box
    quick_supply = (1707, 154)
    whole_supply = (1240, 744)
    quick_repair = (1684, 291)
    expedition_start = (979, 915)
    
    ai = auto_input()
    ai.mouse_click(quick_supply[0], quick_supply[1])
    time.sleep(4)
    ai.mouse_click(whole_supply[0], whole_supply[1])
    time.sleep(4)
    if BADLY_HURT:
        ai.mouse_click(quick_repair[0], quick_repair[1])
        time.sleep(4)
        ai.mouse_click(whole_supply[0], whole_supply[1])
        BADLY_HURT = False
        time.sleep(4)                 
    ai.mouse_click(expedition_start[0], expedition_start[1])
    time.sleep(4)

def battle_isdone():
    #current_img = get_screen()
    while True:
        #current_img = cv2.imread('res/battle_result_s.png')
        current_img = get_screen()
        template = cv2.imread('res/ss_win.png')
        (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
        if isMatched == True:
            break 
        template = cv2.imread('res/s_win.png')    
        (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
        if isMatched == True:
            break 
        time.sleep(4)
    #print isMatched, current_x, current_y     

def is_badly_hurt():
    #admiral_back = (1375, 766)
    global BADLY_HURT
    #current_img = cv2.imread('res/ship_hurt_result.png')
    current_img = get_screen()
    template = cv2.imread('res/request_fail.png')
    (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
    if isMatched:
        BADLY_HURT = True
        #ai = auto_input()
        #ai.mouse_click(admiral_back[0], admiral_back[1])
        #time.sleep(3)
        return 11  
    template = cv2.imread('res/badly_hurt.png')
    #template = cv2.imread('res/can_not_head.png')
    (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
    if isMatched:
        BADLY_HURT = True
        return 22  
    return 0        
        
def fight():
    global mid_box
    start_fight = (1316, 852)
    #start_fight = (1316, 902)
    submarine_formation = (1486, 865)
    mid_ori = (1053, 519)
    continue_next = (1634, 920)
    back_bay = (1156, 702)
    admiral_back = (1375, 766)

    ai = auto_input()
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(2)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(3)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(2)
    
    ai.mouse_click(start_fight[0], start_fight[1])
    time.sleep(0.5)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(0.5)
    ai.mouse_click(submarine_formation[0], submarine_formation[1])
    time.sleep(1)
    
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(1)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(1)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(1)
    
    #time.sleep(50) #fighting 
    time.sleep(6) #fighting 
    battle_isdone()
    
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(2)
    ai.mouse_click(mid_ori[0], mid_ori[1])
    time.sleep(2)
    ai.mouse_click(continue_next[0], continue_next[1])
    time.sleep(0.5)
    ai.mouse_click(mid_ori[0], mid_ori[1]) #get ship
    time.sleep(1)
    ai.mouse_click(mid_ori[0], mid_ori[1]) 
    time.sleep(0.5)
    
    back_code = is_badly_hurt()
    if back_code == 11:
        ai.mouse_click(admiral_back[0], admiral_back[1])
    else:
        ai.mouse_click(back_bay[0], back_bay[1])
    time.sleep(3)
    #ai.mouse_click(mid_ori[0], mid_ori[1])
    #time.sleep(3)  
    
    
def battle_6_1_for_level():
    #for i in range(10):
    chuzheng_operation()
    map_select()     
    battle_prepare()
    fight()
    
    
    
    

def main():
    while True:
        battle_6_1_for_level()
    
        

if __name__ == '__main__':
    main()
    
'''
    chuanwu = (1380, 700)
    chuzheng = (1390, 340)
    biandui = (230, 160)
    chuzheng = (1390, 340)
    chuzhengjm = (1100, 500)
    chuzhengks = (980, 900)
    zhengxing = (1600, 680)
    ai = auto_input()
    #ai.mouse_click(1380, 700)            
    #time.sleep(5)
    
    ai.mouse_click(chuzheng[0], chuzheng[1])            
    time.sleep(5)
    ai.mouse_click(chuzhengjm[0], chuzhengjm[1])            
    time.sleep(5)
    
    ai.mouse_click(chuzhengks[0], chuzhengks[1])            
    time.sleep(5)
    ai.mouse_click(chuzhengks[0], chuzhengks[1])            
    time.sleep(3)
    ai.mouse_click(chuzhengks[0], chuzhengks[1])            
    time.sleep(3)
    
    ai.mouse_click(zhengxing[0], zhengxing[1])            
    time.sleep(3)
    ai.mouse_click(chuzhengks[0], chuzhengks[1])            
    time.sleep(3)
'''

    