# PageRank Algorithm
import numpy as np

pages = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": ["A"],
    "D": ["C"]
}

page_names = list(pages.keys())
n = len(page_names)

rank = {page: 1 / n for page in page_names}
# Damping factor
d = 0.85

for iteration in range(100):

    new_rank = {}

    for page in page_names:

        # Random jump probability
        new_rank[page] = (1 - d) / n

        # Find pages that link to the current page
        for source in page_names:

            if page in pages[source]:

                # Number of outgoing links from source page
                outgoing_links = len(pages[source])

                if outgoing_links > 0:
                    new_rank[page] += (
                        d * rank[source] / outgoing_links
                    )
    rank = new_rank

print("PageRank Values")
print("----------------")

for page, value in sorted(
    rank.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(page, ":", round(value, 6))
