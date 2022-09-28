from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


driver = webdriver.Chrome(r'/home/lynxkub/Desktop/chromedriver')



quant = 'https://www.quanthockey.com/nhl/seasons/nhl-players-stats.html'

driver.get(quant)



titles = driver.find_elements(By.XPATH , '//tr[@class="orange"]')

full_titles = []
for title in titles:
    title_list = title.find_elements(By.TAG_NAME , 'th')
    for i in title_list :
        full_titles.append(i.text)


def scrape(next_page = 2 , full_stats = []) :
    time.sleep(1)
    if next_page > 20:
        file = open('stats.csv' , 'w')
        writer = csv.writer(file)
        writer.writerow([title for title in full_titles[1:]])
        for stat_line in full_stats:
            writer.writerow([stat for stat in stat_line])
        file.close()
        return

    odds_attempt = False
    while odds_attempt == False:
        odds = driver.find_elements(By.XPATH , '//tr[@class="odd"]')
        if len(odds) < 5:
            print('did not find odds')
            odds_attempt = False
        else:
            odds_attempt = True
    
    evens_attempt = False
    while evens_attempt == False:
        evens = driver.find_elements(By.XPATH , '//tr[@class="even"]')
        last_even = driver.find_elements(By.XPATH , '//tr[@class="even_lr"]')
        if len(evens) < 5 :
            print('did not find evens')
            evens.append(last_even)
            evens_attempt = False
        else:
            evens_attempt = True
    
    for stat in odds:
        stat_list = stat.find_elements(By.TAG_NAME , 'td')
        name = stat.find_element(By.XPATH , './/a[@class="hl qh-nowrap"]')
        list_of_stats = []
        try:
            list_of_stats.append(name.text)
        except:
            print('could not find odd name')

        country = stat.find_element(By.XPATH , './/img[@width="16"]')
        country_src = country.get_attribute('src')
        strip = country_src.replace('https://cdn77.quanthockey.com/img/country-flags/' , '')
        second_strip = strip.replace('-Flag-16.png' , '')

        try:
            list_of_stats.append(second_strip)
        except:
            print('could not find odd country')

        for entry in stat_list :
            try:
                list_of_stats.append(entry.text)
            except:
                print('could not find odd list of stats')
        # print(list_of_stats)
        full_stats.append(list_of_stats)
        
    

    for stat in evens:
        list_of_stats = []
        stat_list = stat.find_elements(By.TAG_NAME , 'td')
        name = stat.find_element(By.XPATH , './/a[@class="hl qh-nowrap"]')
    
        try:
            list_of_stats.append(name.text)
        except:
            print('could not find even name')
        country = stat.find_element(By.XPATH , './/img[@width="16"]')
        country_src = country.get_attribute('src')
        strip = country_src.replace('https://cdn77.quanthockey.com/img/country-flags/' , '')
        second_strip = strip.replace('-Flag-16.png' , '')

        try:
            list_of_stats.append(second_strip)
        except:
            print('could not find even country')

        for entry in stat_list :
            try:
                list_of_stats.append(entry.text)
            except:
                print('could not find even stat entry')
        # print(list_of_stats)
        full_stats.append(list_of_stats)
    

    attempt = False 
    if next_page <= 20 :
        while attempt == False:
            try:
                button = driver.find_element(By.XPATH , f'//a[@ga4-page="{next_page}"]')
                button.click()
                print(len(full_stats))
                next_page = next_page + 1
                attempt = True
                
                return scrape(next_page , full_stats)
            except:
                print(next_page)
                attempt = False
                print('trying to find button again')
                
        
# not adding in the pages dynamically

full_titles
scrape()


driver.quit()


# def page_turn(next_page = 2):
#     if next_page > 20:
#         print('at 20')
#         return
#     else:
#         time.sleep(3)
#         button = driver.find_element(By.XPATH , f'//a[@ga4-page="{next_page}"]')
#         button.click()
#         next_page = next_page + 1
#         page_turn(next_page)

# page_turn()



# Find list of names on first page
# names = driver.find_elements(By.XPATH , '//a[@class="hl qh-nowrap"]')
# countries = driver.find_elements(By.XPATH , '//img[@width="16"]')
# teams = driver.find_elements(By.XPATH, '//td[@class="alignleft hl"]')



    
# full_titles[1] = 'Country'
# full_titles.remove(full_titles[0])
# print(full_titles)    

# full_stats = []






# print(full_stats)



# button = driver.find_element(By.XPATH , '//img[@alt="Next Page"]')
# button_src = button.get_attribute('src')
# print(button_src)
# page_num = 2

# button = driver.find_element(By.XPATH , f'//a[@ga4-page="{page_num}"]')
# button.click()



# Print out the name of each player
# for name in names:
#     try:
#         # print(stat.find_element(By.XPATH, './/a[@class="hl qh-nowrap"]').text)
#         print(name.text)
        
#     except:
#         pass

# Find each country of the players
# for country in countries:
#     try:
#         country_src = country.get_attribute('src')
#         strip = country_src.replace('https://cdn77.quanthockey.com/img/country-flags/' , '')
#         second_strip = strip.replace('-Flag-16.png' , '')
#         print(second_strip)
#     except:
#         pass

# Find each player's team
# for team in teams:
#     child = team.find_element(By.TAG_NAME , 'a')
#     team_name = child.get_attribute('title')
#     print(team_name)




# Close out webpage
# driver.quit()



    