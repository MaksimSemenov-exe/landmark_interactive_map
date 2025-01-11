import folium
import geopandas
import json

geojson_path = r'C:\Users\arefb\PycharmProjects\landmark_interactive_map\landmark_interactive_map\Russia_regions.geojson'

with open('landmarks.json', 'r', encoding='utf-8') as file:
    cities = json.load(file)

def create_start_map(geojson: str) -> folium.Map:
    gdf = geopandas.read_file(geojson)
    visual_map = folium.Map([55.7558, 37.6173], zoom_start=10)
    folium.GeoJson(gdf, zoom_on_click=True).add_to(visual_map)
    return visual_map

def cities_landmarks_processing(cities_dict: dict, visual: folium.Map) -> folium.Map:
    for city, city_data in cities_dict.items():
        # Добавление метки для города
        cords = city_data['Координаты']
        folium.Marker(
            cords,
            icon=folium.DivIcon(html=f"""<div style="font-size: 12px; color: black;">{city}</div>""")
        ).add_to(visual)

        # Добавление меток для достопримечательностей
        for landmark, landmark_data in city_data["Достопримечательности"].items():
            folium.Marker(
                landmark_data['Координаты'],
                popup=folium.Popup(landmark_data['Краткое описание'], max_width=300),
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(visual)

    return visual

visual_map = create_start_map(geojson_path)

visual_map = cities_landmarks_processing(cities, visual_map)

visual_map.show_in_browser()
