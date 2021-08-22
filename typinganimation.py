def scirpt():
    def typing_animation():
        import sys
        from time import sleep

        words = "Welcome to the words of wisdom!! \n"
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
            
    typing_animation()

if __name__ == "__main__":
    scirpt()