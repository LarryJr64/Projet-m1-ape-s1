from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options, executable_path='C:\Program Files (x86)\chromedriver.exe')
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options = options)
driver.quit()

def horoscope() :
        
    driver = webdriver.Chrome(PATH, options = options)
    bm = (input("Veillez renseigner en chiffre votre mois de naissance: "))
    bd = (input("Veillez renseigner en chiffre votre jour de naissance: "))         
    bmbd = bm + bd
    bmbd = int(bmbd)
               
    if (bmbd > 121) and (bmbd <= 219) :
        print("Vous êtes Verseau !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_verseau.html")
                    
    if bmbd > 220 and bmbd <= 320 :
        print("Vous êtes Poisson !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_poissons.html")
                    
    if bmbd > 321 and bmbd <= 420 :
        print("Vous êtes Bélier !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_belier.html")
                
    if bmbd > 421 and bmbd <= 520 :
        print("Vous êtes Taureau !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_taureau.html")
                
    if bmbd > 521 and bmbd <= 621 :
        print("Vous êtes Gémeau !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_gemeaux.html")
                
    if bmbd > 622 and bmbd <= 723 :
        print("Vous êtes Cancer !") 
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_cancer.html")
                
    if bmbd > 724 and bmbd <= 823 :
        print("Vous êtes un Lion !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_lion.html")
                    
    if bmbd > 824 and bmbd <= 923 :
       print("Vous êtes Vierge !")
       driver.get("https://www.horoscope.fr/horoscopes/horoscope_vierge.html")
                    
    if bmbd > 924 and bmbd <= 1023 :
        print("Vous êtes Balance !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_balance.html")
                
    if bmbd > 1024 and bmbd <= 1122 :
        print("Vous êtes Scorpion !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_scorpion.html")
                
    if bmbd > 1123 and bmbd <= 1220 :
        print("Vous êtes Sagittaire !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_sagittaire.html")
                
    if bmbd > 1221 and bmbd < 1231 or bmbd <= 120 and bmbd > 101 :
        print("Vous êtes Capricorne !")
        driver.get("https://www.horoscope.fr/horoscopes/horoscope_capricorne.html")
                
            
    driver.maximize_window()
    time.sleep(3)
        
    try :
        driver.find_element_by_xpath('/html/body/div[3]/div/button').click() # on enlève le pop-up cookie (une deuxième fois)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre (une deuxième fois)
    except :
        pass
        
    def section_amour() :
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[1]').click()
                
        
            # on se place sur la partie qui compose les predictions sur le travail  
    def section_travail() :
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[2]').click()
        
                 
            # on se place sur la partie qui compose les predictions sur la finance    
    def section_finance() :
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[3]').click() 
             
                 
            # on se place sur la partie qui compose les predictions sur le bien être
    def section_bien_être() :
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[4]').click()
        
        
            # on se place sur la partie qui compose les predictions sur l'entourage
    def section_entourage() :
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[5]').click()
             
        # on se place sur la partie qui compose les predictions sur l'amour
        
    try :
        driver.find_element_by_xpath('/html/body/div[3]/div/button').click() # on enlève le pop-up cookie (une deuxième fois)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre (une deuxième fois)
    except :
        pass
        
            
        # les "petites" predictions qui se composent seulement d'une note sur 6 (fait avec des emojis)    
        
        
            # Amour   
    section_amour()
    time.sleep(2)
    nbr_amour = len(driver.find_elements_by_xpath("//div[@class='wrapper-part love-horo-wrapper background-part part-nav-category']/div[@class='wrapper-note love-note']//i[@class='fa fa-heart']"))
    nbr_amour_emoji = nbr_amour * "❤️"
            
            # Travail 
    section_travail()
    time.sleep(2)
    nbr_travail = len(driver.find_elements_by_xpath("//div[@class='wrapper-part part-nav-category']/div[@class='wrapper-note work-note']//i[@class='fa fa-star']"))
    nbr_travail_emoji = nbr_travail * "⭐"
            
            # Finance
    section_finance()
    time.sleep(2)
    nbr_finance = len(driver.find_elements_by_xpath("//div[@class='wrapper-part border-top part-nav-category']/div[@class='wrapper-note money-note']//i[@class='fa fa-star']"))
    nbr_finance_emoji = nbr_finance * "💲"
            
            # Bien-être
    section_bien_être()
    time.sleep(2)
    nbr_bienêtre = len(driver.find_elements_by_xpath("//div[@class='wrapper-part border-top part-nav-category']/div[@class='wrapper-note vitality-note']//i[@class='fa fa-star']"))
    nbr_bienêtre_emoji = nbr_bienêtre * "🔥"
            
    try :
        driver.find_element_by_xpath('//*[@id="axeptio_btn_dismiss"]').click() # on enlève le pop-up cookie
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre
    except :
        pass
            
            # Entourage
    section_entourage()
    time.sleep(2)
    nbr_entourage = len(driver.find_elements_by_xpath("//div[@class='wrapper-part border-top part-nav-category']/div[@class='wrapper-note family-note']//i[@class='fa fa-star']"))
    nbr_entourage_emoji = nbr_entourage * "👪"
            
    print("\n Voici nos prédictions sur votre journée : \n Amour : " + nbr_amour_emoji + "\n Travail : " + nbr_travail_emoji + "\n Finance : " + nbr_finance_emoji + "\n Bien-être : " + nbr_bienêtre_emoji + "\n Entourage : " + nbr_entourage_emoji)
            
    try :       
        driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre
    except :
        pass
            
    # là on demande si la personne veut le détails de la prédiction (avec des phrases)
    def détails_predictions() :    
        
        choix_prediction = (input("Voulez vous en savoir plus sur : \n1. Amour \n2. Travail\n3. Finance\n4. Bien-être \n5. Entourage \n6. Sexe \n7. Rien\n\n Votre réponse : ")).lower()
        
        try :
            driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre
            détails_predictions() # je relance la fonction sinon ça fait bug
        except :
            pass
        
        if choix_prediction == "amour" :
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[1]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_0"]/div[3]/p').text)      
            retry()  
            
        if choix_prediction == "sexe" :
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[1]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_0"]/p[2]').text)      
            retry()         
            
        if choix_prediction == "travail" :
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[2]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_1"]/p').text)
            retry()
            
        if choix_prediction == "finance" :
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[3]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_2"]/div[2]/p').text)
            retry()
            
        if choix_prediction == "bien-être" :
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[4]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_3"]/p').text)
            retry()
            
        if choix_prediction == "entourage" :
            try :
                driver.find_element_by_xpath('//*[@id="axeptio_btn_dismiss"]').click() # on enlève le pop-up cookie
                driver.find_element_by_xpath('/html/body/div[4]/div/div[1]').click() # on enlève le gros pop-up bizarre
            except :
                pass
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/div[1]/div[3]/span[5]').click()
            print("\n" + driver.find_element_by_xpath('//*[@id="part_4"]/p').text)
            retry()
            
        if choix_prediction == "rien" : 
            driver.quit()
            
        if  ((choix_prediction != "amour") is True) and ((choix_prediction != "sexe") is True) and ((choix_prediction != "travail") is True) and ((choix_prediction != "finance") is True) and ((choix_prediction != "bien_être") is True) and ((choix_prediction != "entourage") is True) and ((choix_prediction != "rien")is True) :
            print("\nVeillez réécrire votre réponse")
            détails_predictions()
            
    def retry():
        continuer = (input("Voulez vous en savoir plus les autres prédictions ?' : \n1. Oui \n2. Non \nVotre réponse : ")).lower()
        
        if continuer == "oui" :
            détails_predictions()
            
        if continuer == "non" :
            driver.quit()
            
        if ((continuer != "oui") is True) and ((continuer != "non") is True) :
            print("\nVeillez répondre par oui ou non")
            retry()      
  
    
    détails_predictions()
  
    
 

def jeu_de_rune() : 
    driver = webdriver.Chrome(PATH, options = options)
    repn = input("Voulez-vous faire un jeu de tirage des runes ? \n a. Oui \n b. Non \n Votre réponse: ")
    if repn == "a" or repn == 'oui':
        driver.get('https://e-spacevoyance.fr/jeux/tirage-des-runes-gratuit')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[2]/div/div/div[2]/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[2]/div/div/div[2]/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[2]/div/div/div[2]/img').click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/main/div/section[1]/div[1]/div[2]/div[1]/button').click()
       
          
        
    if repn=='b' or repn == "non":
        print("Dommage!")
    
    
    try:
        prem = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[1]/div[2]/h3')
        
        exp1 = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[1]/div[2]/p[1]/strong')
        
        deux = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[2]/div[2]/h3')
        
        exp2 = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[2]/div[2]/p[1]/strong')
        
        tr = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[3]/div[2]/h3')
        
        exp3 = driver.find_element_by_xpath('/html/body/main/div/section[1]/div[2]/article[3]/div[2]/p[1]/strong')
     
        
    except:
        print("bug")
        driver.quit()
        
    ##### première rune 
    time.sleep(5)
    print("\n" +prem.text) 
    print(exp1.text)
    time.sleep(2)
    
    ###### deuxième rune
    driver.execute_script("window.scrollTo(0, 900)") 
    print("\n" + deux.text)
    print(exp2.text)
    time.sleep(2)
    
    ##### trousième rune
    print("\n" + tr.text)
    print(exp3.text)
    time.sleep(2)                 
      






def boule_de_crystal() : 
    driver = webdriver.Chrome(PATH, options = options)   
    rep = input('Voulez-vous \n a. Poser une question? \n b. Connaître votre futur? \n c. Votre destin amoureux? \n Réponse: ').lower()
    if rep == "a"  or rep == "question " :
        driver.get('https://www.bouledecristalgratuite.com/')
        print("Posez votre question")
        mystère = input('Votre question: ')
    if rep == "b"  or rep =="futur" :
        driver.get('https://www.bouledecristalgratuite.com/boule-voyance') and driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]').click()
    if rep=="c" or rep == "amour" :
        driver.get('https://www.bouledecristalgratuite.com/amour')   

    ######## On cherche les réponses 
    
    
    try:
        element1=WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p'))
            )
        element1.click()
        
        
        
        element=WebDriverWait(driver, 4).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div[1]/form/div[1]/textarea"))
            )
        element.click()
        element.send_keys(mystère)
        driver.find_element_by_xpath('/html/body/div[3]/div[1]/form/div[2]/a/img').click()
        time.sleep(2.0)
        print(driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/span').text)
        
       
    except:
        element2=WebDriverWait((driver), 2).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/form/input'))
            )
        element2.click()
    
        try:
            element3=WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/form/input'))
                )
            element3.click()
        except:
            elem=WebDriverWait((driver), 4).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[2]/div/div/span'))
            )
            print(elem.text)
            
def galaxy() :    
    étoile = input('Voulez-vous \n a. Consulter votre horoscope \n b. Tirer les runes  \n c. Regardez dans la boule de crystal \n d. Quitter \n Réponse: ').lower()
    if étoile == "a" or "horoscope ":
        horoscope()
        galaxy()
    if étoile == "b" or "runes" or "rune":
        jeu_de_rune()
        galaxy()
    if étoile=="c" or "boule":
        boule_de_crystal()
        galaxy()
    if étoile == "d" or "quitter" :
        driver.quit()
    else:
        print("bug")     

galaxy()
