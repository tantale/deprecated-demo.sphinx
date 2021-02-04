"""
Invalid Usages
==============

Exemple of invalid usages of the Sphinx decorators.
"""
from deprecated.sphinx import deprecated


@deprecated
def foo():
    """ bad: ``@deprecated`` """

@deprecated(reason="bad reason")
def foo():
    """ bad: ``@deprecated(reason="bad reason")`` """

@deprecated(reason=5)
def foo():
    """ bad: ``@deprecated(reason=5)`` """

@deprecated(version=3.14)
def foo():
    """ bad: ``@deprecated(version=3.14)`` """
