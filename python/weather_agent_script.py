# from uagents import Agent, Context
# import requests
# from uagents.setup import fund_agent_if_low
# from uagents import Agent

# alice = Agent(
#     name="alice",
#     port=8000,
#     seed="alice secret phrase",
#     endpoint=["http://127.0.0.1:8000/submit"],
# )

# fund_agent_if_low(alice.wallet.address())

# WEATHER_API_KEY = '08c460c250b97d8748a6ce35bec15ed1'
# CITY_NAME = input("Enter the city name: ")  
# min = float (input("Enter the minimum temp: "))
# max = float (input("Enter the maximum temp: "))

# weather_agent = Agent(name="weather_agent")

# @weather_agent.on_interval(period=3600) 
# async def get_weather_info(ctx: Context):
#     try:
#         response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}')
#         weather_data = response.json()
#         print(weather_data)

#         temperature = round(weather_data['main']['temp'] - 273,2)
#         weather_description = weather_data['weather'][0]['description']

#         ctx.logger.info(f'Weather in {CITY_NAME}: Temperature: {temperature}°C, Description: {weather_description}')
#         if(temperature<min ):
#             ctx.logger.info('Temprature is below minimum')
#         if(temperature>max ):
#             ctx.logger.info('Temprature is above maximum')
        
#     except Exception as e:
#         ctx.logger.error(f'Error fetching weather data: {e}')

# if __name__ == "__main__":
#     weather_agent.run()


# from uagents import Agent, Context
# import requests

# WEATHER_API_KEY = '08c460c250b97d8748a6ce35bec15ed1'

# # Create a weather agent
# weather_agent = Agent(name="weather_agent")

# @weather_agent.on_interval(period=3600) 
# async def get_weather_info(ctx: Context):
#     try:
#         CITY_NAME = ctx.get("city_name")
#         min_temp = ctx.get("min_temp")
#         max_temp = ctx.get("max_temp")

#         response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}')
#         weather_data = response.json()
#         print(weather_data)

#         temperature = round(weather_data['main']['temp'] - 273, 2)
#         weather_description = weather_data['weather'][0]['description']

#         ctx.logger.info(f'Weather in {CITY_NAME}: Temperature: {temperature}°C, Description: {weather_description}')
#         if temperature < min_temp:
#             ctx.logger.info('Temperature is below minimum')
#         if temperature > max_temp:
#             ctx.logger.info('Temperature is above maximum')
        
#     except Exception as e:
#         ctx.logger.error(f'Error fetching weather data: {e}')

# if __name__ == "__main__":
#     # Start the weather agent
#     weather_agent.run()



from uagents import Agent, Context
import requests
import json

WEATHER_API_KEY = '08c460c250b97d8748a6ce35bec15ed1'

weather_agent = Agent(name="weather_agent")

@weather_agent.on_interval(period=3600)
async def get_weather_info(ctx: Context):
    try:
        with open("user_input.json", "r") as file:
            user_input = json.load(file)

        CITY_NAME = user_input["city_name"]
        min_temp = user_input["min_temp"]
        max_temp = user_input["max_temp"]

        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}')
        weather_data = response.json()
        print(weather_data)

        temperature = round(weather_data['main']['temp'] - 273, 2)
        weather_description = weather_data['weather'][0]['description']

        ctx.logger.info(f'Weather in {CITY_NAME}: Temperature: {temperature}°C, Description: {weather_description}')
        if (temperature < min_temp):
            ctx.logger.info('Temperature is below minimum')
        if (temperature > max_temp):
            ctx.logger.info('Temperature is above maximum')

    except Exception as e:
        ctx.logger.error(f'Error fetching weather data: {e}')

if __name__ == "__main__":
    # Start the weather agent
    weather_agent.run()
