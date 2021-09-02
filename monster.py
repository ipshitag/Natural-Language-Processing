def get_jobs(keyword, num_jobs,path,slp_time):
    
    """
    Get jobs from Monster, by passing a keyword. The returned dataframe includes
    -Job Title -> Title of the job, as given by employer
    -Searched Job Title -> The keyword passed as argument, the searched element
    -Full Description -> Full Description that comes after clicking 'See More'
    -Company Name -> Name of the Company
    -URL -> Link of individual jobs
    
    All the above data can be commented out as needed.
    
    
    Params: 
        - keyword = Job title to be searched
        - num_jobs = Number of jobs to be collected
        - verbose = Can be used to print the data as it is collected
        - path = path of the chromedriver
        - slp_time = time the browser needs to stop, depends on the network connection
    
    Returns:
        - Dataframe containing all the information
    """
    
    startTime = time.time()
    #Initializing the webdriver
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    options.add_argument('headless')
    
    
    url ='https://www.monster.com/jobs/search?q='+keyword+'&where=&geo=%27%27'
    driver.get(url)
    jobs = []
    pg=0
    num = 0
    
    print("Extracting: "+keyword)

    while len(jobs) < num_jobs:
      #executionTime = (time.time() - startTime)
      #if executionTime>250:
       # break


        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(3)

        pg = pg+1 
        currentJoblist = 0
        
        #pg = 0
        3#num = 0
        
        if not (len(jobs) >= num_jobs) and (pg<5):
            listButtonsCount = len(driver.find_elements_by_class_name('results-card'))
            
            #print("No of job butons:" +str(listButtonsCount))
            #pg = pg+1

            #Going through each job in this page
            job_buttons = driver.find_elements_by_xpath('//*[@class="title-company-location"]/a')
            i = 0
            
            for job_button in job_buttons:
                
                if i>num_jobs:
                    break
                
                key = True
    
                #print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
                if len(jobs) >= num_jobs:
                    break
                
                try:            
                    job_button.click()  #You might 
                except (StaleElementReferenceException,ElementNotInteractableException) as e:
                    driver.refresh()
                
                time.sleep(4)
                
                #code to kill the sign-up pop-up after it render on screen
                # if not found_popup:
                                         
                collected_successfully = False
                
                while not collected_successfully:
                    try:
                        # company_name
                        try:
                            company_name = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            company_name = -1
                        
                        # location
                        try:
                            location = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[1]').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            location = -1
                        
                        # job_title
                        try:
                            job_title = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/h1').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_title=-1
                                                         
                        #parent
                        try:
                            #job_description = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[4]/div/div[2]/div/div[1]/div').text
                            job_description = driver.find_element_by_xpath("//div[contains(@class, 'jobdescriptioncomponent__SanitizedHtmlContainer-my61fv-2 gvwQGf')]").text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_description = -1
                        
                        
                        #job function
                        try:
                            job_function = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/h1').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_function = -1
                            
                        
                        collected_successfully = True
                    except:
                        collected_successfully=False
                        #time.sleep(5)
    
                    
                    
                num = num+1
                jobs.append({"Job Title" : job_title,
                            "Searched Job Title" : keyword,
                            "Company Name" : company_name,
                            "Full Description" : job_description,
                            "Location" : location,
                            "URL" : url})
                    
                
                i = i+1
                
                print("----- {0} {1} ----- Page {2}".format(num,keyword,pg))
    
                currentJoblist=currentJoblist+1 # increasing the count of the list of buttons clicked and saved
                
                if not (currentJoblist < listButtonsCount): # to check the list last button and to go to next page
                        pg=pg+1
                        currentJoblist = 0  # resetting the button list count for new page button's list
                        break

    driver.quit()
    
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
