<h1>
  <br>
    Chess Search App
  <br>
</h1>

<p>
  <a href="https://github.com/tylerhgv/chess-search/search?l=python"><img src="https://img.shields.io/github/languages/top/tylerhgv/chess-search"></a>
  &nbsp;
  <a href="https://github.com/tylerhgv/chess-search/commits/main"><img src="https://img.shields.io/github/last-commit/tylerhgv/chess-search"></a>
  &nbsp;
  <a href="https://github.com/tylerhgv/chess-search/issues/"><img src="https://img.shields.io/github/issues-raw/tylerhgv/chess-search?color=orange"></a> 
</p>

<p>&nbsp;</p>
<h2 id="overview"> Overview </h2>

A simple search engine that allow searching for chess games based on queries about opening names & opening moves. Built with Python 3.10 and [python-chess](https://python-chess.readthedocs.io/en/latest/#).

<p>&nbsp;</p>
<h2 id="usage"> Usage </h2>

- **How To Run:** (currently not implemented)

- **Main Features:**

  - **Search by Opening Name:** Search by querying the name of an opening (e.g. "Queen Gambit"). Casing does not matter.
  - **Search by Opening Moves:** Search by querying opening plies (up to the first 3 moves / 6 plies) (e.g. "e4 e5 Ke2"). No move number necessary.
  - **Output:** Top 20 results, sorted by most recent games by default.

- **Data Source:** Data was taken from [lichess](https://lichess.org/)'s database. A total of 121,332 games from Jan 2013 were analyzed. 

<p>&nbsp;</p>
<h2 id="alg"> Algorithm Details </h2>

<h3> Search by Opening Name </h3>

- **How results are ranked:**
  - The goal of the algorithm is to rank results based on the following priorities:

    - **Priority #1:** Documents with more matching terms > documents with fewer matching terms.
    - **Priority #2:** Documents with more important terms > documents with less important terms.
    - If two documents have equal weight, fallback to default ranking (by most recent).

- **How queries are processed:**
  - **Step 1:**
  
    - Given a query string, a list of n terms [t1, t2,... tn] is extracted.
    - Terms are ordered by increasing document frequencies (t1 have the lowest df and therefore is the most significant).
  
  - **Step 2:**
  
    - Retrieve a list of postings lists [p1, p2,... pn] based on the terms.
    - p1 has the smallest size.
  
  - **Step 3:**
  
    - Intersect the lists, starting with intersection of n lists (Find documents that have all n terms). (**Priority #1**)
    - If number of retrieved docs < 20, continue finding intersection of n-1 lists, n-2 lists,... 1 list.
    - In each iteration of intersecting n-k lists, prioritize docs that have terms with low df (t1 > t2 > ... > tn). (**Priority #2**)
    - Continue until 20 documents are retrieved.
  
  - **Time Complexity:** This is not optimized, so probably very large. 

<p>&nbsp;</p>
<h2 id="tech"> Technologies Used </h2>

| Name | Description |
| --- | --- |
| Python 3.10 | Main development language. |
| python-chess 1.7.0 | Library for handling .pgn files. |
| nltk 3.6.5 | Library for natural language processing (tokenizing, stemming). |
| PyQt (planned) | Framework for building GUI with Python. |

<p>&nbsp;</p>
<h2 id="screens"> Screenshots </h2>

None at the moment

<p>&nbsp;</p>
