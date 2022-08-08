from selenium import webdriver
from chromedriver_autoinstaller import install
from selenium.webdriver.common.by import By

import time

def login_autoClick_likeButton_instagram(url):
    username = input('username >>>>')
    password = input('password >>>>')
    
    

    driver = webdriver.Chrome(install())
    driver.get(url)
    time.sleep(3)
    
    ##########################   Login   ##########################
    id = driver.find_element(By.NAME,'username')
    id.send_keys(username)
    
    pw = driver.find_element(By.NAME,'password')
    pw.send_keys(password)
    
    # login 오류 예외 처리 
    # error_message = driver.find_element_by_css_selector(
    #     'div.eiCW-'
    # )
    # if error_message:
    #     print('❗️ >>>>>>>>>>>> 다시 입력하세요')
        
    
    button = driver.find_element(By.CSS_SELECTOR,
        "div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.CovQj.jKUp7.DhRcB"
    )
    button.click()
    time.sleep(6)
    
    ##########################  Login 후 popup창 예외 처리  ##########################
    popup1 = driver.find_element(By.CSS_SELECTOR,
        'div.pV7Qt.DPiy6.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.qhGB0.ZUqME'
    )  
    if popup1:
        print('❗️ >>>>>>>>>>>>>>>>>>>>>>>>> popup1')
        button = driver.find_element(By.CSS_SELECTOR,
            'div.cmbtv'
        )
        button.click()
        time.sleep(6)
        
    else:
        print('😀 >>>>>>>>>>>>>>>>>>>>>> no popup1')
    
    popup2 = driver.find_element(By.CSS_SELECTOR,
        'div._a9-v'
    )
    if popup2:
        print('❗️ >>>>>>>>>>>>>>>>>>>>>>>>> popup2')
        button = driver.find_element(By.CSS_SELECTOR,
            'button._a9--._a9_1'
        )
        button.click()
        time.sleep(6)
    else:
        print('😀 >>>>>>>>>>>>>>>>>>>>>> no popup1')
        
        
    
    ##########################  해시태그 검색 ##########################
    hash_tag = input('해시태그 입력 >>>>>>>>>>>>>>>')
    hash_tag_url = f'https://www.instagram.com/explore/tags/{hash_tag}/?hl=ko'
    driver.get(hash_tag_url)
    time.sleep(6)
    
    ##########################  첫번째 사진 클릭  ##########################
    first_photo = driver.find_element(By.CSS_SELECTOR,
        'div._aagw'
    )
    first_photo.click()
    time.sleep(5)
    
    ########################## 자동 좋아요 시작 ##########################
    while True:
        like = driver.find_element(By.CSS_SELECTOR,
            "section._aamu._aaz9 span>svg._ab6-"
        )
        next = driver.find_element(By.CSS_SELECTOR,
            "div._aaqg._aaqh > button._abl- svg._ab6-"
        )
        
        if like.get_attribute('aria-label') == '좋아요':
            like.click()
            time.sleep(5)
            next.click()
            time.sleep(5)
        else:
            next.click()
            time.sleep(5)



url = 'https://www.instagram.com/accounts/login/?hl=ko&source=auth_switcher'
login_autoClick_likeButton_instagram(url)
