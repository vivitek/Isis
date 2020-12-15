from bs4 import BeautifulSoup
import requests
import sys

def main():
    file = open('site.txt', "r")
    types = open('liste.txt', "r")
    doc = open('data.csv', "w")
    line = file.readline()
    ty = types.readline()

    while line:
        line = line.replace('\n', '/')
        ty = ty.replace('\n', '')
        try:
                r = requests.get(line)
                soup = BeautifulSoup(r.content, "html.parser")
                meta = soup.find_all('meta')

                for tag in meta:
                        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
                                print(line)
                                doc.write('"' + line + '"' + ",")
                                doc.write('"' + tag.attrs['content'] + '"' + ",")
                                doc.write('"' + ty + '"' + "\n")
                line = file.readline()
                ty = types.readline()
        except:
                line = file.readline()
                ty = types.readline()
                
    file.close()
    types.close()
    doc.close()

if __name__ == '__main__':
    main()