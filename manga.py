import requests
from bs4 import BeautifulSoup
import os
#!pip install img2pdf
import img2pdf
import shutil

chapter = 'chapter-'
# for one peice
url = 'https://ww6.mangakakalot.tv/chapter/manga-jn986670/chapter-'
# for the begining after the end
#url = 'https://ww8.mangakakalot.tv/chapter/manga-dg980989/chapter-'

def convertImagesToPdf(folder):
    print(os.getcwd())
    image_files = [i for i in os.listdir(os.getcwd()) if i.endswith(".jpg")]
    print(image_files)
    pdf_data = img2pdf.convert(image_files)
    os.chdir('..')
    os.chdir(os.path.join(os.getcwd(),"pdf"))
    with open(folder+".pdf", "wb") as file:
      file.write(pdf_data)
    os.chdir('..')

def downloadManga(url,folder):
    os.mkdir(os.path.join(os.getcwd(),folder))
    os.chdir(os.path.join(os.getcwd(),folder))
    r = requests.get(url)
    soup = BeautifulSoup(r.text , 'html.parser')
    print(soup.title.text)
    images = soup.find_all('img')
    for image in images:
        try:
          name = image['title']
        except:
          name = "un"
        try:
          link = image['src']
        except:
          link = image['data-src']
        if link[:24] == 'https://cm.blazefast.co/':
          print(link)
          with open(name + '.jpg','wb') as f:
            im = requests.get(link)
            f.write(im.content)

    print("Completed downloading .... ",folder)
    convertImagesToPdf(folder)

def deleteDirectory():
    os.chdir('..')
    print(os.getcwd())
    shutil.rmtree(os.path.join(os.getcwd(),"chapter-734"))

for i in range(500, 600):
   downloadManga(url+str(i),chapter+str(i))
   print(os.getcwd())
#convertImagesToPdf()
#deleteDirectory()
#os.mkdir(os.path.join(os.getcwd(),"pdf"))
