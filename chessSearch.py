# Import stuff
import ujson
import string
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import itertools
import time


def read_query_name(q):
    """
    Take a string query about opening name and return a list of top 20 matching docs
    :param q: Input query
    :type q: str
    :return: List of 20 matching docIDs
    :rtype: list
    """

    postings = []
    results = []

    # Open inverted index for terms
    with open('data/terms.json', 'r') as f:
        terms_index = ujson.load(f)

    # Extract terms from query
    q_raw = index_terms(q)
    q_terms = []
    for term in q_raw:
        if term in terms_index:
            q_terms.append(term)
    doc_freq = []
    for term in q_terms:
        doc_freq.append(f'{term} ({len(terms_index[term])})')
    print(f'[INFO] Terms extracted from query: {doc_freq}')

    # Build an array of matching postings lists
    for term in q_terms:
        postings.append(terms_index[term])

    # Intersect lists & build results
    print('[INFO] Begin building results')

    # No matching postings lists found
    if len(postings) == 0:
        print(f'[INFO] {len(postings)} postings list found. Return empty')
        return results

    # No intersect if only one postings list
    elif len(postings) == 1:
        print(f'[INFO] {len(postings)} postings list found. Return top 20')
        postings.reverse()
        results = postings[:20]
        return results

    # Intersect if more than one posting list
    elif len(postings) > 1:
        print(f'[INFO] {len(postings)} postings lists found. Begin intersecting')

        # Sort postings lists by doc frequency (length of lists) (smallest -> largest)
        postings.sort(key=len)
        len_new = [len(x) for x in postings]
        print(f'[INFO] Lengths of postings lists after sorting: {len_new}')

        # Intersect postings lists to find matches
        print(f'[INFO] Begin intersection of {len(postings)} total lists')
        n = len(postings)
        while len(results) < 20:
            # Main idea behind the algorithm:
            # Step 1:
            #   - A list of terms (t0,t1,... tn) is given
            #   - t0 is the most important (smallest docFreq)
            # Step 2:
            #   - Retrieve a list of postings lists (p0,p1,... pn)
            #   - p0 has the smallest size
            # Step 3:
            #   - Intersect the postings lists
            #   - Start with the intersection of n lists
            #       (Find docs that have all n terms)
            #   - If not enough 20 results, find intersection of n-1 lists, n-2 lists,...
            #   - In each iteration of n-k, prioritize postings that have t0 > tn
            #   - Continue until reaching 20 results
            # GOAL: To sort the results based on following priorities (P = postings):
            #   - Priority #1: P with more terms > P with fewer terms
            #   - Priority #2: P with more important (t0) > P with less important (tn)

            # Break if everything exhausted
            if n == 0:
                break

            # Compute intersection
            print(f'[INFO] Retrieving docs that are in {n} posting lists...', end='')
            r_temp = find_postings(postings, n)

            # Add to result until 20 docs are retrieved
            # Few things here:
            #   - Postings are ordered least to most recent by default
            #   - Therefore, n last items of r_temp are grabbed
            #   - Results are appended to the beginning, and will be processed in reverse
            for item in postings:

                # Break if 20 are retrieved
                if len(results) >= 20:
                    break

                # Remove entries that are already in result
                r_temp = clean(list(set(r_temp) - set(results)))

                # Retrieve entries with smallest df terms to largest df terms
                num_needed = 20 - len(results)
                r_posting = clean(list(set(r_temp) & set(item)))
                results = r_posting[-num_needed:] + results

            n -= 1
            print(f'DONE (Current: {len(results)} retrieved)')

    # Reverse and return result
    results.reverse()
    return results


def index_terms(s):
    """
    Build a list of terms from a string input
    :param s: Input string
    :type s: str
    :return: List of terms
    :rtype: list
    """

    # Clean punctuation
    for word in s:
        if word in string.punctuation:
            s = s.replace(word, " ")

    # Normalize case
    s = s.lower()

    # Tokenize
    tokens = word_tokenize(s)

    # Stem
    stemmer = PorterStemmer()
    tokens_stemmed = [stemmer.stem(t) for t in tokens]

    # Remove duplicates
    result = list(set(tokens_stemmed))

    # Return list of terms
    return result


def find_postings(p, n):
    """
    Given a list of postings lists (PL), return the docs that belong to exactly n PLs
    This module returns the intersections of every possible combination of n PLs
    (n <= len(p))

    :param p: List of PLs
    :type p: list
    :param n: Number of PLs that the doc must belong to
    :type n: int
    :return: List of docs that belong to exactly n PLs
    :rtype: list
    """

    # Generate all possible combinations
    combs = list(itertools.combinations(range(len(p)), n))

    # Find intersection of each combination tuple
    # Each tuple contains index of the postings lists
    result = []
    for item in combs:
        set_list = []
        for index in item:
            set_list.append(set(p[index]))
        temp = list(set.intersection(*set_list))
        result += temp

    # Clean and return result
    result = clean(result)
    return result


def clean(li):
    """
    Helper function to clean a list by removing duplicates & sorting ascending
    :param li: Input list
    :type li: list
    :return: Cleaned list
    :rtype: list
    """
    li = list(set(li))
    li.sort()
    return li


if __name__ == '__main__':
    print('[INFO] Starting...')
    nltk.download('punkt')

    # Load docs
    print('[INFO] Loading documents database...', end='')
    with open('data/docs.json', 'r') as infile:
        docs = ujson.load(infile)
    print(f'DONE')

    # Read user query
    t_start = time.perf_counter()
    q_test = 'king indian anglo english defense formation'
    res = read_query_name(q_test)
    print(f'[INFO] Complete result list: {res}')
    i = 1
    for index in res:
        print(f'[OUT] ({i}) GAME #{index}: {docs[str(index)]["openingName"]}')
        i += 1

    t_elapsed = round(time.perf_counter() - t_start, 2)
    print(f'[INFO] Elapsed time: {t_elapsed}s')
