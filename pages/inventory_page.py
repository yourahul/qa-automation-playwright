class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_item_to_cart(self):
        self.page.click("button[id='add-to-cart-sauce-labs-backpack']")

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()
