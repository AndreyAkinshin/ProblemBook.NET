# “LockSlimInFinalizer” (Solution)

## Answer

```
~Foo: start
Exception: SynchronizationLockException
~Foo: finish
```

## Explanation

A [SynchronizationLockException](http://msdn.microsoft.com/library/system.threading.synchronizationlockexception.aspx) will be thrown because the finalizer will be called from the GC thread.

[Problem](./LockSlimInFinalizer-P.md)