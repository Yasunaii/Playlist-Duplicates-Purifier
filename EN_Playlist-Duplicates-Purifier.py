import json
import os
from collections import defaultdict
from fuzzywuzzy import fuzz
from tqdm import tqdm
import multiprocessing as mp
from itertools import combinations
import string

def process_chunk(args):
    """
    Processes a group of track comparisons.
    This function is called by each process in the process pool.
    """
    chunk, confirmed_threshold, suspected_threshold = args
    local_confirmed = defaultdict(list)
    local_suspected = []

    for track, compare_track in chunk:
        track_isrc = track.get("isrc")
        compare_isrc = compare_track.get("isrc")
 
        # ISRC verification
        if track_isrc and compare_isrc and track_isrc == compare_isrc:
            local_confirmed[track_isrc].append((track, compare_track))
            continue

        # Similarity check
        track_name = track['name'].strip()
        compare_name = compare_track['name'].strip()

        # Ignore titles that are too short or made up entirely of special characters, unless they are exactly the same
        if (len(track_name) < 3 or len(compare_name) < 3 or all(c in string.punctuation for c in track_name) or all(c in string.punctuation for c in compare_name)) and track_name != compare_name:
            continue

        name_similarity = fuzz.token_sort_ratio(track_name, compare_name)

        # Ignore titles with a similarity below the threshold
        if name_similarity < suspected_threshold:
            continue

        track_artist = track['artist'].strip().lower()
        compare_artist = compare_track['artist'].strip().lower()
        artist_similarity = fuzz.token_sort_ratio(track_artist, compare_artist)

        # Ignore artists with similarity below threshold
        if artist_similarity < 85:
            continue

        album_similarity = fuzz.token_sort_ratio(track['album_name'], compare_track['album_name'])

        local_suspected.append((track, compare_track, name_similarity, artist_similarity, album_similarity))

    return local_confirmed, local_suspected

def chunked_combinations(iterable, chunk_size=1000):
    """Divides combinations into groups for parallel processing"""
    all_combos = list(combinations(iterable, 2))
    for i in range(0, len(all_combos), chunk_size):
        yield all_combos[i:i + chunk_size]

def write_results(output_file_path, confirmed_duplicates, suspected_duplicates):
    """Writes results to a file in the new format"""
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # En-tête et disclaimer général
        output_file.write('=== Duplicate Detection Results ===\n\n')

        # Section des doublons confirmés avec disclaimer
        output_file.write('ISRC Confirmed Doubles:\n')
        output_file.write('!!! Although the titles are different, both tracks share the same ISRC number.\n')
        output_file.write('! The ISRC (International Standard Recording Code) is a unique identifier for each audio recording. ')
        output_file.write('It helps to spot and eliminate exact duplicates in playlists, as each official version of a song has a distinct code\n\n')

        # Liste des doublons confirmés
        for isrc, instances in confirmed_duplicates.items():
            for track, compare_track in instances:
                output_file.write(f'Title 1: {track["name"]} | Artist 1: {track["artist"]} | Album 1: {track["album_name"]}\n')
                output_file.write(f'Title 2: {compare_track["name"]} | Artist 2: {compare_track["artist"]} | Album 2: {compare_track["album_name"]}\n\n')

        # Section des doublons potentiels
        output_file.write('Potentials Duplicates:\n\n')
        output_file.write('!!! Please note: These potential duplicates may not actually be duplicates. ')
        output_file.write('To be 100%, sure we recommend manually checking each pair of potential duplicates.\n\n')
        for track, compare_track, name_similarity, artist_similarity, album_similarity in suspected_duplicates:
            output_file.write(f'Title 1: {track["name"]} | Artist 1: {track["artist"]} | Album 1: {track["album_name"]}\n')
            output_file.write(f'Title 2: {compare_track["name"]} | Artist 2: {compare_track["artist"]} | Album 2: {compare_track["album_name"]} '
                            f'(Similitude: {name_similarity}%, Artiste Similarité: {artist_similarity}%, Album Similarité: {album_similarity}%)\n\n')


def find_duplicates(json_file_path, output_file_path, confirmed_threshold=85, suspected_threshold=90, chunk_size=1000):
    """Fonction principale de détection des doublons"""
    print("Chargement du fichier JSON...")
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    tracks = data['tracks']

    print(f"Nombre total de pistes : {len(tracks)}")

    # Préparation des chunks pour le traitement parallèle
    chunks = list(chunked_combinations(tracks, chunk_size))
    total_chunks = len(chunks)

    print(f"Démarrage de l'analyse des doublons...")

    # Initialisation des résultats
    confirmed_duplicates = defaultdict(list)
    suspected_duplicates = []

    # Préparation des arguments pour le processing
    chunk_args = [(chunk, confirmed_threshold, suspected_threshold) for chunk in chunks]

    # Utilisation du Pool de processus avec tqdm
    with mp.Pool(processes=mp.cpu_count()) as pool:
        results = []
        for result in tqdm(pool.imap_unordered(process_chunk, chunk_args),
                          total=total_chunks,
                          desc="Analyse des pistes"):
            local_confirmed, local_suspected = result
            # Mise à jour des résultats
            for isrc, dupes in local_confirmed.items():
                confirmed_duplicates[isrc].extend(dupes)
            suspected_duplicates.extend(local_suspected)

    print("\nÉcriture des résultats...")
    write_results(output_file_path, confirmed_duplicates, suspected_duplicates)

    # Affichage des statistiques finales
    print(f"\nAnalyse terminée :")
    print(f"- Nombre de doublons confirmés : {sum(len(dupes) for dupes in confirmed_duplicates.values())}")
    print(f"- Nombre de doublons potentiels : {len(suspected_duplicates)}")

    return confirmed_duplicates, suspected_duplicates

if __name__ == "__main__":
    json_file_path = 'C:\\Users\\sammy\\Downloads\\test\\Apple_Poat.json'
    output_file_path = 'C:\\Users\\sammy\\Downloads\\test\\Duplicates_List.txt'

    try:
        find_duplicates(json_file_path, output_file_path)
    except KeyboardInterrupt:
        print("\nInterruption manuelle du script.")
    except Exception as e:
        print(f"\nUne erreur s'est produite : {str(e)}")