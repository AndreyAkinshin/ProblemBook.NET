# “CaseInComparison” (Solution)

No, it depends from current CultureInfo. An example:

```cs
var a = "i";
var b = "I";
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("tr-TR");
Console.WriteLine(
  string.Compare(a.ToUpper(), b)); //'1'
Console.WriteLine(
  string.Compare(a, b, StringComparison.OrdinalIgnoreCase)); //'0'
```

See [The Turkey Test](http://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html).

[Problem](./CaseInComparison-Q.md)