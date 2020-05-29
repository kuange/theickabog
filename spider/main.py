from requests_html import HTMLSession
import pexpect
import os


def run():
    session = HTMLSession()
    r = session.get('https://www.theickabog.com/king-fred-the-fearless/')
    r.encoding = 'utf-8'

    lists_obj = r.html.find("ul.chapters__list li")
    for i in range(len(lists_obj)):
        a_obj = lists_obj[i].find("a", first=True)
        h2 = a_obj.find("h2", first=True).text
        h3 = a_obj.find("h3", first=True).text

        url_list = list(lists_obj[i].find("a", first=True).absolute_links)
        print(h3, h2, url_list[0])
        detail(session, h3, h2, url_list[0])


def detail(session, h3, h2, url):
    old_h3 = h3
    h3 = h3.replace(" ", "-").lower()
    pwd = os.getcwd()
    print(pwd)

    md_filepath = pwd + "/../md/english"
    md_fileList = os.listdir(md_filepath)

    if h3 + ".md" not in md_fileList:
        r = session.get(url)
        r.encoding = 'utf-8'
        detail_content = r.html.find("div.entry-content", first=True).text

        detail_content = "---\r\npageClass: bg-class\r\n---\r\n\r\n" + \
            ("# %s %s \r\n\r\n" % (old_h3, h2)) + detail_content

        filename = pwd + "/../md/english/" + h3 + ".md"
        print(filename)

        with open(filename, 'w+') as fw:
            fw.write(detail_content)
        print("done ", h3)

        with open(md_filepath + "/README.md", 'a+') as fw:
            str = "- [%s - %s](%s.html) \r\n" % (old_h3, h2, h3)
            fw.write(str)
        print("done %s a+" % h3)


run()
