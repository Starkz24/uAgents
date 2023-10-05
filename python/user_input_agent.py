# from uagents import Agent, Context
# import requests

# user_input_agent = Agent(name="user_input_agent")

# @user_input_agent.on_interval(period=3600) 
# async def get_user_input(ctx: Context):
#     try:
#         CITY_NAME = input("Enter the city name: ")  
#         min_temp = float(input("Enter the minimum temp: "))
#         max_temp = float(input("Enter the maximum temp: "))

#         ctx.logger.info(f'City: {CITY_NAME}, Min Temp: {min_temp}, Max Temp: {max_temp}')

#         # Pass user input to the weather agent
#         weather_agent = ctx.agent("weather_agent")
#         weather_agent.update_context(city_name=CITY_NAME, min_temp=min_temp, max_temp=max_temp)

#     except Exception as e:
#         ctx.logger.error(f'Error getting user input: {e}')

# if __name__ == "__main__":
#     user_input_agent.run()


import json

CITY_NAME = input("Enter the city name: ")
min_temp = float(input("Enter the minimum temp: "))
max_temp = float(input("Enter the maximum temp: "))

user_input = {
    "city_name": CITY_NAME,
    "min_temp": min_temp,
    "max_temp": max_temp
}

with open("user_input.json", "w") as file:
    json.dump(user_input, file)
