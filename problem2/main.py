def draw_xyz(N):
    characters = ['X', 'Y', 'Z']
    character_index = 0
    result = ""

    for i in range(1, N**2 + 1):
        if i % 3 == 0:
            result += characters[0] + " "
        else:
            if i % 2 == 0:
                result += characters[2] + " "
            else:
                result += characters[1] + " "

        if i % N == 0:
            result += "\n"

    return result

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """
    
    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """