# “OverloadResolutionBasic” (Solution)

## Answer

```
params object[]
params object[]
params T[]
params T[]
object, object
```

## Explanation

There are methods:

* `void Foo(object a)` -> `object`
* `void Foo(object a, object b)` -> `object, object`
* `void Foo(params object[] args)` -> `params object[]`
* `void Foo<T>(params T[] args)` -> `params T[]`

Let's consider each call separately.

* `Foo()` -> `params object[]`

The `object` and `object, object` options is inaccessible because of number of arguments. The `params T[]` option is inaccessible because of the compiler can't resolve `T`. Thus, the right options is `params object[]`.

* `Foo(null)` -> `params object[]`

The `object, object` option is inaccessible because of number of arguments. The `params T[]` options is inaccessible because of the compiler can't resolve `T`. The `params object[]` option is acceptable in its `expanded` and `unexpanded` forms. In this case, we should choose the `expanded` form, i.e. the method signature will look like `Foo(object[] args)`. Now, we have the `object` and `object[]` options. The compiler will choose more specific option, i.e. `object[]` (or `params object[]`).

* `Foo(new Bar())` -> `params T[]`

The `object, object` option is inaccessible because of number of arguments. The `object` and `params object[]` options request an additional implicitly conversion: `Bar` to `object`. So, the `params T[]` (or `params Bar[]`) option is more preferable.

* `Foo(new Bar(), new Bar())` -> `params T[]`

The `object` option is inaccessible because of number of arguments. The `object, object` and `params object[]` options request an additional implicitly conversion: `Bar` to `object`. So, the `params T[]` (or `params Bar[]`) option is more preferable.

* `Foo(new Bar(), new object())` -> `object, object`

The `object` option is inaccessible because of number of arguments. There is exactly one option without the `params` keyword: `object, object`. It is more preferable.

## Links

* [“Overload resolution”](http://msdn.microsoft.com/library/aa691336.aspx), [“Method invocations”](http://msdn.microsoft.com/library/aa691356.aspx), [“Applicable function member”](http://msdn.microsoft.com/en-US/library/aa691337.aspx) in MSDN
* [“Overloading”](http://csharpindepth.com/Articles/General/Overloading.aspx) in [“C# in Depth”](http://csharpindepth.com/)

[Problem](./OverloadResolutionBasic-P.md)