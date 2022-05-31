import curses
import time

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    # remember keys
    offset = 0
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()

        if c == -1:
            pass
        # alt
        elif c == 0xe2:
            pass
        elif c == 0x82:
            pass
        elif c == 0xc2:
            pass
        elif c == 0xc3:
            pass
        else:
            # convert to cyrillic
            switch={
              0x61: 'а',
              0x62: 'б',
              0x76: 'в',
              0x67: 'г',
              0x64: 'д',
              0x65: 'е',
              0xa6: 'ж',
              0x7a: 'з',
              0x69: 'и',
              0x6a: 'й',
              0x6b: 'к',
              0x6c: 'л',
              0x6d: 'м',
              0x6e: 'н',
              0x6f: 'о',
              0x70: 'п',
              0x72: 'р',
              0x73: 'с',
              0x74: 'т',
              0x75: 'у',
              0x66: 'ф',
              0x68: 'х',
              0x63: 'ц',
              0xa9: 'ч',
              0xb9: 'ь',
              0x79: 'ы',
              0x2a: 'ъ',
              0xac: 'э',
              0xbb: 'ю',
              0xa2: 'я'
            }
            char = switch.get(offset * 256 + c, str(hex(c)))
            # print
            stdscr.addstr(char + ' ')
            stdscr.refresh()
            # reset special char
            offset = 0

        # sleep to relax cpu
        time.sleep(0.01)

if __name__ == '__main__':
    curses.wrapper(main)