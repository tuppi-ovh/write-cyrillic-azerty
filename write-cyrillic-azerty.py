import curses
import time

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        # position
        y, x = stdscr.getyx()
        # switch case on key id
        if c == -1:
            pass
        # alt
        elif c in (0xe2, 0x82, 0xc2, 0xc3):
            pass
        # unused
        elif c in (0x71, 0x78):
            pass
        # left
        elif c == 0x104:
            stdscr.move(y, max(0, x - 1))
        # up
        elif c == 0x103:
            stdscr.move(max(0, y - 1), x)
        # down
        elif c == 0x102:
            stdscr.move(y + 1, x)
        # right
        elif c == 0x105:
            stdscr.move(y, x + 1)
        # backspace
        elif c == 0x107:
            stdscr.addstr('\x08')
            stdscr.delch()
        # delete
        elif c == 0x14a:
            stdscr.delch()
        # new line
        elif c == 0x0a:
            stdscr.move(y + 1, 0)
        # other cases
        else:
            # convert to cyrillic
            switch={
              # а...я
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
              0x77: 'ш',
              0xab: 'щ',
              0xb9: 'ь',
              0x79: 'ы',
              0x2a: 'ъ',
              0xac: 'э',
              0xbb: 'ю',
              0xa2: 'я',
              # А...Я
              0x41: 'А',
              0xa4: 'Я',
              # 0...9
              0x30: '0',
              0x31: '1',
              0x32: '2',
              0x33: '3',
              0x34: '4',
              0x35: '5',
              0x36: '6',
              0x37: '7',
              0x38: '8',
              0x39: '9',
              # special
              0x20: ' ',
              0x21: '!',
              0x3a: ':',
              0x2f: '/',
              0x2e: '.',
              0x2c: ',',
              0x3f: '?',
            }
            char = switch.get(c, str(hex(c)))
            stdscr.insstr(char)
            stdscr.move(y, x + 1)

        # refresh
        stdscr.refresh()
        # sleep to relax cpu
        time.sleep(0.01)

if __name__ == '__main__':
    curses.wrapper(main)