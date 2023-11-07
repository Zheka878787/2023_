def generate_cards(self):
    num_symbols_per_card = self.num_cards + 1
    for _ in range(self.num_cards):
        symbols = random.sample(self.symbols, num_symbols_per_card)
        self.cards.append(DobbleCard(symbols))