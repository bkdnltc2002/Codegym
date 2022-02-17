def enQueue(self, item):
    if self.size >= self.limit:
        print('Hang doi đầy')
        return
    else:
        self.que.append(item)
    if self.front is None:
        self.front = self.rear = 0
    else:
        self.rear = self.size
    self.size += 1
    print('Hang doi sau khi them vao la')
    print(self.que)


# phương thức lấy một phần tử trong hàng đợi ra
def deQueue(self):
    if self.size <= 0:
        print('Hang doi rong')
        return 0
    else:
        # pop(0): lay thang dau
        self.que.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        else:
            self.rear = self.size - 1
        print('Hang doi sau khi lay gia tri la')
        print(self.que)


def size(self):
    return self.size


class Queue(object):
    # Định nghĩa phương thức khởi tạo của hàng đợi
    def __init__(self, limit=5):
        # vừa khai báo và vừa gán giá trị
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    # phương thức kiểm tra hàng đợi có rỗng hay không
    def isEmpty(self):
        return self.size <= 0

    # phương thức thêm một phần tử vào hàng đợi Queue
    def enQueue(self, item):
        if self.size >= self.limit:
            print('Hang doi đầy')
            return
        else:
            self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print('Hang doi sau khi them vao la')
        print(self.que)

    # phương thức lấy một phần tử trong hàng đợi ra
    def deQueue(self):
        if self.size <= 0:
            print('Hang doi rong')
            return 0
        else:
            # pop(0): lay thang dau
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print('Hang doi sau khi lay gia tri la')
            print(self.que)

    def size(self):
        return self.size