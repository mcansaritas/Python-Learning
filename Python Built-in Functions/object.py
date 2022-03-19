"""The built-in object() method returns an empty object. You cannot add new properties or methods
to this object. This object is the base for all classes, it holds the built-in properties and
methods which are default for all classes. The syntax is object()."""

x = object()
print(dir(x))