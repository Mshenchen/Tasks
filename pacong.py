import requests
import re
import os

images = '表情包'
if not os.path.exists(images):
    os.mkdir(images)


def download(name, url):
    response = requests.get(url)
    print(response.status_code)
    suffix = url.split('.')[-1]
    try:
        with open(images+'/' + name+'.'+suffix, mode='wb') as file:
            file.write(response.content)
    except:
        print('保存失败', name+'.'+suffix)


def download_page(url_one_page):
    response = requests.get(url_one_page)
    print(response.text)
    re_temp = '<img class="ui image lazy" data-original="(.*?)" src="/Public/lazyload/img/transparent.gif" title="(.*?)" alt=".*" style="max-height:188;margin: 0 auto"/>'
    result = re.findall(re_temp, response.text)
    print(result)
    for img in result:
        print(img)
        download(img[1], img[0])


for page in range(1, 3):
    pages = ('https://fabiaoqing.com/biaoqing/lists/page/'+str(page)+'.html')
    download_page(pages)
# download_page('https://fabiaoqing.com/biaoqing/lists/page/1.html')
