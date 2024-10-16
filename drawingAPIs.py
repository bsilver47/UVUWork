import tkinter as tk
from urllib.request import urlopen
from PIL import Image, ImageTk
from io import BytesIO
from munch import DefaultMunch
import requests

# the url in this request is what pulls the data from the NOAA Weather Service at a specific location and can be replaced by URLs that follow the same pattern of different locations
response = requests.get("https://api.weather.gov/gridpoints/SLC/103,150/forecast/hourly")

# this section adapts the data from response to a usable format
jsonJson = DefaultMunch.fromDict(response.json())
periods = jsonJson.properties.periods
url = periods[1].icon
url = url.split(',', 1)[0]

# this section prepares the messages that will be printed
temp = "The Temperature will soon be " + str(periods[1].temperature) + str(periods[1].temperatureUnit) + "\n"
wind = "with wind speeds of " + str(periods[1].windspeed) + "\n"
precip = "and a percent of precipitation of " + str(periods[1].probabilityOfPrecipitation.value) + "\n"

# this section prepares the graphic window and inserts the image
root = tk.Tk()
root.title("Weather")
image_data = urlopen(url).read()
image = Image.open(BytesIO(image_data))
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

# this section inserts the text into the window
text = tk.Text(root, width=40, height=10)
text.pack()
text.insert(tk.END, temp)
text.insert(tk.END, wind)
text.insert(tk.END, precip)

# this line is what produces and maintains the window until closed
root.mainloop()
