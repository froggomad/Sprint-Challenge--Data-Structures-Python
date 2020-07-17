class RingBuffer:
    def __init__(self, max_value):
        self.pointer = 0
        self.max_value = max_value
        self.storage = []

    def get(self):
        return self.storage

    def append(self, value):
        if len(self.storage) < self.max_value:
            self.storage.append(value)
        else:
            if self.pointer == self.max_value:
                self.pointer = 0
            self.storage[self.pointer] = value
            self.pointer += 1


buffer = RingBuffer(3)

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())

buffer.append('d')
buffer.append('e')
buffer.append('f')

print(buffer.get())