class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        span = 1

        while stack and stack[-1][0] <= price:
            _, new_span = stack.pop()
            span += new_span
        
        stack.append((price, span))
        return span