# “CurrentCulture” (Problem)

Look to the following code:

```cs
Thread.CurrentThread.CurrentUICulture = 
  CultureInfo.CreateSpecificCulture("ru-RU");
Thread.CurrentThread.CurrentCulture = 
  CultureInfo.CreateSpecificCulture("en-US");
var dateTime = new DateTime(2014, 12, 31, 13, 1, 2);
Console.WriteLine(dateTime);
```

Which locale will be choose for date formatting?

[Solution](./CurrentCulture-S.md)