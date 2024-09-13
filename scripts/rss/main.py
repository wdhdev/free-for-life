import os
import time
import markdown
from feedgen.feed import FeedGenerator

DATA_DIR = "data"
RSS_PATH = "website/rss.xml"
START_ENTRY = "_start.md"
END_ENTRY = "_end.md"


def add_entry(feed: FeedGenerator, filename: str):
    print(f"Adding entry for file: {filename}")

    start_time = time.time()

    with open(f"{DATA_DIR}/{filename}", "r") as f:
        md_content = f.read()
        html_content = markdown.markdown(md_content, extensions=["markdown.extensions.tables"])
        fe = feed.add_entry()
        formatted_filename = filename.lower()[:-3].replace("_", "-")
        fe.title(formatted_filename)
        fe.link(href=f"https://free.hrsn.dev/#/?id={formatted_filename}")
        fe.description(html_content)

    end_time = time.time()
    print(f"Added entry for file: {filename} in {end_time - start_time} seconds.")


def main():
    start_time = time.time()
    fg = FeedGenerator()
    fg.title("Free For Life")
    fg.link(href="https://free.hrsn.dev/", rel="alternate")
    fg.description("A massive list including a huge amount of products and services that are completely free!")
    fg.language("en")

    print("Starting to generate RSS feed...")
    add_entry(fg, END_ENTRY)

    # Get the list of files and sort them
    data_files = sorted(os.listdir(DATA_DIR))

    for filename in data_files:
        if not filename.endswith(".md"):
            continue
        if filename in [START_ENTRY, END_ENTRY]:
            continue
        add_entry(fg, filename)

    add_entry(fg, START_ENTRY)

    fg.rss_file(RSS_PATH)

    end_time = time.time()

    print(f"RSS feed generated and saved to: {RSS_PATH} in {end_time - start_time} seconds.")


if __name__ == "__main__":
    print("Starting script...")
    main()
    print("Script finished.")
