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
    
    
    
    ###RTB Dashboard Overview Report
    

    
    
    
    ##RTB Dashboard Overview Report - Click on All
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    sleep(7)
    ##Select Adokut
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[4]/span').click()
    sleep(2)
    ##Select Today from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Today Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    sleep(2)
    ##Click on the Apply button 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()

    sleep(2)    
    print("RTB - Adokut_Overview Report for Today filter succesfully")
    
    
    
        ##Select Last_Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Last_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    sleep(2)
    ##Click on the Apply button 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()
    sleep(2)    
    print("RTB - Adokut_Overview Report for Last_Month filter succesfully")
    
    
            ##Select Custom_Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Custom_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    sleep(2)

    ##Click on the From Date 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
   
    ##Click on the To Date
    
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    sleep(2)
    
    #Click on the Apply Button
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()
    sleep(2)    

    print("RTB - Adokut_Overview Report for Custom_Month filter succesfully")
    
    driver.refresh()
    sleep(5)

    ##############RTB - Admida ############
    
    ##RTB Dashboard Overview Report - Click on All
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    sleep(7)
    ##Select Admida
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span').click()
    sleep(2)
    ##Select Today from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Today Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    sleep(2)
    ##Click on the Apply button 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()

    sleep(2)    
    print("RTB - Admida_Overview Report for Today filter succesfully")
    
    ######
    
    
    
    
        ##Select Last_Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Last_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    sleep(2)
    ##Click on the Apply button 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()
    sleep(2)    
    print("RTB - Admida_Overview Report for Last_Month filter succesfully")
    
    
            ##Select Custom_Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Custom_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    sleep(2)

    ##Click on the From Date 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
   
    ##Click on the To Date
    
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    sleep(2)
    
    #Click on the Apply Button
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[3]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()
    sleep(2)    

    print("RTB - Admida_Overview Report for Custom_Month filter succesfully")
    
    print("Run succesfully")
except ValueError:
    print("error")