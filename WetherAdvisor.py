def provide_weather_advisory(temperature):
    if temperature < 0:
        return "It's freezing! Wear a heavy coat."
    elif temperature >= 0 and temperature <= 10:
        return "It's cold! Bundle up."
    elif temperature >= 11 and temperature <= 20:
        return "It's cool! A light jacket will do."
    else:
        return "It's warm! Enjoy the day."
 
print(provide_weather_advisory(15))  # Output: "It's cool! A light jacket will do."