import cv2

def can_match(img_main, img_template):
    img_gray = cv2.cvtColor(img_main, cv2.COLOR_BGR2GRAY)
    img_template_gray = cv2.cvtColor(img_template, cv2.COLOR_BGR2GRAY)
    w, h = img_template_gray.shape[::-1]
    
    res = cv2.matchTemplate(img_gray, img_template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if max_val <= 0.8:
        return (False, (0, 0))
    else :
        top_left = max_loc
        return (True, (top_left[0]+w/2, top_left[1]+h/2))
    
    '''
    top_left = max_loc
    bottom_right = (top_left[0]+w, top_left[1]+h)
    cv2.rectangle(img_rgb, top_left, bottom_right, (255, 0, 0), 2)    
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
if __name__ == '__main__':
    img_rgb = cv2.imread('main.png')
    template = cv2.imread('region1.png')

    print can_match(img_rgb, template)
        