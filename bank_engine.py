import json
import sys
import os

def update_balance(card_num, amount):
    # Загружаем текущую базу
    with open('bank.json', 'r') as f:
        data = json.load(f)
    
    if card_num in data['cards']:
        data['cards'][card_num]['balance'] += int(amount)
        
        # Сохраняем обратно
        with open('bank.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"✅ Баланс карты {card_num} пополнен на {amount}!")
    else:
        print("❌ Карта не найдена")

if __name__ == "__main__":
    # Получаем данные из аргументов GitHub Actions
    card = sys.argv[1]
    money = sys.argv[2]
    update_balance(card, money)
