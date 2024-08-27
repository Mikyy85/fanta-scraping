from typing import List
import pandas as pd
import requests
from bs4 import BeautifulSoup

def import_excel_data(file, year:str):
    ids: List[int]= _read_excel_and_get_ids(file)
    _retrieve_player_data(ids, year )
    


def _read_excel_and_get_ids(file) -> List[int]:
    try:
        # Read the Excel file, skipping the first row
        df = pd.read_excel(file, header=1)  # Set header=1 to skip the first row

        # Filter only the "Id" column
        if 'Id' in df.columns:  # Ensure the column name matches exactly
            ids = df['Id'].tolist()  # Get the list of IDs
            return ids
        else:
            raise ValueError("Column 'Id' not found in the file.")
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")

def _retrieve_player_data(ids:List[int], year:str):
    BASE_URL = 'https://www.fantacalcio.it/serie-a/squadre/-/-/'
    for id in ids:

        url = f"{BASE_URL}{id}/{year}"
        
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the player name
            player_name_element = soup.find('h1', class_='player-name')

            # Check if the element was found
            if player_name_element:
                # Extract the text from the element
                player_name = player_name_element.get_text(strip=True)
            else:
                continue

            # Find the <a> tag with the class "team-name team-link"
            team_link = soup.find('a', class_='team-name team-link')

            # Extract the team name
            if team_link:
                team_name = team_link.get_text(strip=True)  # This will get the text inside the <a> tag
                print(team_name) 

            # Extract MV (Media Voto)
            mv_element = soup.find('li', title='Media Voto')
            if mv_element:
                mv_value = mv_element.find('span', class_='badge').get_text(strip=True)
            else:
                mv_value = None

            # Extract FM (Fantamedia)
            fm_element = soup.find('li', title='Fantamedia')
            if fm_element:
                fm_value = fm_element.find('span', class_='badge').get_text(strip=True)
            else:
                fm_value = None



