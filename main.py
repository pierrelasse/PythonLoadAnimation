from loadanim import loadanim

def main():
    for i in range(5):
        loadanim(
            text1 = f"Test{i + 1} %c",
            text2 = f"Test{i + 1} OK",

            time = 1,
            wait = 0.05
        )
        
if __name__ == "__main__":
    main()