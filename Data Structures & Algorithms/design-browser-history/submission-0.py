class new_node:
    def __init__(self,url:str):
        self.next = self.prev = None
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = new_node(homepage)
        self.tail = new_node("dummy")
        self.tail.prev = self.homepage
        self.homepage.next = self.tail
        self.curr = self.homepage
    
    def add_after_curr(self,node):
        node.next = self.tail
        node.prev = self.curr
        node.next.prev = node
        node.prev.next = node
        self.curr = node

    def visit(self, url: str) -> None:
        node = new_node(url)
        self.add_after_curr(node)

    def back(self, steps: int) -> str:
            while self.curr.prev and steps :
                self.curr = self.curr.prev
                steps = steps - 1
            return self.curr.url

    def forward(self, steps: int) -> str:
            while self.curr.next.next and steps :
                self.curr = self.curr.next
                steps = steps - 1
            return self.curr.url     


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)