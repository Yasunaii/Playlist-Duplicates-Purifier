# Playlist Duplicates Purifier

<details>
<summary>EN VERSION</summary>

## Description

The **Playlist Duplicates Purifier** is a Python script designed to detect duplicates within a music track collection. By leveraging both ISRC codes and the similarity of titles, artists, and albums, it identifies potential and confirmed duplicates effectively.

### Features

- **ISRC-Based Duplicate Detection**: Quickly identifies duplicates using the International Standard Recording Code (ISRC).
- **Similarity Analysis**: Evaluates the similarity of track titles, artists, and albums to spot duplicates that may not have matching ISRC codes.
- **Parallel Processing**: Optimizes performance through parallel processing, making it faster and more efficient.
- **Detailed Duplicate Report**: Generates a comprehensive report of all found duplicates for easy review.

## Prerequisites

- **Python**: Version 3.13 (ensure compatibility with other versions).
- **Streaming Subscription**: Requires an active subscription to Spotify or Apple Music.
- **Playlist Data**: You will need a JSON file containing your playlist data. Sign up on [Playlists Cloud](https://playlists.cloud/playlists/83e90de4-5858-4a03-bbd6-43578e45a0d4) and import your playlists. After importing, go to "Manage Playlist," select the playlist you wish to analyze, and click the purple download button on the right to "Export as JSON." Place this file in the folder you created.
- **Visual Studio Code**: Recommended for code editing and environment management.
- **Required Python Packages**: Install the following packages using pip:
    ```bash
    pip install colorama fuzzywuzzy Levenshtein python-Levenshtein RapidFuzz tqdm
    ```

### Installation

1. **Python Setup**:
   - Download and install Python from the [official website](https://www.python.org/).
   - During installation, check the box labeled **"Add Python to PATH"**.

2. **Visual Studio Code Setup**:
   - Download and install Visual Studio Code from the [official site](https://code.visualstudio.com/).

### Project Configuration

1. **Create Project Directory**:
   - Create a new folder on your computer for the project, e.g., `Playlist-Duplicates-Purifier.py`.

2. **Playlist Data**:
   - You will need a JSON file containing all the data. Sign up on [Playlists Cloud](https://playlists.cloud/playlists/83e90de4-5858-4a03-bbd6-43578e45a0d4) and import your playlists. Once done, go to "Manage Playlist," select the playlist you want to analyze, click the purple button on the right with the down arrow to "Export as JSON," and place the file in the folder you previously created.

3. **Open Folder in VS Code**:
   - Launch Visual Studio Code.
   - Navigate to **File > Open Folder** and select the newly created folder.

4. **Create Python File**:
   - In VS Code, create a new file named `dPlaylist-Duplicates-Purifier.py`.
   - Copy and paste the script code into this file.

5. **Set Up Virtual Environment and Install Dependencies**:
   - Open a new terminal in VS Code (Terminal > New Terminal).
   - Run the following command to install the required packages:
     ```bash
     pip install colorama fuzzywuzzy Levenshtein python-Levenshtein RapidFuzz tqdm
     ```
   - VS Code will detect the absence of a virtual environment and prompt you to create one. Click "Yes" to proceed.
   - This will automatically create a virtual environment within your project folder.

6. **Select Python Interpreter**:
   - Ensure that VS Code is using the new virtual environment. 
   - If it doesn't automatically detect it, press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS), type **"Python: Select Interpreter"**, and choose the newly created environment.

### Running the Script

To execute the script, follow these steps:

1. Verify that VS Code is using the virtual environment (check the bottom left corner of the VS Code window).
2. Open a new terminal in VS Code if one isn’t already open.
3. Run the script using the following command:

   ```bash
   python Playlist-Duplicates-Purifier.py
   ```

## Uninstalling
At the end of the process, you'll probably want to uninstall the following items: 
1. Uninstall python and Visual studio code from Windows settings like all other applications
If you uninstall in this way, the packages installed by pressing “pip install” will also be uninstalled.

</details>

<details>
<summary>FR VERSION</summary>

## Description

Le **Playlist Duplicates Purifier** est un script Python conçu pour détecter les doublons dans une collection de morceaux de musique. En exploitant les codes ISRC et la similarité des titres, des artistes et des albums, il identifie efficacement les doublons potentiels et confirmés.

### Caractéristiques

-  **Détection des doublons basée sur l'ISRC**: Identifie rapidement les doublons à l'aide de l'International Standard Recording Code (ISRC).
-  **Analyse de similarité**: Évalue la similitude des titres, des artistes et des albums pour repérer les doublons dont les codes ISRC ne correspondent pas.
-  **Traitement parallèle**: Optimise les performances grâce au traitement parallèle, ce qui le rend plus rapide et plus efficace.
-  **Rapport détaillé sur les doublons**: Génère un rapport complet de tous les doublons trouvés pour une vérification facile.

 
## Prérequis
- **Python**: Version 3.13 (assurer la compatibilité avec d'autres versions).
- **Abonnement au streaming**: Nécessite un abonnement actif à Spotify ou Apple Music.
-  **Données de la liste de lecture**: Vous aurez besoin d'un fichier JSON contenant les données de votre liste de lecture. Inscrivez-vous sur [Playlists Cloud](https://playlists.cloud/) et importez vos listes de lecture. Après l'importation, allez dans « Manage Playlist », sélectionnez la liste de lecture que vous souhaitez analyser et cliquez sur le bouton de téléchargement violet à droite pour « Export as JSON ». Placez ce fichier dans le dossier que vous avez créé.
-  **Visual Studio Code**: Recommandé pour l'édition de code et la gestion de l'environnement.
-  **Paquets Python requis**: Installez les paquets suivants à l'aide de pip :
    ```bash
    pip install colorama fuzzywuzzy Levenshtein python-Levenshtein RapidFuzz tqdm
    ```
### Installation
1. **Installation de Python**:
   - Téléchargez et installez Python à partir du [site web officiel](https://www.python.org/).
   - Pendant l'installation, cochez la case **"Add Python to PATH »**.
2. **Installation de Visual Studio Code**:
   - Téléchargez et installez Visual Studio Code à partir du [site officiel](https://code.visualstudio.com/).

 
### Configuration du projet
1. **Créer le répertoire du projet**:
   - Créez un nouveau dossier sur votre ordinateur pour le projet, par exemple, `Playlist-Duplicates-Purifier.py`.

2. **Données de la liste de lecture**:
   - Vous aurez besoin d'un fichier JSON contenant toutes les données. Inscrivez-vous sur [Playlists Cloud](https://playlists.cloud/playlists/83e90de4-5858-4a03-bbd6-43578e45a0d4) et importez vos listes de lecture. Une fois cela fait, allez dans « Manage Playlist », sélectionnez la liste de lecture que vous voulez analyser, cliquez sur le bouton violet à droite avec la flèche vers le bas pour « Export as JSON », et placez le fichier dans le dossier que vous avez précédemment créé.

 
3. **Ouvrir le dossier dans VS Code**:
   - Lancez Visual Studio Code.
   - Naviguez vers **Fichier > Ouvrir le dossier** et sélectionnez le dossier nouvellement créé.
4. **Créer un fichier Python**:
   - Dans VS Code, créez un nouveau fichier nommé `dPlaylist-Duplicates-Purifier.py`.
   - Copiez et collez le code du script dans ce fichier.
5. **Configurer l'environnement virtuel et installer les dépendances**:
   - Ouvrez un nouveau terminal dans VS Code (Terminal > New Terminal).
   - Exécutez la commande suivante pour installer les paquets nécessaires :
     ```bash
     pip install colorama fuzzywuzzy Levenshtein python-Levenshtein RapidFuzz tqdm
     ```
   - VS Code détectera l'absence d'environnement virtuel et vous demandera d'en créer un. Cliquez sur « Oui » pour continuer.
   - Cela créera automatiquement un environnement virtuel dans le dossier de votre projet.

6. **Sélectionner l'interprète Python**:
   - Assurez-vous que VS Code utilise le nouvel environnement virtuel. 
   - S'il ne le détecte pas automatiquement, appuyez sur `Ctrl + Shift + P` (ou `Cmd + Shift + P` sur macOS), tapez **"Python : Select Interpreter « **, et choisissez l'environnement nouvellement créé.

    
## Exécution du script
Pour exécuter le script, procédez comme suit :
1. Vérifiez que VS Code utilise l'environnement virtuel (vérifiez le coin inférieur gauche de la fenêtre VS Code).
2. Ouvrez un nouveau terminal dans VS Code s'il n'y en a pas déjà un.
3. Exécutez le script en utilisant la commande suivante :
   ```bash
   python Playlist-Duplicates-Purifier.py
   ```

## Désintallation
A la fin du processus vous aurez surement envie de désintaller les éléments : 
1. Désintaller python et Visual studio code a partir des paramètre windows comme toutes les autres applications
Si vous désintaller de cette façon les packages installé en faisans "pip install" se désintalleront également.



</details>