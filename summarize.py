from csv import reader, writer
import os
from summarizer import Summarizer


def summarize(body):
    model = Summarizer()

    result = model(body, ratio=0.15, min_length=30)
    summary = ''.join(result)

    return summary


with open("articoli.csv", "r") as source, open("buffer.csv", "w", newline='') as output:
    rdr = reader(source, delimiter=";")
    wtr = writer(output, delimiter=";")

    line = 0
    for row in rdr:
        body = row[4]
        # summary = body[:10]
        summary = summarize(body)

        row.append(summary)
        wtr.writerow(row)

        line+=1


with open("buffer.csv", "r") as source:
    rdr = reader(source, delimiter=";")

    with open("output.csv", "w", newline='') as result:
        wtr = writer(result, delimiter=";")
        for r in rdr:
            wtr.writerow((r[0], r[1], r[2], r[3], r[5]))

os.remove("buffer.csv")




