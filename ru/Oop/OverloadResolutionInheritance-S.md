# «OverloadResolutionInheritance» (Решение)

```
Bar.Quux(),  
Bar.Quux(params object[])
Bar.Quux(),  Baz
```

Ниже представлен схематический порядок вызовов в приведённом коде:

```cs
Main();
  new Baz(); // Baz.ctor
      base.ctor(); // Bar.ctor
        base.ctor(); // Foo.ctor
          Quux();
            // Будет вызван Bar.Quux(),
            // т.к. Quux() имеет перегрузку в дочернем классе
            Console.WriteLine("Bar.Quux(),  " + name);
            // в name пока ничего не хранится
        name = "Bar";
    name = "Baz";
    Quux();
      // Будет вызван Bar.Quux(params object[] args),
      // т.к. в классе Bar есть подходящий метод
      Console.WriteLine("Bar.Quux(params object[])");
    ((Foo)this).Quux(); 
      // Будет вызван Bar.Quux(), 
      // т.к. Quux() имеет перегрузку в дочернем классе
      Console.WriteLine("Bar.Quux(),  " + name);
      // name == "Baz"
```

См. также:

* [Задача «OverloadResolutionOverride»](./OverloadResolutionOverride-P.md)

[Задача](./OverloadResolutionInheritance-P.md)