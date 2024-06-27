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
    sleep(5)
    print("Login succesfully")
    #Dashboard_Overview Report_ClickAll
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    sleep(7)
    ##Select_Admida From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span').click()
    sleep(2)
    ##Apply for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    
    print("Admida_Overview Report for CurrentMonth succesfully")
    ##ClickOn TodayFrom Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    sleep(2)
    ##Apply for Today
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Admida_Overview Report for Today filter succesfully")
    
    ##ClickOn Yesterday From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[3]').click()
    sleep(2)
    ##Apply for Yesterday
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Admida_Overview Report for Yesterday filter succesfully")
    
        ##ClickOn Last Month From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    sleep(2)
    ##Apply for Last Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Admida_Overview Report for Last Month filter succesfully")
    
    
            ##ClickOn Custom Month From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    sleep(2)
    ##Select From Date
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    sleep(2)
    ##Select To Date
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    sleep(2)
    ##Apply for Custom Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()
    sleep(2)
    print("Admida_Overview Report for Custom Month filter succesfully")
    
    print("Admida_Filter for Dashboard Overview Function Completed")
    
    driver.refresh()
    sleep(2)
    
    ###############################################################################################################################################
    
    #Dashboard_Overview Report_ClickAll
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/div/div/div[3]/input').click()
    sleep(7)
    ##Select_Adokut From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[4]/span').click()
    sleep(2)
    ##Apply for Current Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    
    print("Adokut_Overview Report for CurrentMonth succesfully")
    ##ClickOn TodayFrom Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[2]').click()
    sleep(2)
    ##Apply for Today
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Adokut_Overview Report for Today filter succesfully")
    
    ##ClickOn Yesterday From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[3]').click()
    sleep(2)
    ##Apply for Yesterday
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Adokut_Overview Report for Yesterday filter succesfully")
    
        ##ClickOn Last Month From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[6]').click()
    sleep(2)
    ##Apply for Last Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]').click()
    sleep(2)
    print("Adokut_Overview Report for Last Month filter succesfully")
    
    
            ##ClickOn Custom Month From Filter
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select').click()
    sleep(2)
    ##Select 
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[2]/select/option[7]').click()
    sleep(2)
    ##Select From Date
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[3]/div/div').click()
    sleep(2)
    ##Select To Date
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[4]/div/div').click()
    sleep(2)
    ##Apply for Custom Month
    driver.find_element("xpath", '/html/body/app-root/ngx-pages/ngx-one-column-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/app-dashboard/app-superadmin-dashboard/div[2]/div[1]/nb-card/nb-card-header/div/div/div[5]/button').click()
    sleep(2)
    print("Adokut_Overview Report for Custom Month filter succesfully")
    
    print("Adokut_Filter for Dashboard Overview Function Completed")
    
    
    print("Run succesfully")
except ValueError:
    print("error")