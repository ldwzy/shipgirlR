import cv2
import frame_estimate
import time
import ShipGilrAutoRun

def battle_isdone():
    #current_img = get_screen()
    while True:
        current_img = cv2.imread('res/battle_result_s.png')
        #current_img = get_screen()
        template = cv2.imread('res/ss_win.png')
        (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
        if isMatched == True:
            break 
        template = cv2.imread('res/s_win.png')    
        (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)
        if isMatched == True:
            break 
        time.sleep(5)
    print isMatched, current_x, current_y    
        
        
#battle_isdone()
def get_screen():
    current_im_cv2 = ShipGilrAutoRun.get_screen()
  
    cv2.imshow('Detected', current_im_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 

#get_screen()    

def is_badly_hurt():
        #current_im = ShipGilrAutoRun.get_screen()
        #current_img = cv2.imread('res/ship_hurt_result.png')
        current_img = cv2.imread('res/admiral_hurt.png')
        #current_img = cv2.imread('res/go_head_or_return.png')
        #current_img = get_screen()
        #template = cv2.imread('res/badly_hurt.png')
        template = cv2.imread('res/request_fail.png')
        #template = cv2.imread('res/can_not_head.png')
        #template = cv2.imread('res/go_head.png')
        (isMatched, current_x, current_y) = frame_estimate.can_match(current_img, template)

        print isMatched, current_x, current_y 
        
is_badly_hurt()        