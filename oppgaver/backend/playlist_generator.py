from dataclasses import dataclass

from clients.cover_image_generator_client import CoverImageGeneratorClient
from clients.playlist_description_generator_client import PlaylistDescriptionGeneratorClient
import uuid

def image_cover_prompt(tracks: list[str]):
    s = ""
    for track in tracks:
        s += f"{track}, "
    # TODO: 2.3 Forbedre denne prompten slik at den genererer et relevant coverbilde basert på låtene i spillelisten
    # return f"""
    #     Given these tracks: {s} create a very smooth and abstract shape that represents the general
    #     vibe of the songs. The style should be similar to that of hypermodern graphic design, like AI
    #     logos.  
    # """
    return f"""
        Given these tracks: {s} create a word bubble with the most relevant music words (like genre, instruments, 
        feel, etc.).
    """


def description_prompt(tracks: list[str]):
    # TODO: 2.3 Forbedre denne prompten slik at den genererer en relevant beskrivelse basert på låtene i spillelisten
    s = ""
    for track in tracks:
        s += f"{track}, "
    # TODO: 2.3 Forbedre denne prompten slik at den genererer et relevant coverbilde basert på låtene i spillelisten
    # return f"""
    #     Given these tracks: {s} create a very smooth and abstract shape that represents the general
    #     vibe of the songs. The style should be similar to that of hypermodern graphic design, like AI
    #     logos.  
    # """
    return f"""
        Given these tracks: {s} create a poem about the songs.
    """


class CoverGenerator:
    def __init__(self):
        self.image_generation_client = CoverImageGeneratorClient()

    def generate_cover_image(self, track_names: list[str]):
        prompt = image_cover_prompt(track_names)
        imageUrl = self.image_generation_client.generate_image(prompt)
        return imageUrl
    


class DescriptionGenerator:
    def __init__(self):
        self.description_generation_client = PlaylistDescriptionGeneratorClient()
    
    def generate_description(self, track_names: list[str]):
        prompt = description_prompt(track_names)
        description = self.description_generation_client.generate_description(prompt)
        return description
