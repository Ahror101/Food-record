import uuid


class Product:
    def __init__(self, name, price, quantity):
        self.id = str(uuid.uuid4())  # Har bir mahsulot uchun UUID
        self.name = name
        self.price = price
        self.quantity = quantity

    def info(self):
        return f"ID: {self.id}, Mahsulot nomi: {self.name}, Narxi: {self.price}, Miqdori: {self.quantity}"

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
        return f"{super().info()}, Garantiya: {self.warranty} yil"


class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def info(self):
        return f"{super().info()}, Yaroqlilik muddati: {self.expiration_date}"

    def sell(self, amount):
        if self.expiration_date < "2022-01-28":
            return "Xatolik: mahsulot muddati o'tgan!"
        return super().sell(amount)


class Basket:
    def __init__(self):
        self.items = []  # Lug‘at emas, ro‘yxat bo‘lishi kerak!

    def add(self, product, quantity):
        if product.quantity >= quantity:
            product.sell(quantity)
            item_id = str(uuid.uuid4())  # Har bir savat elementi uchun UUID
            self.items.append({"id": item_id, "product": product, "quantity": quantity})  # Lug‘at ichida saqlash
            return f"{quantity}ta {product.name} (ID: {item_id}) savatga qo‘shildi."
        return f"Omborda yetarli {product.name} yo‘q!"

    def remove(self, item_id):
        for item in self.items:
            if item["id"] == item_id:
                item["product"].restock(item["quantity"])
                self.items.remove(item)
                return f"ID: {item_id} bo‘lgan mahsulot savatdan olib tashlandi."
        return f"ID: {item_id} bo‘lgan mahsulot savatda topilmadi."

    def calc(self):
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def show(self):
        if not self.items:
            return "Savat bo‘sh!"
        return "\n".join([
                             f"ID: {item['id']} - {item['product'].name} - {item['quantity']}ta - {item['product'].price * item['quantity']}$"
                             for item in self.items])

    def clear(self):
        for item in self.items:
            item["product"].restock(item["quantity"])
        self.items = []
        return "Savatcha tozalandi!"

    def update_quantity(self, item_id, new_quantity):
        for item in self.items:
            if item["id"] == item_id:
                product = item["product"]
                old_quantity = item["quantity"]

                if new_quantity > old_quantity:  # Qo'shish kerak
                    diff = new_quantity - old_quantity
                    if product.quantity >= diff:
                        product.sell(diff)
                        item["quantity"] = new_quantity
                        return f"ID: {item_id} bo‘lgan mahsulot miqdori {new_quantity} taga yangilandi."
                    return f"Omborda yetarli {product.name} yo‘q!"
                elif new_quantity < old_quantity:  # Kamaytirish kerak
                    diff = old_quantity - new_quantity
                    product.restock(diff)
                    item["quantity"] = new_quantity
                    return f"ID: {item_id} bo‘lgan mahsulot miqdori {new_quantity} taga yangilandi."
        return f"ID: {item_id} bo‘lgan mahsulot savatda topilmadi!"


samsung = Electronics("Samsung", 1350, 10, 2)
apple = Food("Olma", 2, 50, "2025-01-01")
milk = Food("Sut", 5, 20, "2023-12-01")

basket = Basket()
samsung_add = basket.add(samsung, 2)
samsung_id = samsung_add.split("ID: ")[-1].split(")")[0]

apple_add = basket.add(apple, 5)
apple_id = apple_add.split("ID: ")[-1].split(")")[0]

print(basket.show())

print(basket.update_quantity(samsung_id, 3))
print(basket.update_quantity(apple_id, 2))
print(basket.clear())
print(basket.show())
