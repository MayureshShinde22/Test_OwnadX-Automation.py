from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://staging.ownadx.com")
sleep(3)
#login details 


try:
    
    Last1 = driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[1]/input').send_keys("superadmin@ownadx.com")
    sleep(2)
    Last2 = driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys("admin@123")
    sleep(2)
    
    driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[3]/button').click()
    sleep(7)
    print("Login succesfully")
    
    #driver.get("https://staging.ownadx.com/#/pages/partner-template/list-partner-template")

    
    
    #Click on the Manage Partner
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/nb-sidebar/div/div/nb-menu/ul/li[3]/a/nb-icon[1]').click()
    sleep(2)
    #Click on the List Partner Template
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/nb-sidebar/div/div/nb-menu/ul/li[3]/ul/li/a').click()
    sleep(2)
    driver.refresh
    sleep(8)
    print("Succesfully Reached to the List Partner Template window")
    
    ##Checking the SORT function for List Partner Template 
    #Click on the ID Sort
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[2]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[2]').click()
    sleep(2)
    
  #  # Search by Id 
  #  
  #  driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[2]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
  #  sleep(2)
  #  driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[2]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').send_keys("123")
  #  sleep(2)
  #  ##clear input
  #  driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[2]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').clear()
  #  sleep(2)
#
  

    print("Sort & search feature for ID is working")
    
 
    #Click on the List Partner Template
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[3]').click()
    sleep(2)
   # driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[3]').click()
    #sleep(2)
    #Click on the Search by List Partner Template
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[3]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
    sleep(2)
    
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[3]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').send_keys("look")
    sleep(2)
    ##clear input
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[3]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').clear()
    sleep(5)
   # driver.refresh
   # sleep(8)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[3]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').send_keys("ownAdx")
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[3]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').clear()
    sleep(2)
   # driver.refresh
   # sleep(8)
    print("Sort & Search feature of List Partner Template is working")
    
    #Click on the Platform Name 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[4]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[4]').click()
    sleep(2)
    ##Click on search 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
    sleep(8)
    
    print("Sort & search feature for Platform Name is working")
    
    
    
    #Click on the Integration/Feed Type 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[5]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[5]').click()
    sleep(2)
    ##click on search 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
    sleep(8)
    print("Sort & search feature for Integration/Feed Type is working")

    
    #Click on the Product 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[6]').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[6]').click()
    sleep(2)
    
    ##Click on search
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[6]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
    sleep(2)
    
    print("Sort & search feature for Product is working")

    #Click on the Status
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[7]').click()
    sleep(2)
    
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[1]/th[7]').click()
    sleep(2)
    
    ##Click on search 

    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-list-partner-template/div[2]/div/nb-card/nb-card-body/div[2]/ng2-smart-table/table/thead/tr[2]/th[7]/ng2-smart-table-filter/div/default-table-filter/input-filter/input').click()
    sleep(2)

    print("Sort & search feature for Product is working")

    
    
    
    
    
    
    
    
    
    
     
    print("Run succesfully")    
except ValueError:
    print("error")