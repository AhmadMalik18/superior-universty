class ModelbasedReflexAgent:
    def __init__ (self):
        self.previous_action = None
        self.comfortable_range = (15,11)

    def decide_action(self, current_temperature):
        if self.previous_action is None:
            self.previous_action = "off"
        if current_temperature < self.comfortable_range[0]:
            if self.previous_action != "on":
                self.previous_action = "on"
                print("heater turned on")
            else:
                 print("heater alreadyon, no action needed")
        elif current_temperature > self.comfortable_range[1]:
            if self.previous_action != "off":
                self.previous_action = "off"
                print("heater turned off")
            else:
                print("heater already off, no action needed")
        else:
            print(f"Temperature is {current_temperature}, no action needed")

agent = ModelbasedReflexAgent()
agent.decide_action(18)
agent.decide_action(56)
agent.decide_action(10)
agent.decide_action(34)
agent.decide_action(15)



