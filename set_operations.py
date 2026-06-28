playlist_1 = ['Gehra Hua', 'Saiyaara', 'Jaiye Sajana', 'Mashooqa', 'Barbaad']
playlist_2 = ['Gehra Hua', 'Saiyaara', 'Barbaad', 'Sitaare', 'Shararat', 'Arz Kiya Hai ']

def commonplaylist(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

def blendplaylist(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.union(set2)
common = commonplaylist(playlist_1, playlist_2)
blend = blendplaylist(playlist_1, playlist_2)
print(f'the common playlist: {common}')
print(f'the blended playlist: {blend}')
