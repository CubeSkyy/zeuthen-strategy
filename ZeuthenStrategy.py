class ZeuthenStrategy:
    agentName = "A1"
    initialConcede = agentName

    def __init__(self, a1_util, a2_util):
        self.A1Util = a1_util
        self.A2Util = a2_util
        self.A1SelfDeal = list(range(len(a1_util)))
        self.A2SelfDeal = list(range(len(a2_util)))
        self.A1Deal = []
        self.A2Deal = []
        self.initialAgent = "A1"

    @staticmethod
    def swap_element(src, dst, index):
        if index not in dst:
            dst.append(index)
        if index in src:
            src.remove(index)

    def remove_a1_self_deal(self, index):
        self.swap_element(self.A1SelfDeal, self.A1Deal, index)

    def remove_a2_self_deal(self, index):
        self.swap_element(self.A2SelfDeal, self.A2Deal, index)

    @staticmethod
    def get_util(deal, utils):
        sum_ = 0
        for e in deal:
            sum_ += utils[e]

        return sum_

    def get_a1_util(self, deal):
        return self.get_util(deal, self.A1Util)

    def get_a2_util(self, deal):
        return self.get_util(deal, self.A2Util)

    def agreement(self):
        return self.get_a1_util(self.A2Deal) >= self.get_a1_util(self.A1SelfDeal) or self.get_a2_util(
            self.A1Deal) >= self.get_a2_util(self.A2SelfDeal)

    def agreed_deal(self):
        if self.get_a1_util(self.A2Deal) >= self.get_a1_util(self.A1SelfDeal):
            return "A2"
        else:
            return "A1"

    def get_a1_risk(self):
        return (self.get_a1_util(self.A1SelfDeal) - self.get_a1_util(self.A2Deal)) / self.get_a1_util(self.A1SelfDeal)

    def get_a2_risk(self):
        return (self.get_a2_util(self.A2SelfDeal) - self.get_a2_util(self.A1Deal)) / self.get_a2_util(self.A2SelfDeal)

    @staticmethod
    def get_min_index(deal, util):
        list_ = [util[index] for index in deal]
        min_val = min(list_)
        indices = [deal[i] for i, x in enumerate(list_) if x == min_val]
        return indices

    def get_agent_min_index(self, self_deal, self_util, other_util):
        max_val = float("-inf")
        max_element = -1
        for i in self.get_min_index(self_deal, self_util):
            if other_util[i] > max_val:
                max_val = other_util[i]
                max_element = i

        return max_element

    def get_a1_min_index(self):
        return self.get_agent_min_index(self.A1SelfDeal, self.A1Util, self.A2Util)

    def get_a2_min_index(self):
        return self.get_agent_min_index(self.A2SelfDeal, self.A2Util, self.A1Util)

    def concede(self, agent):
        if self.get_a1_risk() < self.get_a2_risk():
            return "A1"
        elif self.get_a2_risk() < self.get_a1_risk():
            return "A2"
        else:
            return agent

    def new_offer(self, agent):
        if agent == "A1":
            self.remove_a1_self_deal(self.get_a1_min_index())
        if agent == "A2":
            self.remove_a2_self_deal(self.get_a2_min_index())

    def get_final_deal(self, agent):
        self.A1SelfDeal.sort()
        self.A2SelfDeal.sort()
        self.A1Deal.sort()
        self.A2Deal.sort()
        if self.agreed_deal() == "A1":
            return self.A1SelfDeal if agent == "A1" else self.A1Deal
        else:
            return self.A2SelfDeal if agent == "A2" else self.A2Deal

    def get_util_final_deal(self, agent):
        if agent == "A1":
            return self.get_a1_util(self.get_final_deal("A1"))
        else:
            return self.get_a2_util(self.get_final_deal("A2"))

    def compute_result(self):
        agent = self.initialAgent
        while not self.agreement():
            agent = self.concede(agent)
            self.new_offer(agent)

    def print_result(self):
        print("---------------------------")
        print("Initial concede:", self.initialAgent)
        print("Final Deal:", self.agreed_deal())
        print("A1:", self.get_final_deal("A1"))
        print("A2:", self.get_final_deal("A2"))
        print("A1 util:", self.get_util_final_deal("A1"))
        print("A2 util:", self.get_util_final_deal("A2"))

    def reset(self):
        self.A1SelfDeal = list(range(len(self.A1Util)))
        self.A2SelfDeal = list(range(len(self.A2Util)))
        self.A1Deal = []
        self.A2Deal = []
        self.initialAgent = "A1"

    def execute(self):
        self.compute_result()
        self.print_result()
        self.reset()


def main():
    # a1_util = [2, 2, 3]
    # a2_util = [1, 1, 2]
    a1_util = [1, 2, 2, 3, 4]
    a2_util = [4, 3, 2, 2, 2]

    strategy = ZeuthenStrategy(a1_util, a2_util)

    strategy.initialAgent = "A1"
    strategy.execute()

    strategy.initialAgent = "A2"
    strategy.execute()


if __name__ == "__main__":
    main()
