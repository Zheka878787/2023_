import random


class DobbleCard:
    def __init__(self, symbols):
        self.symbols = symbols

    def __repr__(self):
        return f'DobbleCard({self.symbols})'


class DobbleGame:
    def __init__(self, num_cards):
        self.num_cards = num_cards
        self.cards = []
        self.symbols = ['Яблоко', 'Банан', 'Вишня', 'Собака', 'Слон', 'Лягушка', 'Гитара', 'Сердце', 'Мороженое', 'Лось',
                        'Ключ', 'Лимон']
        self.generate_cards()

    def generate_cards(self):
        num_symbols_per_card = self.num_cards + 1
        for _ in range(self.num_cards):
            symbols = random.sample(self.symbols, num_symbols_per_card)
            self.cards.append(DobbleCard(symbols))

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


# Создание игры и запуск
game = DobbleGame(5)
game.play()