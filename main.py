import utils

def main():
    with open("./transcript-back.en.srt") as f:
        data = f.read()
        filtered_data = utils.filter(data)
        print(filtered_data)

if __name__ == "__main__":
    main()
