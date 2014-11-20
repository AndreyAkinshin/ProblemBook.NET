# “OverloadResolutionInheritance” (Solution)

## Answer

```
Bar.Quux(),  
Bar.Quux(params object[])
Bar.Quux(),  Baz
```

## Explanation

A schematic calls tree of the code:

```cs
Main();
  new Baz(); // Baz.ctor
      base.ctor(); // Bar.ctor
        base.ctor(); // Foo.ctor
          Quux(); // Bar.Quux() beacuse there is an overload
            Console.WriteLine("Bar.Quux(),  " + name);
            // name doesn't have value
        name = "Bar";
    name = "Baz";
    Quux();
      // Bar.Quux(params object[] args) because Bar have a suitable method
      Console.WriteLine("Bar.Quux(params object[])");
    ((Foo)this).Quux(); // Bar.Quux() beacuse there is an overload
      Console.WriteLine("Bar.Quux(),  " + name); // name == "Baz"
```

## Links

* [The “OverloadResolutionOverride” problem](./OverloadResolutionOverride-P.md)

[Problem](./OverloadResolutionInheritance-P.md)