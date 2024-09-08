import re

class SmartCityBot:
    def __init__(self):
        # Define responses for various smart city topics
        self.responses = {
            'smart traffic': "Smart traffic management systems use sensors and data analytics to optimize traffic flow and reduce congestion.",
            'smart lighting': "Smart lighting systems adjust street lighting based on real-time data, such as pedestrian movement and weather conditions, to improve energy efficiency.",
            'waste management': "Smart waste management solutions involve using sensors to monitor waste levels in bins and optimize collection routes.",
            'public safety': "Smart city solutions for public safety include surveillance cameras, emergency response systems, and predictive policing technologies.",
            'energy management': "Smart energy management systems monitor and control energy use in buildings and infrastructure to increase efficiency and reduce costs.",
            'IoT': "The Internet of Things (IoT) connects various devices and sensors in a smart city to collect and analyze data for better decision-making.",
            'smart parking': "Smart parking systems use sensors to provide real-time information on available parking spaces, helping drivers find parking more easily."
        }
    
    def get_response(self, user_input):
        # Normalize user input to lowercase
        user_input = user_input.lower()
        
        # Check for keywords in user input and respond accordingly
        for key in self.responses:
            if re.search(key, user_input):
                return self.responses[key]
        
        # Default response if no keywords match
        return "Sorry, I don't have information on that topic. Can you ask about a different smart city solution?"

def main():
    bot = SmartCityBot()
    print("Hello! I'm SmartCityBot. How can I assist you with smart city solutions today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("SmartCityBot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print(f"SmartCityBot: {response}")

if __name__ == "__main__":
    main()
