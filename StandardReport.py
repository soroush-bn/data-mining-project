from time import sleep
from random import randint
from Crawler import Crawler
if __name__ == '__main__':
    Course_Page_Url = None
    University = None
    Abbreviation = None
    University_Homepage = None
    output_file = None

    course_count = 0

    crawler = Crawler()
    crawler.search()
    while(True):
        crawler.select_all_courses()
        sleep(randint(2,7))
        crawler.download_standard_report()
        sleep(randint(5,12))
        crawler.go_to_next_page()
