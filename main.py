import utils

def main(url):
    utils.extract_transcript(url)
    utils.convert_sub()

    with open("./transcript.en.srt") as f:
        data = f.read()
        filtered_data = utils.filter_transcript(data)
        print(filtered_data)

if __name__ == "__main__":
    main("https://youtu.be/4u5x9e226i4")
