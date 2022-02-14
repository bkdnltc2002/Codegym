class Node:
    def __init__(self,dataval=None):
        #tạo một nút của dslk trỏ tới None = Null
        #Vừa khởi tạo, vừa gán giá trị cho dataval, nextval (datavalue,nextvalue)
        #next value chứa địa chỉ của nút tiếp theo
        self.dataval = dataval
        self.nextval = None
class SlinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        #Duyệt từ đầu đến cuối danh sách liên kết
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        # self = danh sách liên kết
        NewNode = Node(newdata)
        # cập nhật nút mới tới nút đã có
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtTheEnd(self, newdata):
        NewNode = Node(newdata)
        # xét trường hợp danh sách rỗng
        if self.headval is None:  # trỏ vô null
            self.headval = NewNode
            return
        laste = self.headval
        # duyet danh sach == laste.nextval is not None
        while (laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def RemoveNode(self, RemoveKey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == RemoveKey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None
if __name__ == "__main__":
    list1 = SlinkedList()
    list1.headval = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    #Lien kết nút đầu tiên tới nút thứ hai
    list1.headval.nextval = e2
    e2.nextval = e3
    list1.listprint()