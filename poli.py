class Product:
    def __init__(self, name, price, quantity):
        self.name = name  
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"Mahsulot nomi: {self.name}, Narxi: {self.price}, Miqdori: {self.quantity}"

    def sell(self, amount):
        if amount > self.quantity:
            return f"Siz {amount}ta mahsulot so'radingiz, lekin omborda {self.quantity}ta bor."
        else:
            self.quantity -= amount
            return f"{amount}ta mahsulot sotildi. Omborda {self.quantity}ta qoldi."

    def restock(self, amount):
        self.quantity += amount
        return f"Omborga {amount}ta mahsulot qo'shildi. Yangi miqdor: {self.quantity}"


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f", Garantiya: {self.warranty} yil"
        return data


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date  

    def info(self):
        data = super().info()
        data += f", Yaroqlilik muddati: {self.expiration_date}"
        return data
    
    def sell(self, amount):
        if self.expiration_date < "2022-01-28":  
            return "Xatolik: mahsulot muddati o'tgan!"
        return super().sell(amount)


class Basket:
    def __init__(self):
        self.items = []

    def add(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append((product, quantity))
            product.sell(quantity)
            return f"{quantity}ta {product.name} savatga qo‘shildi."
        return f"Omborda yetarli {product.name} yo‘q!"

    def remove(self, product_name):
        for i, (product, quantity) in enumerate(self.items):
            if product.name == product_name:
                product.restock(quantity)
                del self.items[i]
                return f"{product_name} savatdan olib tashlandi."
        return f"{product_name} savatda topilmadi."

    def calc(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def show(self):
        if not self.items:
            return "Savat bo‘sh!"
        return "\n".join([f"{product.name} - {quantity}ta - {product.price * quantity}$" for product, quantity in self.items])

samsung = Electronics("Samsung", 1350, 10, 2)
apple = Food("Olma", 2, 50, "2025-01-01")
milk = Food("Sut", 5, 20, "2023-12-01")


basket = Basket()
print(basket.add(samsung, 2))
print(basket.add(apple, 5))
print(basket.show())
print(f"Umumiy narx: {basket.calc()}$")
print(basket.remove("Samsung"))
print(basket.show())
