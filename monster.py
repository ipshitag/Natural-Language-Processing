def get_jobs(keyword, num_jobs,path,slp_time):
    
    #timer
    startTime = time.time()
    
    #driver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    options.add_argument('headless')
    
    #counter and flags
    jobs = []
    num = 0
    
    #url
    url ='https://www.monster.com/jobs/search?q='+ keyword +'&where=&geo=%27%27&page=6'
    driver.get(url)
    jobs = []
    
    print("Extracting: "+keyword)
    
    #wait
    time.sleep(slp_time)
    
    #get parent id's
    listButtonsCount = len(driver.find_elements_by_class_name('results-card'))
    job_buttons = driver.find_elements_by_xpath('//*[@class="title-company-location"]/a')
    
    for job_button in job_buttons:
        
        if not(num<num_jobs):
            #print(num)
            #print(num_jobs)
            executionTime = (time.time() - startTime)
            print('Execution time in seconds: ' + str(executionTime))
            return pd.DataFrame(jobs)
            
        job_button.click()
        
        #company name
        try:
            company_name = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[1]').text
        except (NoSuchElementException,StaleElementReferenceException) as e:
            company_name = '-1'
        
        #location
        try:
            location = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div[2]/div[1]').text
        except (NoSuchElementException,StaleElementReferenceException) as e:
            location = '-1'
        
        #job title
        try:
            job_title = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/h1').text
        except (NoSuchElementException,StaleElementReferenceException) as e:
            job_title = '-1'
        
        #job description
        try:
            job_description = driver.find_element_by_xpath("//div[contains(@class, 'jobdescriptioncomponent__SanitizedHtmlContainer-my61fv-2 gvwQGf')]").text
        except (NoSuchElementException,StaleElementReferenceException) as e:
            job_description = '-1'
        
        #job function
        try:
            job_function = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div[2]/h1').text
        except (NoSuchElementException,StaleElementReferenceException) as e:
            job_function = '-1'
            
        try:
            link = driver.find_element_by_xpath('//*[@id="card-view-panel"]/div/div[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/a').get_attribute('href')
        except (NoSuchElementException,StaleElementReferenceException) as e:
            link = '-1'
        
        num = num+1
        jobs.append({"Job Title" : job_title,
                     "Searched Job Title" : keyword,
                     "Company Name" : company_name,
                     "Full Description" : job_description,
                     "Location" : location,
                     "URL" : link})
        print("----- {0} {1} -----".format(num,keyword))
