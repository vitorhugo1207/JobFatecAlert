from requests import get
from subprocess import STARTUPINFO, STARTF_USESHOWWINDOW, Popen
from filecmp import cmp

url = 'https://www.fateclins.edu.br/web/oportunidades'

def getDoom():
    try:
        fatecJobDoom = get(url)
        with open('./fatecJob2.html', 'wt') as w:
            w.write(fatecJobDoom.text)
    except:
        return 'HTTP Error'
    return fatecJobDoom.text

def saveFile(fatecJobDoom):
    with open('./fatecJob.html', 'wt') as w:
        w.write(fatecJobDoom)

def openFile():
    with open('./fatecJob.html', 'rt') as r:
        return r.read()

def compareFile():
    result = cmp("./fatecJob.html", "./fatecJob2.html")

    if (result):
        return f"There's not new Jobs on Fatec Web page!\n\n{url}"
    else:
        return f"There's new Jobs on Fatec Web page!\n\n{url}"

def notification(comparationResponse):
    with open('./Fatec Job Alert.txt', 'w') as w:
        w.write(comparationResponse)

    info = STARTUPINFO()
    info.dwFlags = STARTF_USESHOWWINDOW
    info.wShowWindow = 6
    Popen('notepad ./Fatec Job Alert.txt', startupinfo=info)

if __name__ == '__main__':
    fatecJobDoom = getDoom()
    if(fatecJobDoom == 'HTTP Error'):
        notification(fatecJobDoom)
        exit()
        
    comparationResponse = compareFile()
    notification(comparationResponse)
    saveFile(fatecJobDoom)
