class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
temp_celsius = 35
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is {temp_fahrenheit}°F")