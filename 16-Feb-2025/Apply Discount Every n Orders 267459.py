# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.product_price = {product:prices[i] for i,product in enumerate(products)}
        self.customer_count = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        item_prices = [self.product_price[item]*amount[i] for i,item in enumerate(product)]
        total = sum(item_prices)
        if self.customer_count % self.n == 0:
            total -= total * self.discount /100

        self.customer_count +=1
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)