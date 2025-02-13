
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
        data += f", garantiya: {self.warranty}yil"
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
        if self.expiration_date < "2025-02-11":  
            return "Xatolik: mahsulot muddati o'tgan!"
        return super().sell(amount)


laptop = Electronics("Laptop", 1200, 10, 2)
print(laptop.info())

apple = Food("Olma", 2, 50, "2025-01-01")
print(apple.info())
print(apple.sell(5))

milk = Food("Sut", 5, 20, "2023-12-01")
print(milk.sell(2)) 
