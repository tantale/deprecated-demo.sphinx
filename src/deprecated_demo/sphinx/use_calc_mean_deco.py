"""
Use Calc Mean Deco
==================

Use the following command from the project root directory to
see the decorated function in action::

    python -m deprecated_demo.sphinx.use_calc_mean_deco
"""
from deprecated_demo.sphinx.calc_mean_deco import mean

if __name__ == '__main__':
    print(mean.__doc__)
