# “QueryAfterRemove” (Solution)

## Answer

```
1
```

## Explanation

When you call `list.Where(c => c.StartsWith("B"))`, query will only built, but not executed. The actual execution begins at the moment of the call `query.Count()`. By this time, the value of `list` will be `{ "Foo", "Baz" }`, and hence, there exists only one element that starts with the `'B'` letter.

[Problem](./QueryAfterRemove-P.md)