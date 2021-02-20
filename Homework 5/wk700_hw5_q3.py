class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    def __str__(self):
        x = ''
        for i in range(len(self.data)):
            x += str(self.data[i])
            x += ' '
        return x
    def __repr__(self):
        return str(self.data)

def calculate(input, d):
    s = ArrayStack()
    count = 0
    while count < len(input):
        elem = input[count]
        if elem == '':
            continue
        if elem.isdigit():
            s.push(int(elem))
        elif elem == '+'and s.top()!='=':
            if len(s) > 1:
                one = s.pop()
                two = s.pop()
                if str(one).isalpha():
                    one = d[str(one)]
                if str(two).isalpha():
                    two = d[str(two)]
                s.push(one+ two)
            else:
                raise ExceptionError('Not a valid expression')
        elif elem == '-'and s.top()!='=':
            if len(s) > 1:
                one = s.pop()
                two = s.pop()
                if str(one).isalpha():
                    one = d[str(one)]
                if str(two).isalpha():
                    two = d[str(two)]
                s.push(two - one)
            else:
                raise ExceptionError('Not a valid expression')
        elif elem == '*'and s.top()!='=':
            if len(s) > 1:
                one = s.pop()
                two = s.pop()
                if str(one).isalpha():
                    u = str(one)
                    one = d[u]
                if str(two).isalpha():
                    w = str(two)
                    two = d[w]
                s.push(one*two)
            else:
                raise ExceptionError('Not a valid expression')
        elif elem == '/':
            if len(s) > 1 and s.top()!='=':
                one = s.pop()
                two = s.pop()
                if str(one).isalpha():
                    one = d[str(one)]
                if str(two).isalpha():
                    two = d[str(two)]
                s.push(two / one)
            else:
                raise ExceptionError('Not a valid expression')
        elif elem.isalpha():
            s.push(elem)
        elif elem == '=':
            s.push(elem)
        count += 1

    if len(s) > 1:
        num = s.pop()
        t = s.pop()
        var = s.pop()
        d[var] = num
        s.push( var)
    return s







def main():
    x = input('-->')
    d = dict()
    while x != 'done()':
        print(calculate(x, d))
        x = input('-->')

main()
