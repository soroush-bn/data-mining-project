from Crawler import Crawler

if __name__ == '__main__':
    Course_Page_Url = None
    University = None
    Abbreviation = None
    University_Homepage = None

    output_file = None
    course_count = 0

    crawler = Crawler()
    div=crawler.get_advance_search_mode()
    crawler.get_faculties(div)
