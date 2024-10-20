import argparse
import sys

import utils

def main():
    parser = argparse.ArgumentParser(prog='video-summarize', description='summarize youtube videos using llm')

    parser.add_argument('link', help='youtube link for summarizing')
    parser.add_argument('-o', '--output', help='write output to a file')
    parser.add_argument('-t', '--transcript_file', help='write transcript to a file')
    parser.add_argument('-m', '--model', help='ollama model to use. defaults to gemma2:2b', default='gemma2:2b')
    parser.add_argument('-c', '--character_limit', help='custom character limit for models. defaults to 16000', default=16000)
    # parser.add_argument('-H', '--host', help='address of ollama api service', required=True)

    args = parser.parse_args()

    url = args.link
    utils.extract_transcript(url)

    with open("./transcript.en.srt") as f:
        data = f.read()
        filtered_data = utils.filter_transcript(data)

        if args.transcript_file:
            utils.write_to_file(args.output, filtered_data)

        summary = utils.summarize_text(filtered_data, args.model, args.character_limit)
        if args.output:
            utils.write_to_file(args.output, summary)
        print(summary)

if __name__ == "__main__":
    main()
