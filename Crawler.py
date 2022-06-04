import csv

from BaseCrawler import BaseCrawler
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from random import randint

class Crawler(BaseCrawler):
    page = None

    Course_Page_Url = "https://www.ksl.unibe.ch/KSL/veranstaltungen?1/"
    University = "University of Bern"
    Abbreviation = "UoB"
    University_Homepage = "https://www.unibe.ch/index_eng.html"
    university = "None"
    abbreviation = "None"
    department_name = "None"
    course_title = "None"
    unit_count = "None"
    professor = "None"
    objective = "None"
    prerequisite = "None"
    required_skills = "None"
    outcome = "None"
    references = "None"
    scores = "None"
    description = "None"
    projects = "None"
    university_homepage = "None"
    course_homepage = "None"
    professor_homepage = "None"
    page_number = 1
    mode = "all" #it can be advance tho

    def __init__(self):
        self.output_file = csv.writer(open(f'data/{self.__class__.__name__}.csv', 'w', encoding='utf-8', newline=''))
        self.output_file.writerow(
            ['University', 'Abbreviation', 'Department', 'Course title', 'Unit', 'Professor', 'Objective',
             'Prerequisite', 'Required Skills', 'Outcome', 'References', 'Scores', 'Description', 'Projects',
             'University Homepage', 'Course Homepage', 'Professor Homepage']
        )
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
        advance_radio_btn = self.page.find_element(By.ID, "id2-1")
        advance_radio_btn.click()
        sleep(.5)

    def get_faculties(self):
        try:
            myElem = WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.ID, 'id2b')))
        except TimeoutException:
            print("\n could not load page properly please retry.")
        div_for_entry_fields = self.page.find_element(By.ID, "id2b")
        entry_lis = div_for_entry_fields.find_elements(By.TAG_NAME, "li")
        sleep(1)
        faculty_select_tag = div_for_entry_fields.find_element(By.ID, "id28")
        sleep(1)
        faculty_options = faculty_select_tag.find_elements(By.TAG_NAME, "option")
        sleep(1)
        print(faculty_options)
        faculty_names = []
        for f in faculty_options:
            faculty_names.append(f.text)
        return faculty_options, faculty_names

    def select_faculty(self, faculty_options, faculty_name):
        for faculty in faculty_options:
            if (faculty.text == faculty_name):
                faculty.click()
        sleep(1)
        return

    def search(self):
        try :
            self.page.find_element(By.ID, "id29").click()
        except:
            self.page.find_element(By.ID, "id5").click()
        sleep(1)

    def __setup_driver(self):
        chromedriver_path = ".//chromedriver.exe"
        opt = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")
        prefs = {"profile.managed_default_content_settings.images": 2}
        self.page = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opt)

    def get_titles(self):
        pass

    def get_courses_of_department(self, department):
        super().get_courses_of_department(department)
        self.get_advance_search_mode()
        faculty_options, faculty_names = self.get_faculties()
        self.select_faculty(faculty_options, department)
        self.search()
        try:
            myElem = WebDriverWait(self.page, 10).until(
                EC.presence_of_element_located((By.ID, 'EventsManagementTable')))
        except TimeoutException:
            print("\n could not load EventsManagementTable properly please retry.")

        table = self.page.find_element(By.ID, "EventsManagementTable")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        thead = table.find_element(By.TAG_NAME, "thead")
        titles_tr = thead.find_elements(By.TAG_NAME, "tr")
        course_trs = tbody.find_elements(By.TAG_NAME, "tr")
        return course_trs, titles_tr

    def go_to_course_detail(self, course_tr, ):
        try:
            myElem = WebDriverWait(course_tr, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'td')))
            print("find that")
        except TimeoutException:
            print("\n could not go to course details please retry.")
        tds = course_tr.find_elements(By.TAG_NAME, "td")
        links = tds[-1].find_elements(By.TAG_NAME, "a")
        links[1].click()

    def select_all_courses(self):
        if(self.mode=="advance"):
            try:
                myElem = WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.ID, 'id30')))
                print("all courses are selected")
            except TimeoutException:
                print("\n could not click on select all please retry.")
            self.page.find_element(By.ID, "id30").click()
        else:
            try:
                myElem = WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.ID, 'id25')))
                print("all courses are selected")
            except TimeoutException:
                print("\n could not click on select all please retry.")
            self.page.find_element(By.ID, "id25").click()

        sleep(randint(1,3))

    def download_standard_report(self):
        try:
            myElem = WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.ID, 'berichtLink')))
            print(".... downloading standard report")
        except TimeoutException:
            print("\n could not click on berichtLink  please retry.")
        # self.page.find_element(By.ID,"berichtLink").click()
        self.page.execute_script('document.querySelector("#berichtLink").click()')
        sleep(2)

    def get_course_data(self, course):
        super().get_course_data(course)
        print(course)
        print("_---------------")
        self.go_to_course_detail(course_tr=course)
        sleep(1)
        try:
            myElem = WebDriverWait(self.page, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'table')))
        except TimeoutException:
            print("\n could not load table properly please retry.")
            self.page.back()
            return

        table = self.page.find_element(By.TAG_NAME, "table")
        tbody = table.find_element(By.TAG_NAME, "tbody")
        trs = tbody.find_elements(By.TAG_NAME, "tr")
        print("len of all trs = " + str(trs.__len__()))
        for tr in trs:
            try:
                tds = tr.find_elements(By.TAG_NAME, "td")
                if tds[1].text == "Title":
                    self.course_title = tds[2].text
                elif tds[1].text == "Unit Count":
                    self.unit_count = tds[2].text
                elif tds[1].text == "Description":
                    self.description = tds[2].text
                elif tds[1].text == "Learning outcome":
                    self.outcome = tds[2].text
                elif tds[1].text == "ILIAS-Link (Learning resource for course)":
                    self.references = tds[2].text
                elif tds[1].text == "Lecturer":
                    self.professor = tds[2].text
                elif tds[1].text == "Name of catalogue of learning objectives":
                    self.objective = tds[2].text
                elif tds[1].text == "Grading":
                    self.scores = tds[2].text
                elif tds[1].text == "Learning outcome":
                    self.outcome = tds[2].text
                elif tds[1].text == "Allocation to subject":
                    self.department_name = tds[2].text
            except:
                continue

        self.save_course_data(self.University, self.abbreviation, self.department_name, self.course_title,
                              self.unit_count, self.professor, self.objective, self.prerequisite, self.required_skills
                              , self.outcome, self.references, self.scores, self.description, self.projects
                              , self.University_Homepage, self.page.current_url, self.professor_homepage)
        sleep(2)
        self.page.back()

    def save_course_data(self, university, abbreviation, department_name, course_title, unit_count, professor,
                         objective, prerequisite, required_skills, outcome, references, scores, description, projects,
                         university_homepage, course_homepage, professor_homepage):
        super().save_course_data(university, abbreviation, department_name, course_title, unit_count, professor,
                                 objective, prerequisite, required_skills, outcome, references, scores, description,
                                 projects, university_homepage, course_homepage, professor_homepage)

    def handler(self):
        super().handler()

    def go_to_next_page(self):
        self.page.get(
            'https://www.ksl.unibe.ch/KSL/veranstaltungen?0-1.-veranstaltungenForm-ergebnisContainer-navigator_top-navigation-' +
            str(self.page_number) + '-pageLink&1/')
        self.page_number+=1
        print("going to next page ...")
        sleep(randint(10,15))

