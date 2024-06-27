from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://staging.ownadx.com")
sleep(10)
#login details 


try:
    
    Last1 = driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[1]/input').send_keys("superadmin@ownadx.com")
    sleep(2)
    Last2 = driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[2]/div[1]/input').send_keys("admin@123")
    sleep(2)
    
    driver.find_element("xpath", '/html/body/app-root/app-auth/nb-layout/div/div/div/div/div/nb-layout-column/div/div/nb-card/nb-card-body/nb-auth-block/ng-component/div/div/div/div[2]/form/div[3]/button').click()
    sleep(7)
    print("Login succesfully")
    
    




    ###############Search Dashboard - Overview Report ###############################
    #Minimize XML-Tab
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[4]/div/nb-accordion/nb-accordion-item/nb-accordion-item-header').click()
    sleep(2)
    #    #####Search Dashboard Overview Report - Click on All
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    #sleep(7)
    ###Select Admida
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span').click()
    #sleep(2)
    ###Click on the Apply button for Current Month
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()
#
    #sleep(2)    
    #print("Search Dashboard- Admida_Overview Report for Current Month filter succesfully")
    #
    #
    #
    #
    #    ###Select Today from Filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    #sleep(2)
    ###Click on the Today Button from filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    #sleep(2)
    ###Click on the Apply button for Current Month
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()
#
    #sleep(2)    
    #print("Search Dashboard - Admida_Overview Report for Today filter succesfully")
    #
    #
    #    ###Select Last_Month from Filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    #sleep(2)
    ###Click on the Last_Month Button from filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    #sleep(2)
    ###Click on the Apply button for Current Month
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()
#
    #sleep(2)    
    #print("Search Dashboard - Admida_Overview Report for Last_Month filter succesfully")
#
#
    #        ###Select Custom Month from Filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    #sleep(2)
    ###Click on the Custom_Month Button from filter
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    #sleep(2)
    #
    ##Select From Date 
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    #sleep(2)
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
#
    ##Select To Date
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    #sleep(2)
#
    ###Click on the Apply button for Current Month
    #driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()
#
    #sleep(2)    
    #print("Search Dashboard - Admida_Overview Report for Custom_Month filter succesfully")
############################################################################################################################################################
    #driver.refresh()
    #sleep(5) 
    
    
    ###############Search Dashboard - Overview Report ###############################
    
        #####Search Dashboard Overview Report - Click on All
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    sleep(7)
    ##Select Adokut
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span').click()
    sleep(2)
    ##Click on the Apply button for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()

    sleep(2)    
    print("Search Dashboard- Adokut_Overview Report for Current Month filter succesfully")
    
    
    
    
        ###Select Today from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Today Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    sleep(2)
    ##Click on the Apply button for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()

    sleep(2)    
    print("Search Dashboard - Adokut_Overview Report for Today filter succesfully")
    
    
        ###Select Last_Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Last_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    sleep(2)
    ##Click on the Apply button for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/button').click()

    sleep(2)    
    print("Search Dashboard - Adokut_Overview Report for Last_Month filter succesfully")


            ###Select Custom Month from Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Click on the Custom_Month Button from filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    sleep(2)
    
    #Select From Date 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    sleep(2)
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()

    #Select To Date
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    sleep(2)

    ##Click on the Apply button for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[5]/div/nb-accordion/nb-accordion-item/nb-accordion-item-body/div/div/div[1]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()

    sleep(2)    
    print("Search Dashboard - Adokut_Overview Report for Custom_Month filter succesfully")
###########################################################################################################################################################
    driver.refresh()
    sleep(5) 
    
    print("Run succesfully")    
except ValueError:
    print("error")