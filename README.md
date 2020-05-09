# Zeuthen Strategy - Monotonic Concession Protocol

Calculates the agreed deal between 2 agents negotiating tasks under the Zeuthen Strategy.

##Example

```python
a1_util = [1, 2, 2, 3, 4]
a2_util = [4, 3, 2, 2, 2]

strategy = ZeuthenStrategy(a1_util, a2_util)

strategy.initialAgent = "A1"
strategy.execute()
```



## Authors

* **Miguel Coelho** - *87687*
