import os

def openFile():
    try:
        os.system('start firefox.exe')
        os.system('code')

    except Exception: 
        print(str(e))


if __name__ == "__main__":
    openFile()

