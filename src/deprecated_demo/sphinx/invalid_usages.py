"""
Invalid Usages
==============

Examples of invalid usages of the Sphinx decorators.

The decoration of the following functions is bad.

No parameter at all:

.. code-block:: python

   @deprecated
   def bad1():
       pass


Missing ``version`` argument:

.. code-block:: python

   @deprecated(reason="bad reason")
   def bad2():
       pass


Invalid type for ``reason`` argument:

.. code-block:: python

   @deprecated(reason=5)
   def bad3():
       pass

See the best practices bellow:
"""
from deprecated.sphinx import deprecated


@deprecated(version="4.3.0")
def good1():
    pass


@deprecated(version="4.3.0", reason="this function will be removed in v4.4.0")
def good2():
    pass


@deprecated(version="4.3.0")
def good3():
    """This is a good function"""


@deprecated(version="4.3.0", reason="this function will be removed in v4.4.0")
def good4():
    """This is a good function"""

