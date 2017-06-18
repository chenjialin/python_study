import re
import os
import urllib, urllib2
import requests
import chardet
from multiprocessing.dummy import Pool


def urllink(link):
    html_1 = urllib2.urlopen(link, timeout=120).read()
    encoding_dict = chardet.detect(html_1)
    web_encoding = encoding_dict['encoding']
    if web_encoding in ('utf-8', 'UTF-8'):
        html = html_1
    else:
        html = html_1.decode('gbk', 'ignore').encode('utf-8')

    return html
# <img src="http://image.51xiqu.com/ligui/02220901.jpg"

if __name__ == "__main__":
    page = 9
    image_url_list = []
    cur_path = os.getcwd()
    for i in range(1, page + 1):
        link = "http://www.dazui88.com/tag/ligui/list_78_%s.html" % i
        # print 'link: ', link
        html = urllink(link)
        # print 'html: ', html
        plist = re.findall(r"<p>.*?</p>", html, re.S)
        p_par = ' '.join(plist)
        image_urls = re.findall(r'<img\ssrc="(?P<pic_url>.*?)"', p_par)
        image_url_list.extend(image_urls)
    n = 0
    for url in image_url_list:
        if 'http' not in url:
            continue
        n += 1
        try:
            pic = requests.get(url, stream=True)
            print 'Download image %s ...' % url
            img_path = os.path.join(cur_path, 'images/%s.jpg' % n)
            print 'img_path: ', img_path
            img_obj = open(img_path, 'wb')
            for content in pic.iter_content(chunk_size=1024*8):
                if content:
                    img_obj.write(content)
                    img_obj.flush()
            img_obj.close()
        except Exception, e:
            print 'Error: ' + str(e)
