import turtle
import pandas

screen = turtle.Screen()
screen.title("Special Italy Quiz")
initial_background = "sources/img/image.gif"
sicily_background = "sources/img/sicily-map.gif"
italy_background = "sources/img/italy-map.gif"
screen.setup(width=600, height=450)
screen.addshape(initial_background)
screen.addshape(sicily_background)
screen.addshape(italy_background)
turtle.shape(initial_background)


def right_guess(right_name, x, y):
    """Make the right guess be written on screen, in the correspon position of the region/province""""
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(f"{right_name}")


quiz_type = screen.textinput(title="Select your quizz", prompt="Type Italy or Sicily to start").title()
if quiz_type == "Sicily":
    turtle.shape(sicily_background)
    screen.setup(height=432, width=600)
    sicily_data = pandas.read_csv("sources/csv/sicily_provinces.csv", delimiter=";")
    sicily_provinces = sicily_data.province.to_list()
    guessed_provinces = []
    missing_provinces = []
    while len(guessed_provinces) < 9:
        user_guess = turtle.textinput(title=f"{len(guessed_provinces)}/9 right guesses",
                                      prompt="Guess a province or type 'exit' to quit:").title()
        if user_guess in sicily_provinces:
            guessed_provinces.append(user_guess)
            province_data = sicily_data[sicily_data.province == user_guess]
            province_x = int(province_data.x.iloc[0])
            province_y = int(province_data.y.iloc[0])
            right_guess(right_name=user_guess, x=province_x, y=province_y)

        if user_guess == "Exit":
            missing_provinces = [province for province in sicily_provinces if province not in guessed_provinces]
            break

    if len(guessed_provinces) == 9:
        screen.textinput(title="Well Done!", prompt="You completed the challenge, type anything to exit")
    else:
        screen.textinput(title=f"You missed {len(missing_provinces)}",
                         prompt=f"You missed the following provinces: {missing_provinces}. Type anything to exit")

elif quiz_type == "Italy":
    turtle.shape(italy_background)
    screen.setup(height=560, width=700)
    italy_data = pandas.read_csv("sources/csv/italy_regions.csv")
    italy_regions = italy_data.region.to_list()
    print(italy_regions)
    guessed_regions = []
    missing_regions = []
    while len(guessed_regions) < len(italy_regions):
        user_guess = turtle.textinput(title=f"{len(guessed_regions)}/{len(italy_regions)} right guesses",
                                      prompt="Guess a region or type 'exit' to quit:").title()
        if user_guess == "Trentino - Alto Adige" or user_guess == "Alto Adige" or user_guess == "Trentino-Alto Adige":
            user_guess = "Trentino"

        if user_guess == "Friuli" or user_guess == "Venezia" or user_guess == "Venezia Giulia" or user_guess == "Friuli - Venezia" or user_guess == "Friulia - Venezia Giulia":
            user_guess = "Friuli-Venezia Giulia"

        if user_guess in italy_regions:
            guessed_regions.append(user_guess)
            region_data = italy_data[italy_data.region == user_guess]
            region_x = int(region_data.x.iloc[0])
            region_y = int(region_data.y.iloc[0])
            right_guess(right_name=user_guess, x=region_x, y=region_y)

        if user_guess == "Exit":
            missing_regions = [region for region in italy_regions if region not in guessed_regions]
            break

    if len(guessed_regions) == len(italy_regions):
        screen.textinput(title="Well Done!", prompt="You completed the challenge, type anything to exit")
    else:
        screen.textinput(title=f"You missed {len(missing_regions)}",
                         prompt=f"You missed the following regions: {missing_regions}. Type anything to exit")
