class MinStack:

    def __init__(self):
        # Основной стек для хранения всех значений
        self.stack = []
        # Вспомогательный стек для хранения минимальных значений
        self.min_stack = []
        

    def push(self, value: int) -> None:
        # Добавляем значение в основной стек
        self.stack.append(value)
        
        # Если min_stack пуст или новое значение меньше/равно текущего минимума
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            # Иначе дублируем текущий минимум
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        # Удаляем из обоих стеков
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        # Возвращаем верхний элемент основного стека
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        # Возвращаем верхний элемент min_stack (текущий минимум)
        if self.min_stack:
            return self.min_stack[-1]
        return None



        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()