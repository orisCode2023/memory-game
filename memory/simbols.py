def generate_symbols(size: int):
    symbols = []
    for symbol in range(size // 2):
        symbols.append(symbol)
    symbols.extend(symbols)
    return symbols


     











