# “NoStringInterning” (Problem)

Look to the following code:

```cs
[assembly: CompilationRelaxationsAttribute
  (CompilationRelaxations.NoStringInterning)]
```

Does it means, that the literal string in this assembly now will be interned?

[Solution](./NoStringInterning-S.md)