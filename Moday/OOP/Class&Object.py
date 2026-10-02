
# ================================= 5. Class and Object =================================

# ១. ការបង្កើត Class (ពុម្ពមេ)
class Phone:
    # មុខងារកំណត់លក្ខណៈសម្បត្តិដំបូង
    def __init__(self, brand, color):
        self.brand = brand  # លក្ខណៈសម្បត្តិ (Attribute)
        self.color = color  # លក្ខណៈសម្បត្តិ (Attribute)

    # សកម្មភាព (Method)
    def ring(self):
        print(f"ទូរស័ព្ទម៉ាក {self.brand} កំពុងរោទ៍... ឡូឡាៗ!")

# ២. ការបង្កើត Objects (វត្ថុពិតដែលផលិតចេញពី Class Phone)
phone1 = Phone("iPhone", "ពណ៌ខ្មៅ")
phone2 = Phone("Samsung", "ពណ៌ប្រាក់")

# ៣. ការហៅទិន្នន័យ និងសកម្មភាពមកប្រើប្រាស់
print(phone1.brand)
print(phone2.color)

phone1.ring()
