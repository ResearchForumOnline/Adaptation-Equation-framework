from src.equations import genetic_adaptation_equation

def test_adaptation():
    val = genetic_adaptation_equation(1, 1, 0.5, 0.5, 1.5, 0.01, 0.3, 0.4, 0.7, 0.1, 0.01)
    assert val > 0