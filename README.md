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

A simple search engine that allow searching for chess games based on queries about opening names & opening moves. Built with Python 3.10 and [python-chess](https://python-chess.readthedocs.io/en/latest/#).

<p>&nbsp;</p>
<h2 id="usage"> Usage </h2>

- **How To Run:** 
  - Install Python.
  - Create a virtual environment & install requirements from requirements.txt.
  - Activate the virtual environment. Usually the command is: ``` .\[venv name]\Scripts\activate ```.
  - Run app.py from the project's root directory: ``` python app.py ```.

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

<h3> Search by Opening Moves </h3>

- **How results are ranked:**
  - The goal of the algorithm is to retrieve only games that match the exact valid move sequences.
  - Due to the strict matching, the only ranking priority is: game with more matching plies > game with fewer matching plies.

- **How queries are processed:**
  - **Step 1:**
  
    - A list of maximum 6 plies [ply1, ply2,... ply6] is extracted.
    - The entire list of plies must be valid plies.
  
  - **Step 2:**
  
    - Retrieve a list of 6 postings lists [pos1, pos2,... pos6] such that: pos[i] = games that contain ply[i] as the [i]th ply.
    - For example:
      - Ply sequence: [e4, e5, ...].
      - Postings list: pos2 = games that have e5 as the second ply.
  
  - **Step 3:**
  
    - Intersect the postings lists, starting with the first 6 lists (Find games that match the entire 6 plies / 3 moves).
    - If not enough 20 results, continue finding intersection of the first 5 lists, 4 lists,...
    - Continue until 20 documents are retrieved.
  
<h3> Time Complexity </h3>

These are not optimized, so probably very large. 

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

Main screen.

![1](https://user-images.githubusercontent.com/41291862/144515301-d065eb51-0758-4353-9476-48b28ee4027d.png)

<p>&nbsp;</p>

Searching by opening name.

![2](https://user-images.githubusercontent.com/41291862/144515374-70acf8a3-7aeb-459d-ae04-5eb5dbc8cc78.png)

<p>&nbsp;</p>

Searching by opening moves.

![3](https://user-images.githubusercontent.com/41291862/144515377-777830f7-4860-4450-be3d-acf0a203324c.png)

<p>&nbsp;</p>
