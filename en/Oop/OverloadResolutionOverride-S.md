# “OverloadResolutionOverride” (Solution)

```
Bar.Quux(object)
Baz.Quux(params T[])
```

There is a rule: if compiler found a suitable signature for a method call in the “current” class, compiler will not look to parents classes. In this problem, the `Bar` and `Baz` classes have own versions of the `Quux` method. Their signatures are suitable for the call argument list. Thus, they will be called; the overloaded `Quux` method of the base class will be ignored.

See also:

* [“Overloading”](http://csharpindepth.com/Articles/General/Overloading.aspx) in [“C# in Depth”](http://csharpindepth.com/)

[Problem](./OverloadResolutionOverride-P.md)