def __init__(self, num_cards):
    self.num_cards = num_cards
    self.cards = []
    self.symbols = ['Яблоко', 'Банан', 'Вишня', 'Собака', 'Слон', 'Лягушка', 'Гитара', 'Сердце', 'Мороженое', 'Лось',
                    'Ключ', 'Лимон']
    self.generate_cards()