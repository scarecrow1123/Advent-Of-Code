class Tape:
    def __init__(self):
        self.__stretch_factor = 50
        self.__buf = []
        self.__buf_len = 0
        self.__left_head = 0
        self.__right_head = 0
        self.current_position = 0 
        self.__stretch_tape()
    
    def __stretch_tape(self):
        e = self.__stretch_factor/2
        self.__buf = [0]*e + self.__buf[:] + [0]*e
        self.__buf_len += self.__stretch_factor
        self.current_position += e 

    def peek(self):
        return self.__buf[self.current_position]

    def right(self):
        if self.current_position == self.__buf_len:
            self.__stretch_tape()
        self.current_position += 1
        self.__right_head = self.current_position

    def left(self):
        if self.current_position == 0:
            self.__stretch_tape()
        self.current_position -= 1
        self.__left_head = self.current_position

    def checksum(self):
        return self.__buf.count(1)

    def write(self, value):
        self.__buf[self.current_position] = value

    def show(self):
        print self.__buf

class Machine:
    def __init__(self, tape, table):
        self.__state = 'A'
        self.__tape = tape
        self.__transition_table = table
        self.__move_fn = {
            'left': self.__tape.left,
            'right': self.__tape.right
        }
        self.__tape.left()
        self.__move_fn['right']()

    def __transition(self, *args):
        if len(args[0]) == 3:
            self.__tape.write(args[0][0])
            (self.__move_fn[args[0][1]])()
            self.__state = args[0][2]

    def __step(self):
        cur_val  = self.__tape.peek()
        self.__transition(self.__transition_table[self.__state][cur_val])

    def run(self, count):
        for i in range(count):
            if i % 1000 == 0:
                print i
            self.__step()
            #self.__tape.show()

class Parser:
    def __init__(self, text):
        self.lines = text.splitlines()
        self.__len_lines = len(self.lines)
        self.start = None
        self.step_count = None
        self.transition_table = {}
        self.parse()

    def parse(self):
        self.begin(0)
        self.count(1)
        self.state(3)

    def begin(self, line_number):
        self.start = self.lines[line_number][-2]    
        self.count(line_number+1)

    def count(self, line_number):
        self.step_count = int(self.lines[line_number].split(' ')[-2])
        self.state(line_number+2)

    def state(self, line_number):
        if line_number >= self.__len_lines:
            return None

        source = self.lines[line_number][-2]
        self.transition_table[source] = {}

        def helper(line_number):

            def curr():
                c = int(self.lines[line_number+1][-2])
                self.transition_table[source][c] = []
                write(c)

            def write(c):
                w = int(self.lines[line_number+2][-2])
                self.transition_table[source][c].append(w)
                move(c,w)

            def move(c, w):
                m = self.lines[line_number+3].split(' ')[-1][:-1]
                self.transition_table[source][c].append(m)
                nxt(c, w, m)

            def nxt(c, w, m):
                n = self.lines[line_number+4].split(' ')[-1][0]
                self.transition_table[source][c].append(n)
            
            curr()
        helper(line_number)
        helper(line_number+4)
        self.state(line_number+10)

with open('input.txt') as inputfile:
    txt = inputfile.read()
    parser = Parser(txt)
    tape = Tape()
    machine = Machine(tape, parser.transition_table)
    machine.run(parser.step_count)
    print tape.checksum()
