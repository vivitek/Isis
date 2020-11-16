from bs4 import BeautifulSoup
import requests
import sys

def main():
    file = open('site.txt', "r")
    line = file.readline()
    
    while line:
        line = line.replace('\n', '/')
        try:
                r = requests.get(line)
                print(line)
                soup = BeautifulSoup(r.content, "html.parser")
                meta = soup.find_all('meta')

                for tag in meta:
                        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
                                print(tag.attrs['content'])
                                write = open("data.txt", "a")
                                line = line.replace('/', '\n')
                                write.write(line)
                                write.write(tag.attrs['content'])
                                write.write("\n")
                                write.close()
                line = file.readline()
        except:
                line = file.readline()

    file.close()

if __name__ == '__main__':
    main()