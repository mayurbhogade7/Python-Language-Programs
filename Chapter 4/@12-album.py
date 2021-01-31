def make_album(album_title, artist_name, num_songs=None):
    album = {'album title': album_title, 'artist_name': artist_name}
    if num_songs:
        album['number of songs'] = num_songs
    return album

while True:
    print("Enter album title, artist name and number of songs")
    a_t = input("album title: ")
    a_n = input("artist name: ")
    n_s = input("number of songs: ")
    album = make_album(a_t, a_n, n_s)
    print(album)
    r = input("Do you want to continue (yes/ no): ")
    if r == 'no':
        break