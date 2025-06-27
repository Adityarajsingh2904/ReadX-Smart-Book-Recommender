import csv
import random

DATA_RATINGS = "data/BX-Book-Ratings-Subset.csv"
DATA_BOOKS = "data/BX-Books.csv"

# hyperparameters for matrix factorization
K = 10
STEPS = 5
ALPHA = 0.002
BETA = 0.02

_user_map = {}
_item_map = {}
_user_ids = []
_item_ids = []
_books = {}
_ratings = []
_P = []
_Q = []


def _load_data():
    """Load ratings and book metadata from CSV files."""
    global _ratings, _user_map, _item_map, _user_ids, _item_ids, _books

    _ratings = []
    _user_map = {}
    _item_map = {}
    _user_ids = []
    _item_ids = []

    with open(DATA_RATINGS, encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            user = int(row["User-ID"])
            item = row["ISBN"]
            rating = float(row["Book-Rating"])
            if user not in _user_map:
                _user_map[user] = len(_user_map)
                _user_ids.append(user)
            if item not in _item_map:
                _item_map[item] = len(_item_map)
                _item_ids.append(item)
            _ratings.append((_user_map[user], _item_map[item], rating))

    with open(DATA_BOOKS, encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            _books[row["ISBN"]] = {
                "ISBN": row["ISBN"],
                "Book-Title": row["Book-Title"],
                "Book-Author": row["Book-Author"],
                "Image-URL-M": row.get("Image-URL-M", ""),
            }


def _train_model():
    """Train a simple matrix factorization model using SGD."""
    global _P, _Q
    n_users = len(_user_map)
    n_items = len(_item_map)

    random.seed(0)
    _P = [[random.random() / K for _ in range(K)] for _ in range(n_users)]
    _Q = [[random.random() / K for _ in range(K)] for _ in range(n_items)]

    for _ in range(STEPS):
        for u, i, r in _ratings:
            pred = sum(_P[u][k] * _Q[i][k] for k in range(K))
            err = r - pred
            for k in range(K):
                _P[u][k] += ALPHA * (2 * err * _Q[i][k] - BETA * _P[u][k])
                _Q[i][k] += ALPHA * (2 * err * _P[u][k] - BETA * _Q[i][k])


def _init():
    _load_data()
    _train_model()


_init()


def _predict(u_idx, i_idx):
    return sum(_P[u_idx][k] * _Q[i_idx][k] for k in range(K))


def recommend_books(user_id, n=10):
    """Return a list of up to ``n`` recommended books for ``user_id``."""
    if user_id not in _user_map:
        return []

    u = _user_map[user_id]
    rated = {i for (uu, i, _) in _ratings if uu == u}
    scores = []
    for i in range(len(_item_ids)):
        if i not in rated:
            score = _predict(u, i)
            scores.append((score, i))
    top = sorted(scores, reverse=True)[:n]

    results = []
    for _, idx in top:
        isbn = _item_ids[idx]
        book = _books.get(isbn, {"ISBN": isbn})
        results.append(book)
    return results
