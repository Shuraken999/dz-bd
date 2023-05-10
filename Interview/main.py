class Stack(list):

    def __init__(self):
        self = self
    
    def is_empty(listack):
        if len(listack) == 0:
            return True
        else:
            return False

    def push(element, listack):
        listack.insert(0, element)
        

    def pop(listack):
        element = listack[0]
        listack.pop(0)
        return element
        
    def peek(listack):
        return listack[0]

    def size(listack):
        return len(listack)

    def balance(brackets):
        a = '('
        b = ')'
        c = '{'
        d = '}'
        e = '['
        f = ']'
        if Stack.size(brackets)%2 != 0:
                return print('Несбалансированно')
        if brackets.count(a) == brackets.count(b) and brackets.count(c) == brackets.count(d) and brackets.count(e) == brackets.count(f):
            return print('Cбалансированно')
        else:
            return print('Несбалансированно')
            
# Проверка методов из 1-го задания
tef = Stack()
print('Пустой стек: ', Stack.is_empty(tef))
tef = ['1','2']
print('Не пустой стек: ', Stack.is_empty(tef))
print('Стек до метода "push":', tef)
Stack.push('7', tef)
print('Стек после метода "push":', tef)
print(f'Применение метода "pop": {Stack.pop(tef)}, стек после метода "pop": {tef}')
print('Результат метода "peek":', Stack.peek(tef), 'стек после матода "peek":', tef)
print('Результат метода "size":', Stack.size(tef))
# Проверка решения 2-го задания
ter = Stack()                    
simboly = '[(((((({}))))))()]'
ter = list(simboly)
Stack.balance(ter)

        
        
        
        