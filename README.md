# Selenium Python POM Hybrid Framework Project with Behave BDD

Hybrid Custom Framework to Test YourStore Web App with Behave BDD



### Tech Stack
1. Python 3.11
2. Behave - BDD
3. PyTest - Testing Framework
4. Reporting - Allure Report
5. Test Data - Using feature file


### How to Install Packages
`` pip install selenium webdriver-manager behave allure-behave pytest-html faker 
``

### To Freeze your Package version
`` pip freeze > requirements.txt ``

## To Install te Freeze Version
``pip install -r requirements.txt``


``behave -s .\features\ -f allure_behave.formatter::AllureFormatter -o reports/your_store_allure_test_report
``


### How to run via Jenkins(CI/CD)


• Create job - Select freestyle project template
• In SCM section select 'Git' option
• Provide github project repo url 
• Add github credentials 
• In 'Build' section select 'custom python builder'
• In 'Home' section add  python.exe location from local machine
• In 'Nature' section mention Shell
• In command section write commands
	> Python -m venv env
	> call .venv/Scripts/activate.bat
	> pip install selenium
	> pip install webdriver-manager
	> pip install behave
	> pip install allure-behave
	> behave features --tags=run
	-f allure_behave.formatter::AllureFormatter 
	-o reports/project_allure_report
	
• In 'Post Build Actions' give report path in Allure Report section
	> Reports\project_allure_report

