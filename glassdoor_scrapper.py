def get_jobs(keyword, num_jobs, verbose,path,slp_time):
    
    """
    Get jobs from glassdoor, by passing a keyword. The returned dataframe includes
    -Job Title -> Title of the job, as given by employer
    -Searched Job Title -> The keyword passed as argument, the searched element
    -Salary Estimate -> The salary estimates given
    -Job Function -> The role of the job as given by employer
    -Job Description -> Description of job which comes before clicking 'See More'
    -Full Description -> Full Description that comes after clicking 'See More'
    -Company Name -> Name of the Company
    -Rating -> Rating of the company
    -Location -> Location of the job, as passed by user
    -Size -> Number of employees in the company
    -Founded -> When the company was founded
    -Type of ownership -> Kind of company
    -Industry -> Type of Industry
    -Sector -> Sector of the company
    -Revenue -> Revenue of the company
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
    
    driver =webdriver.Chrome('chromedriver',options=chrome_options)
    
    url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=N&locId=115&locKeyword=India&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=false&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
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

        try:
            time.sleep(5)
            driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()
            #print("worked")
              #clicking to the X.
    
        except NoSuchElementException:
            pass
        
        # found_popup = False 
        currentJoblist = 0
        #pg = 0
        3#num = 0
        
        if not (len(jobs) >= num_jobs) and (pg<5):
            listButtonsCount = len(driver.find_elements_by_xpath('//*[@id="MainCol"]//div[1]//ul//li[@data-test="jobListing"]'))
            
            #print("No of job butons:" +str(listButtonsCount))
            #pg = pg+1

            #Going through each job in this page
            job_buttons = driver.find_elements_by_xpath('.//*[@id="MainCol"]//a[@class="jobLink"]')  #jl for Job Listing. These are the buttons we're going to click.
            
            for job_button in job_buttons:  
                
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
                try:
                    driver.find_element_by_css_selector('[alt="Close"]').click()
                    #print("worked")
                    # print("&&& line 89")
                    # found_popup = True
                except (NoSuchElementException,StaleElementReferenceException) as e:
                    # print("&&& line 92")
                    pass
                          
                
                collected_successfully = False
                
                while not collected_successfully:
                    try:
                        # company_name
                        try:
                            company_name = driver.find_element_by_xpath('//*[@id="MainCol"]//li['+ str(currentJoblist + 1) +']//div[2]//a//span').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            company_name = -1
                        
                        # location
                        try:
                            location = driver.find_element_by_xpath('//*[@id="MainCol"]//li['+ str(currentJoblist + 1) +']//div[2]//div[2]/span').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            location = -1
                        
                        # job_title
                        try:
                            job_title = driver.find_element_by_xpath('//*[@id="MainCol"]//li['+ str(currentJoblist + 1) +']//a[@data-test="job-link"]').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_title=-1
                            
                            
                        if job_title != keyword:
                            key = False
                                
                        #parent
                        try:
                            job_description = driver.find_elements_by_xpath('.//div[@class="jobDescriptionContent desc"]')
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_description = -1
                        
                        #getting child
                        if job_description!=-1:
                            t = ' '
                            for element in job_description:
                                t = t + element.text
                            full_description = t
                        
                        #job function
                        try:
                            job_function = driver.find_element_by_xpath('//*[@id="JDCol"]//strong[text()[1]="Job Function :"]//following-sibling::*').text
                        except (NoSuchElementException,StaleElementReferenceException) as e:
                            job_function = -1
                        
                        #try:
                            #job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                        #except (NoSuchElementException,StaleElementReferenceException) as e:
                            #job_description = -1
                            
                        
                        collected_successfully = True
                    except:
                        collected_successfully=False
                        #time.sleep(5)
    
                try:
                    #salary_estimate
                    salary_estimate = driver.find_element_by_xpath('//*[@id="JDCol"]//span[@data-test="detailSalary"]').text
                except (NoSuchElementException,StaleElementReferenceException) as e:
                    salary_estimate = -1 #You need to set a "not found value. It's important."
                
                #try:
                    # rating
                 #   rating = driver.find_element_by_xpath('//*[@id="JDCol"]//span[@data-test="detailRating"]').text
                #except (NoSuchElementException,StaleElementReferenceException) as e:
                    #rating = -1 #You need to set a "not found value. It's important."
    
                #Printing for debugging
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    #print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))
                    print("Job Function: {}".format(job_function))
    
                #Going to the Company tab...
                #clicking on this:
                #<div class="tab" data-tab-type="overview"><span>Company</span></div>
                #time.sleep(1)
                
                #try:
                 #   try:
                  #      driver.find_element_by_xpath('.//div[@id="SerpFixedHeader"]//span[text()="Company"]').click()
                  #  except (NoSuchElementException,StaleElementReferenceException) as e:
                   #     pass
    
                    #try:
                     #   size = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Size"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   size = -1
    
                    #try:
                     #   founded = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Founded"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   founded = -1
    
                    #try:
                     #   type_of_ownership = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Type"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   type_of_ownership = -1
    
                    #try:                        
                     #   industry = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Industry"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   industry = -1
    
                    #try:
                     #   sector = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Sector"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   sector = -1
    
                    #try:                        
                     #   revenue = driver.find_element_by_xpath('.//div[@id="EmpBasicInfo"]//span[text()="Revenue"]//following-sibling::*').text
                    #except (NoSuchElementException,StaleElementReferenceException) as e:
                     #   revenue = -1
                        
    
                #except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                    #size = -1
                    #founded = -1
                    #type_of_ownership = -1
                    #industry = -1
                    #sector = -1
                    #revenue = -1
    
                    
                #if verbose:
                    
                    #print("Size: {}".format(size))
                    #print("Founded: {}".format(founded))
                    #print("Type of Ownership: {}".format(type_of_ownership))
                    #print("Industry: {}".format(industry))
                    #print("Sector: {}".format(sector))
                    #print("Revenue: {}".format(revenue))
                    # print("Headquarters: {}".format(headquarters))
                    # print("Competitors: {}".format(competitors))
                    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                    
                    
                if key == True:
                    num = num+1
                    jobs.append({"Job Title" : job_title,
                    "Searched Job Title" : keyword,
                    "Company Name" : company_name,
                    "Full Description" : full_description,
                    "Location" : location,
                    "Salary Estimate" : salary_estimate,
                    "Job Function" : job_function,
                    #"Job Description" : job_description,
                    #"Rating" : rating,            
                    #"Size" : size,
                    #"Founded" : founded,
                    #"Type of ownership" : type_of_ownership,
                    #"Industry" : industry,
                    #"Sector" : sector,
                    #"Revenue" : revenue,
                    "URL" : url})
                    
                    print("----- {0} {1} ----- Page {2}".format(num,keyword,pg))
    
                currentJoblist=currentJoblist+1 # increasing the count of the list of buttons clicked and saved
                
                if not (currentJoblist < listButtonsCount): # to check the list last button and to go to next page
                        pg=pg+1
                        currentJoblist = 0  # resetting the button list count for new page button's list
                        break
                        
    
            #Clicking on the "next page" button
            try:                
                # driver.find_element_by_xpath('.//li[@class="next"]//a').click()
                
                driver.find_element_by_xpath('//*[@id="FooterPageNav"]//a[@data-test="pagination-next"]').click()
                
            except (NoSuchElementException,StaleElementReferenceException) as e:
                print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                break

    driver.quit()
    
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.
