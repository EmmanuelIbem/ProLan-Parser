class DFA:
    current_state = None
    def __init__(self, states, token, transition_function, start_state, accept_states):
        self.states = states
        self.token = token
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state
        return
    
    def transition_to_state_with_input(self, input_value):
        if ((self.current_state, input_value) not in self.transition_function.keys()):
            self.current_state = None
            return
        self.current_state = self.transition_function[(self.current_state, input_value)]
        return
    
    def in_accept_state(self):
        return self.current_state in accept_states
    
    def go_to_initial_state(self):
        self.current_state = self.start_state
        return
    
    def scan(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            continue
        return self.in_accept_state()
    pass



states = {1,'div',3,4,5,'lparen','rparen','plus','minus','times',11,'assign',13,'number','number2','id'}
token = {'a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        '\n','\s','\t',
        '0','1','2','3','4','5','6','7','8','9',
        '*','+','-','(',')',':','=','.','/'}

tf = dict()
tf[(1, '\s')] = 1
tf[(1, '\t')] = 1
tf[(1, '\n')] = 1
tf[(1, '/')] = 'div'
tf[(1, '(')] = 'lparen'
tf[(1, ')')] = 'rparen'
tf[(1, '+')] = 'plus'
tf[(1, '-')] = 'minus'
tf[(1, '*')] = 'times'
tf[(1, ':')] = 11
tf[(1, '.')] = 13
tf[(1, '0')] = 'number'
tf[(1, '1')] = 'number'
tf[(1, '2')] = 'number'
tf[(1, '3')] = 'number'
tf[(1, '4')] = 'number'
tf[(1, '5')] = 'number'
tf[(1, '6')] = 'number'
tf[(1, '7')] = 'number'
tf[(1, '8')] = 'number'
tf[(1, '9')] = 'number'
tf[(1, 'a')] = 'id'
tf[(1, 'b')] = 'id'
tf[(1, 'c')] = 'id'
tf[(1, 'd')] = 'id'
tf[(1, 'e')] = 'id'
tf[(1, 'f')] = 'id'
tf[(1, 'g')] = 'id'
tf[(1, 'h')] = 'id'
tf[(1, 'i')] = 'id'
tf[(1, 'j')] = 'id'
tf[(1, 'k')] = 'id'
tf[(1, 'l')] = 'id'
tf[(1, 'm')] = 'id'
tf[(1, 'n')] = 'id'
tf[(1, 'o')] = 'id'
tf[(1, 'p')] = 'id'
tf[(1, 'q')] = 'id'
tf[(1, 'r')] = 'id'
tf[(1, 's')] = 'id'
tf[(1, 't')] = 'id'
tf[(1, 'u')] = 'id'
tf[(1, 'v')] = 'id'
tf[(1, 'w')] = 'id'
tf[(1, 'x')] = 'id'
tf[(1, 'y')] = 'id'
tf[(1, 'z')] = 'id'
tf[('div', '/')] = 3
tf[('div', '*')] = 4
tf[(3, '\n')] = 1
tf[(3, '\s')] = 3
tf[(3, '\t')] = 3
tf[(3, '0')] = 3
tf[(3, '1')] = 3
tf[(3, '2')] = 3
tf[(3, '3')] = 3
tf[(3, '4')] = 3
tf[(3, '5')] = 3
tf[(3, '6')] = 3
tf[(3, '7')] = 3
tf[(3, '8')] = 3
tf[(3, '9')] = 3
tf[(3, 'a')] = 3
tf[(3, 'b')] = 3
tf[(3, 'c')] = 3
tf[(3, 'd')] = 3
tf[(3, 'e')] = 3
tf[(3, 'f')] = 3
tf[(3, 'g')] = 3
tf[(3, 'h')] = 3
tf[(3, 'i')] = 3
tf[(3, 'j')] = 3
tf[(3, 'k')] = 3
tf[(3, 'l')] = 3
tf[(3, 'm')] = 3
tf[(3, 'n')] = 3
tf[(3, 'o')] = 3
tf[(3, 'p')] = 3
tf[(3, 'q')] = 3
tf[(3, 'r')] = 3
tf[(3, 's')] = 3
tf[(3, 't')] = 3
tf[(3, 'u')] = 3
tf[(3, 'v')] = 3
tf[(3, 'w')] = 3
tf[(3, 'x')] = 3
tf[(3, 'y')] = 3
tf[(3, 'z')] = 3
tf[(3, '/')] = 3
tf[(3, '(')] = 3
tf[(3, ')')] = 3
tf[(3, '+')] = 3
tf[(3, '-')] = 3
tf[(3, '*')] = 3
tf[(3, ':')] = 3
tf[(3, '.')] = 3
tf[(3, '=')] = 3
tf[(4, '*')] = 5
tf[(4, '\n')] = 4
tf[(4, '\s')] = 4
tf[(4, '\t')] = 4
tf[(4, '0')] = 4
tf[(4, '1')] = 4
tf[(4, '2')] = 4
tf[(4, '3')] = 4
tf[(4, '4')] = 4
tf[(4, '5')] = 4
tf[(4, '6')] = 4
tf[(4, '7')] = 4
tf[(4, '8')] = 4
tf[(4, '9')] = 4
tf[(4, 'a')] = 4
tf[(4, 'b')] = 4
tf[(4, 'c')] = 4
tf[(4, 'd')] = 4
tf[(4, 'e')] = 4
tf[(4, 'f')] = 4
tf[(4, 'g')] = 4
tf[(4, 'h')] = 4
tf[(4, 'i')] = 4
tf[(4, 'j')] = 4
tf[(4, 'k')] = 4
tf[(4, 'l')] = 4
tf[(4, 'm')] = 4
tf[(4, 'n')] = 4
tf[(4, 'o')] = 4
tf[(4, 'p')] = 4
tf[(4, 'q')] = 4
tf[(4, 'r')] = 4
tf[(4, 's')] = 4
tf[(4, 't')] = 4
tf[(4, 'u')] = 4
tf[(4, 'v')] = 4
tf[(4, 'w')] = 4
tf[(4, 'x')] = 4
tf[(4, 'y')] = 4
tf[(4, 'z')] = 4
tf[(4, '*')] = 4
tf[(4, '+')] = 4
tf[(4, '-')] = 4
tf[(4, '(')] = 4
tf[(4, ')')] = 4
tf[(4, ':')] = 4
tf[(4, '=')] = 4
tf[(4, '.')] = 4
tf[(4, '/')] = 4
tf[(5, '*')] = 5
tf[(5, '/')] = 1
tf[(5, '+')] = 4
tf[(5, '-')] = 4
tf[(5, '(')] = 4
tf[(5, ')')] = 4
tf[(5, ':')] = 4
tf[(5, '=')] = 4
tf[(5, '.')] = 4
tf[(5, '0')] = 4
tf[(5, '1')] = 4
tf[(5, '2')] = 4
tf[(5, '3')] = 4
tf[(5, '4')] = 4
tf[(5, '5')] = 4
tf[(5, '6')] = 4
tf[(5, '7')] = 4
tf[(5, '8')] = 4
tf[(5, '9')] = 4
tf[(5, 'a')] = 4
tf[(5, 'b')] = 4
tf[(5, 'c')] = 4
tf[(5, 'd')] = 4
tf[(5, 'e')] = 4
tf[(5, 'f')] = 4
tf[(5, 'g')] = 4
tf[(5, 'h')] = 4
tf[(5, 'i')] = 4
tf[(5, 'j')] = 4
tf[(5, 'k')] = 4
tf[(5, 'l')] = 4
tf[(5, 'm')] = 4
tf[(5, 'n')] = 4
tf[(5, 'o')] = 4
tf[(5, 'p')] = 4
tf[(5, 'q')] = 4
tf[(5, 'r')] = 4
tf[(5, 's')] = 4
tf[(5, 't')] = 4
tf[(5, 'u')] = 4
tf[(5, 'v')] = 4
tf[(5, 'w')] = 4
tf[(5, 'x')] = 4
tf[(5, 'y')] = 4
tf[(5, 'z')] = 4
tf[(5, '\n')] = 4
tf[(5, '\s')] = 4
tf[(5, '\t')] = 4
tf[(11, '=')] = 'assign'
tf[(13, '0')] = 'number2'
tf[(13, '1')] = 'number2'
tf[(13, '2')] = 'number2'
tf[(13, '3')] = 'number2'
tf[(13, '4')] = 'number2'
tf[(13, '5')] = 'number2'
tf[(13, '6')] = 'number2'
tf[(13, '7')] = 'number2'
tf[(13, '8')] = 'number2'
tf[(13, '9')] = 'number2'
tf[('number', '0')] = 'number'
tf[('number', '1')] = 'number'
tf[('number', '2')] = 'number'
tf[('number', '3')] = 'number'
tf[('number', '4')] = 'number'
tf[('number', '5')] = 'number'
tf[('number', '6')] = 'number'
tf[('number', '7')] = 'number'
tf[('number', '8')] = 'number'
tf[('number', '9')] = 'number'
tf[('number', '0')] = 'number2'
tf[('number', '1')] = 'number2'
tf[('number', '2')] = 'number2'
tf[('number', '3')] = 'number2'
tf[('number', '4')] = 'number2'
tf[('number', '5')] = 'number2'
tf[('number', '6')] = 'number2'
tf[('number', '7')] = 'number2'
tf[('number', '8')] = 'number2'
tf[('number', '9')] = 'number2'
tf[('number2', '0')] = 'number2'
tf[('number2', '1')] = 'number2'
tf[('number2', '2')] = 'number2'
tf[('number2', '3')] = 'number2'
tf[('number2', '4')] = 'number2'
tf[('number2', '5')] = 'number2'
tf[('number2', '6')] = 'number2'
tf[('number2', '7')] = 'number2'
tf[('number2', '8')] = 'number2'
tf[('number2', '9')] = 'number2'
tf[('id', 'a')] = 'id'
tf[('id', 'b')] = 'id'
tf[('id', 'c')] = 'id'
tf[('id', 'd')] = 'id'
tf[('id', 'e')] = 'id'
tf[('id', 'f')] = 'id'
tf[('id', 'g')] = 'id'
tf[('id', 'h')] = 'id'
tf[('id', 'i')] = 'id'
tf[('id', 'j')] = 'id'
tf[('id', 'k')] = 'id'
tf[('id', 'l')] = 'id'
tf[('id', 'm')] = 'id'
tf[('id', 'n')] = 'id'
tf[('id', 'o')] = 'id'
tf[('id', 'p')] = 'id'
tf[('id', 'q')] = 'id'
tf[('id', 'r')] = 'id'
tf[('id', 's')] = 'id'
tf[('id', 't')] = 'id'
tf[('id', 'u')] = 'id'
tf[('id', 'v')] = 'id'
tf[('id', 'w')] = 'id'
tf[('id', 'x')] = 'id'
tf[('id', 'y')] = 'id'
tf[('id', 'z')] = 'id'
tf[('id', '0')] = 'id'
tf[('id', '1')] = 'id'
tf[('id', '2')] = 'id'
tf[('id', '3')] = 'id'
tf[('id', '4')] = 'id'
tf[('id', '5')] = 'id'
tf[('id', '6')] = 'id'
tf[('id', '7')] = 'id'
tf[('id', '8')] = 'id'
tf[('id', '9')] = 'id'
start_state = 1
accept_states = {1,'div',3,4,5,'lparen','rparen','plus','minus','times',11,'assign',13,'number','number','id'}

d = DFA(states, token, tf, start_state, accept_states)

inp_program = list('5')

print (d.scan(inp_program))




