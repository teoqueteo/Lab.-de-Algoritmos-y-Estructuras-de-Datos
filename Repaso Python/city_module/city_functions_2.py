def city_country(city, country, population=None):
    """Devuelve una cadena con formato 'Ciudad, País – población xxx' si se proporciona population."""
    if population:
        return f"{city.title()}, {country.title()} – población {population}"
    else:
        return f"{city.title()}, {country.title()}"