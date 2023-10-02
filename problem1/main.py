def play_with_asterisk(n):
    result = ""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        result += spaces + stars + "\n"
    return result

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
