import argparse

import utils

parser = argparse.ArgumentParser(prog='video-summarize', description='summarize youtube videos using llm')

parser.add_argument('link', help='youtube link for summarizing')
parser.add_argument('-o', '--output', help='write output to a file')

args = parser.parse_args()

def main(url):
    utils.extract_transcript(url)
    utils.convert_sub()

    with open("./transcript.en.srt") as f:
        data = f.read()
        filtered_data = utils.filter_transcript(data)

        if args.output:
            with open(args.output, "w") as f:
                f.write(filtered_data)
                print(f"Writing output to \'{args.output}\'")
                exit(1)
        print(filtered_data)

if __name__ == "__main__":
    main(args.link)
