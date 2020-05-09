# Zeuthen Strategy - Monotonic Concession Protocol

Calculates the agreed deal between 2 agents negotiating tasks under the Zeuthen Strategy.

Project done to support a written essay for the 2019-2020 Autonomous Agents and Multi-Agent Systems in Instituto Superior Técnico.

## Example

The input:
```python
a1_util = [1, 2, 2, 3, 4]
a2_util = [4, 3, 2, 2, 2]

strategy = ZeuthenStrategy(a1_util, a2_util)

strategy.initialAgent = "A1"
strategy.execute()
```

Outputs:

```
Initial concede: A1
Final Deal: A2
A1: [3, 4]
A2: [0, 1, 2]
A1 util: 7
A2 util: 9
```

## Authors

* **Miguel Coelho** - *87687*
