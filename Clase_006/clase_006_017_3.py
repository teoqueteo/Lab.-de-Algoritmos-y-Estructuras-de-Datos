lugares_favoritos = {
    'Juan': ['Paris', 'Roma', 'Tokio'],
    'Sara': ['Barcelona', 'Londres', 'Bali'],
    'Eduardo': ['Nueva York', 'Los Ángeles', 'Chicago']}
for persona, lugares in lugares_favoritos.items():
    lugares_str = ', '.join(lugares)
    print(f"{persona} tiene como lugares favoritos: {lugares_str}.")