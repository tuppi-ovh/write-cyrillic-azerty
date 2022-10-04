import curses
import time

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    alt = 0
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        # position
        y, x = stdscr.getyx()
        # switch case on key id
        if c == -1:
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
              0xc58b: 'ж',
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
              0xc2a2   : 'ч',
              0x77: 'ш',
              0xc2bb   : 'щ',
              0xb9: 'ь',
              0x79: 'ы',
              0x2a: 'ъ',
              0xac: 'э',
              0xe28693 : 'ю',
              0xc3a6   : 'я',
              # А...Я
              0x41: 'А',
              0x42: 'Б',
              0x44: 'Д',
              0x45: 'Е',
              0x4b: 'К',
              0x50: 'П',
              0xc386: 'Я',
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
              0x29: ')',
              0x3a: ':',
              0x2f: '/',
              0x2e: '.',
              0x2c: ',',
              0x3f: '?',
            }
            # switch-case on  code  
            char = switch.get(alt * 256 + c, "alt")
            # decide if print or alt  
            if char == "alt":
                alt = 256 * alt + c
                #print("(c={} alt={})".format(hex(c), hex(alt)))
            else: 
                stdscr.insstr(char)
                stdscr.move(y, x + 1)
                alt = 0

        # refresh
        stdscr.refresh()
        # sleep to relax cpu
        time.sleep(0.01)

if __name__ == '__main__':
    curses.wrapper(main)
