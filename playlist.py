def display_playlist():
    songs = ["7 Rings", "Golden Hour", "Bite Me"]

    print("\n===== MY PLAYLIST =====")
    for number, song in enumerate(songs, start=1):
        print(f"{number}. {song}")