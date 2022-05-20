from time import sleep

from Crawler import Crawler
if __name__ == '__main__':
    Course_Page_Url = None
    University = None
    Abbreviation = None
    University_Homepage = None

    output_file = None
    course_count = 0

    crawler = Crawler()
    crawler.get_advance_search_mode()
    faculty_options,faculty_names=crawler.get_faculties()
    # crawler.select_faculty(faculty_options,faculty_names[2])
    # crawler.search()
    # first way to obtain data
    # for fn in faculty_names:
    #     crawler.select_faculty(faculty_options,fn)
    #     crawler.search()
    #     crawler.select_all_courses()
    #     crawler.download_standard_report()
    #     sleep(7)

    #second way :
    course_trs,title_trs=crawler.get_courses_of_department("Faculty of Law")
    for i in range(0,len(course_trs)):
        course_trs, title_trs = crawler.get_courses_of_department("Faculty of Law")
        crawler.get_course_data(course_trs[i])
        sleep(5)
        print("course number "+str(i)+" done ")