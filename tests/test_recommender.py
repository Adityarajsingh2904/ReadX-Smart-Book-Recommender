import recommender


def test_recommend_books_returns_results():
    results = recommender.recommend_books(276747, n=5)
    assert isinstance(results, list)
    assert len(results) > 0
    assert all('ISBN' in r for r in results)
