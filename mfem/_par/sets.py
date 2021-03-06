# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sets
else:
    import _sets

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _sets.SWIG_PyInstanceMethod_New
_swig_new_static_method = _sets.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import mfem._par.array
import mfem._par.mem_manager
import mfem._par.table
class IntegerSet(object):
    r"""Proxy of C++ mfem::IntegerSet class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(IntegerSet self) -> IntegerSet
        __init__(IntegerSet self, IntegerSet s) -> IntegerSet
        __init__(IntegerSet self, int const n, int const * p) -> IntegerSet
        """
        _sets.IntegerSet_swiginit(self, _sets.new_IntegerSet(*args))

    def Size(self):
        r"""Size(IntegerSet self) -> int"""
        return _sets.IntegerSet_Size(self)
    Size = _swig_new_instance_method(_sets.IntegerSet_Size)

    def PickElement(self):
        r"""PickElement(IntegerSet self) -> int"""
        return _sets.IntegerSet_PickElement(self)
    PickElement = _swig_new_instance_method(_sets.IntegerSet_PickElement)

    def PickRandomElement(self):
        r"""PickRandomElement(IntegerSet self) -> int"""
        return _sets.IntegerSet_PickRandomElement(self)
    PickRandomElement = _swig_new_instance_method(_sets.IntegerSet_PickRandomElement)

    def __eq__(self, s):
        r"""__eq__(IntegerSet self, IntegerSet s) -> int"""
        return _sets.IntegerSet___eq__(self, s)
    __eq__ = _swig_new_instance_method(_sets.IntegerSet___eq__)

    def Recreate(self, n, p):
        r"""Recreate(IntegerSet self, int const n, int const * p)"""
        return _sets.IntegerSet_Recreate(self, n, p)
    Recreate = _swig_new_instance_method(_sets.IntegerSet_Recreate)
    __swig_destroy__ = _sets.delete_IntegerSet

# Register IntegerSet in _sets:
_sets.IntegerSet_swigregister(IntegerSet)

class ListOfIntegerSets(object):
    r"""Proxy of C++ mfem::ListOfIntegerSets class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Size(self):
        r"""Size(ListOfIntegerSets self) -> int"""
        return _sets.ListOfIntegerSets_Size(self)
    Size = _swig_new_instance_method(_sets.ListOfIntegerSets_Size)

    def PickElementInSet(self, i):
        r"""PickElementInSet(ListOfIntegerSets self, int i) -> int"""
        return _sets.ListOfIntegerSets_PickElementInSet(self, i)
    PickElementInSet = _swig_new_instance_method(_sets.ListOfIntegerSets_PickElementInSet)

    def PickRandomElementInSet(self, i):
        r"""PickRandomElementInSet(ListOfIntegerSets self, int i) -> int"""
        return _sets.ListOfIntegerSets_PickRandomElementInSet(self, i)
    PickRandomElementInSet = _swig_new_instance_method(_sets.ListOfIntegerSets_PickRandomElementInSet)

    def Insert(self, s):
        r"""Insert(ListOfIntegerSets self, IntegerSet s) -> int"""
        return _sets.ListOfIntegerSets_Insert(self, s)
    Insert = _swig_new_instance_method(_sets.ListOfIntegerSets_Insert)

    def Lookup(self, s):
        r"""Lookup(ListOfIntegerSets self, IntegerSet s) -> int"""
        return _sets.ListOfIntegerSets_Lookup(self, s)
    Lookup = _swig_new_instance_method(_sets.ListOfIntegerSets_Lookup)

    def AsTable(self, t):
        r"""AsTable(ListOfIntegerSets self, Table t)"""
        return _sets.ListOfIntegerSets_AsTable(self, t)
    AsTable = _swig_new_instance_method(_sets.ListOfIntegerSets_AsTable)
    __swig_destroy__ = _sets.delete_ListOfIntegerSets

    def __init__(self):
        r"""__init__(ListOfIntegerSets self) -> ListOfIntegerSets"""
        _sets.ListOfIntegerSets_swiginit(self, _sets.new_ListOfIntegerSets())

# Register ListOfIntegerSets in _sets:
_sets.ListOfIntegerSets_swigregister(ListOfIntegerSets)



