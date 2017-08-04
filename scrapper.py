from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import os

fileName = 'noen.txt'

def main(i):
    base = webdriver.PhantomJS('phantomjs')
    base.get('http://bputexam.in/studentsection/resultpublished/studentresult.aspx')

    base.find_element_by_id('dpStudentdob_dateInput').send_keys('4/4/2010')
    base.find_element_by_id('txtRegNo').send_keys(str(i))

    select = Select(base.find_element_by_id('ddlSession'))
    select.select_by_visible_text('Odd (2016-17)')

    base.find_element_by_id('btnView').click()

    try:
        result_links = base.find_elements_by_link_text('View Result')
        link = result_links[-1]
        link.click()

        exam = base.find_element_by_id('lblResultName')
        exam = exam.text.split(',')[-1].strip()

        name = base.find_element_by_id('lblName')
        name = name.text.title()
        soup = BeautifulSoup(base.page_source, 'lxml')
        data = []
        table = soup.find('table', attrs={'id':'gvViewResult'})
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        print(exam, '-', name)

        if os.path.exists(fileName):
            write_append = 'a'
        else:
            write_append = 'w'

        fopen = open(fileName, write_append)
        fopen.write(name)
        fopen.write("\n")
        fopen.write(str(data))
        fopen.write('\n\n')
        fopen.close()

        base.quit()

    except Exception as e:
        print("Excpetion occured : ", e)
        base.quit()
