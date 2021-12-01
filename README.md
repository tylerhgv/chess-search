<h1>
  <br>
    Chess Search App (UNFINISHED)
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

- **How To Run:** Install requirements, then run chessSearch.py.

- **Main Features:**
  - <ins>Search by Opening Name</ins>: Search by querying the name of an opening (e.g. "Queen Gambit"). Casing does not matter.
  - <ins>Search by Opening Moves</ins>: Search by querying opening plies (up to the first 3 moves / 6 plies) (e.g. "e4 e5 Ke2"). No move number necessary.
  - <ins>Output</ins>: Top 20(?) results, sorted by most recent games by default.

- **Data Source:** Data was taken from [lichess](https://lichess.org/)'s database. A total of 121,332 games from Jan 2013 were analyzed. 

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
