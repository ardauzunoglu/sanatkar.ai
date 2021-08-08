from selenium import webdriver
import time

poets = ["orhan-veli-kanik", "melih-cevdet-anday", "oktay-rifat"]
poet_name_dict = {
    "orhan-veli-kanik":"Orhan",
    "melih-cevdet-anday":"Melih",
    "oktay-rifat":"Oktay"
}

path = "C:\chromedriver.exe"
driver = webdriver.Chrome(path)

def scrape_poems(poet):
    
    driver.get("https://www.antoloji.com/"+poet+"/siirleri/ara-/sirala-/")
    driver.maximize_window()

    time.sleep(3)

    close = driver.find_element_by_xpath("//*[@id='cookiePolicyw']/div")
    close.click()

    f = open(str(poet) + ".txt", "w", encoding="utf-8")
    x = 1

    while x<=5:
        i = 1
        while i <= 30:
            url = "https://www.antoloji.com/"+poet+"/siirleri/ara-/sirala-/sayfa-" + str(x)
            driver.get(url)

            time.sleep(1)
            
            if i == 1:

                poem = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li["+str(i)+"]/div[2]/a")
                poem.click()

                time.sleep(1)

                driver.get("https://www.antoloji.com/"+poet+"/siirleri/ara-/sirala-/sayfa-" + str(x))

                time.sleep(1)

                poem = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li["+str(i)+"]/div[2]/a")
                poem.click()

            else:
                poem = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/ul/li["+str(i)+"]/div[2]/a")
                poem.click()

            time.sleep(1)

            poem_itself = driver.find_element_by_class_name("pd-text").text
            poet_name_index = poem_itself.index(poet_name_dict[poet])
            poem_itself = poem_itself[:poet_name_index]

            f.write(poem_itself + "\n")
            i+=1

            driver.get(url)

        x += 1

        next_page = driver.find_element_by_class_name("PagedList-skipToNext")
        next_page.click()

        time.sleep(1)

    f.close()
    print(poet + " şairin şiirleri çekildi.")

for poet in poets:
    scrape_poems(poet)