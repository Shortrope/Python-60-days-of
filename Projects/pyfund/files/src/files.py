#!/venv/bin/python3
import sys

def main():
    try:
        f = open('wasteland.txt', mode='wt', encoding='utf-8')

        f.write('Mindset, The New Psychology of Success\n')
        f.write('Through clever research studies and engaging writing.\n')
        f.write('How we learn and which paths we take in life.\n')
    finally:
        f.close()

    try:
        g = open('wasteland.txt', mode='rt', encoding='utf-8')
        print(g.read(), end='')
        print(g.seek(0))
        sys.stdout.write(g.read())
        print('------------------')
        print(g.seek(0))
        print(g.readline(), end='')
        print(g.readline(), end='')
        print(g.seek(0))
        print(g.readline(), end='')
        print(g.seek(0))
        print('------------------')
        print(g.readlines(), end='')
    finally:
        g.close()

if __name__ == '__main__':
    main()