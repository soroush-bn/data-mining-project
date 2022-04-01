from BaseCrawler import BaseCrawler
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Crawler(BaseCrawler):
    page = None

    Course_Page_Url = "https://www.ksl.unibe.ch/KSL/veranstaltungen?1/"
    University = "University of Bern"
    Abbreviation = "UoB"
    University_Homepage = "https://www.unibe.ch/index_eng.html"

    # Below fields didn't find in the website
    Prerequisite = None
    References = None
    Scores = None
    Projects = None
    Professor_Homepage = None


    def __init__(self):
        self.__setup_driver()
        self.load_search_page()


    def load_search_page(self):
        self.page.get("https://www.ksl.unibe.ch/KSL/veranstaltungen?1")
        try:
            myElem = WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.ID, 'veranstaltungenPage')))
            print("--------  page loaded ----------- \n")
        except TimeoutException:
            print("\n could not load page properly please retry.")
        sleep(.5)

    def get_advance_search_mode(self):

        advance_radio_btn=self.page.find_element(By.ID,"id2-1")
        advance_radio_btn.click()
        sleep(.5)
        div_for_entry_fields=self.page.find_element(By.ID,"id2b")

        return div_for_entry_fields

    def get_faculties(self,start_point):
        entry_lis = start_point.find_elements(By.TAG_NAME, "li")
        print(entry_lis)
        sleep(1)
        faculty_select_tag = start_point.find_element(By.ID, "id28")
        sleep(1)
        faculty_options = faculty_select_tag.find_elements(By.TAG_NAME, "option")
        sleep(1)
        print(faculty_options)

    def __setup_driver(self):
        chromedriver_path = ".//chromedriver.exe"
        opt = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.page = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opt)



    def get_courses_of_department(self, department):
        super().get_courses_of_department(department)

    def get_course_data(self, course):
        super().get_course_data(course)

    def save_course_data(self, university, abbreviation, department_name, course_title, unit_count, professor,
                         objective, prerequisite, required_skills, outcome, references, scores, description, projects,
                         university_homepage, course_homepage, professor_homepage):
        super().save_course_data(university, abbreviation, department_name, course_title, unit_count, professor,
                                 objective, prerequisite, required_skills, outcome, references, scores, description,
                                 projects, university_homepage, course_homepage, professor_homepage)

    def handler(self):
        super().handler()
