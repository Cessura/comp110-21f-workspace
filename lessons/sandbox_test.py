from sandbox import sum

def test_sum_empty() -> None:
    xs:list[float] = []
    assert sum(xs) == 0.0

def test_sum_one_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 0.0

def test_sum_multiple() -> None:
     xs: list[float] = [1.0, 2.0, 3.0] 
     assert sum(xs) == 6.0