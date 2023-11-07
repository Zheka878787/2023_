def play(self):
    print("--- Dobble Game ---")
    for i, card in enumerate(self.cards):
        print(f"Карта {i + 1}: {card.symbols}")

    print("\nНайдите совпадающий символ!")
    symbol_to_match = random.choice(self.symbols)
    print(f"\nСимвол для поиска совпадений: {symbol_to_match}")

    matches = []
    for i, card in enumerate(self.cards):
        if symbol_to_match in card.symbols:
            matches.append(i + 1)

    if len(matches) > 0:
        print("Поздравляем! Вы нашли совпадения на следующих картах:")
        for match in matches:
            print(f"Карта {match}")
    else:
        print("Извините, совпадения не найдены.")