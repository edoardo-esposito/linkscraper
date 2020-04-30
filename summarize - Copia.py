from csv import reader, writer
import os
import re
from pathlib import Path
from summarizer import Summarizer


def clean_text(text):
    # remove backslash-apostrophe
    text = re.sub("\'", "", text)
    # remove everything except alphabets
    text = re.sub("[^a-zA-Z]", " ", text)
    # remove whitespaces
    text = ' '.join(text.split())
    # convert text to lowercase
    text = text.lower()

    return text


def summarize(id, body):
    print("SUMMARIZE ID: %s" % id)
    filename = "temp/%s.csv" % id

    result = model(clean_text(body), ratio=0.15, min_length=30)
    summary = ''.join(result)
    # summary = body[:10]

    with open(filename, "w") as output:
        wtr = writer(output, delimiter=";")
        rowcontents = [summary]
        wtr.writerow(rowcontents)

    return body


def summarizefile(filename):
    with open(filename, "r") as source, open("buffer.csv", "w", newline='') as output:
        rdr = reader(source, delimiter=";")
        wtr = writer(output, delimiter=";")

        for row in rdr:
            if len(row[4]):
                id = row[0]
                body = row[4]
                summary = summarize(id, body)

                row.append(summary)
                wtr.writerow(row)

        summaries = {}
        directory = "temp"
        pathlist = Path(directory).glob('**/*.csv')

        for path in pathlist:
            path_in_str = str(path)
            base = os.path.basename(path_in_str)
            ID = os.path.splitext(base)[0]

            with open(path_in_str, "r") as source:
                fr = reader(source, delimiter=";")
                for r in fr:
                    summaries[ID] = r[0]
                    break

        return summaries


#TODO remove all files in temp directory
def writesummariestofile(summaries):
    with open("buffer.csv", "r") as source:
        rdr = reader(source, delimiter=";")

        with open("articles_summarized.csv", "a", newline='') as result:
            wtr = writer(result, delimiter=";")
            for r in rdr:
                wtr.writerow((r[0], r[1], r[2], r[3], r[5], summaries[r[0]]))

    os.remove("buffer.csv")


model = Summarizer()
directory = "output"
pathlist = Path(directory).glob('**/*.csv')
for path in pathlist:
    path_in_str = str(path)
    filename = path_in_str
    summaries = summarizefile(filename)
    writesummariestofile(summaries)

    break
