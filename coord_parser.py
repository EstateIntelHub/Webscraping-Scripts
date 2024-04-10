def format_to_google_maps_link(url):
    # Splitting the URL to find 'lat/' and 'lon/'
    parts = url.split('/')
    latitude = longitude = None

    for i, part in enumerate(parts):
        if part == 'lat' and i + 1 < len(parts):
            latitude = parts[i + 1]
        elif part == 'lon' and i + 1 < len(parts):
            longitude = parts[i + 1]

    if latitude and longitude:
        # Constructing the Google Maps link
        return f"https://www.google.com/maps/@{latitude},{longitude},17.75z"
    else:
        return "Unable to extract coordinates from the URL"

# Example URL
input_url = "https://harta.imobiliare.ro/layout/detaliiofertanew/id/X1BR101K1/init/1/lat/45.7446858/lon/21.2397909/loc/12224/of_lat/45.7446858/of_lon/21.2397909/numepunct/VGltaSYjMzUxO29hcmEsIHpvbmEgQ29tcGxleCBTdHVkZW4mIzM1NTtlc2M"

# Running the function
formatted_link = format_to_google_maps_link(input_url)
formatted_link


print(formatted_link)