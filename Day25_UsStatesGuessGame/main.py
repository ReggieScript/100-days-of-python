import pandas
import turtle
from pandas import DataFrame as df


### SQUIRREL CENSUS PRACTICE ###

# data=pandas.read_csv(r"Day25_PandasAnalysis\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color=data["Primary Fur Color"].value_counts()
# color_fur=df(color.reset_index())
# color_fur=color_fur.rename(columns={"index":"Fur Color","Primary Fur Color":"counts"})
# color_fur.to_csv("Day25_PandasAnalysis\output")

## MISTAKES

# Missing a way to save the correct values after another round is played with the save file option


screen = turtle.Screen()
screen.title("Guess the states!")

image_file = r"Day25_UsStatesGuessGame\blank_states_img.gif"

screen.addshape(image_file)
turtle.shape(image_file)

states_complete = pandas.read_csv(r"Day25_UsStatesGuessGame\50_states.csv")


def write_states(name, xcor, ycor):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("black")
    t.goto(xcor, ycor)
    t.write(name)


game_mode = screen.textinput(title="Choose your gamemode",
                             prompt="Type 'new' for a new game. Type 'savefile' if you want to continue guessing your old game.")
if game_mode == 'new':
    states = states_complete
elif game_mode== 'savefile':
    states = pandas.read_csv(r'Day25_UsStatesGuessGame\MissingStates')
    correct_states = pandas.read_csv(r"Day25_UsStatesGuessGame\CorrectStates.csv")
    for item in correct_states["state"]:
        xcord = states_complete.loc[(
            states_complete["state"] == item)].x.tolist()[0]
        ycord = states_complete[(states_complete["state"] == item)].y.tolist()[
            0]
        write_states(item, xcord, ycord)


correct_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title="Guess the state:", prompt="Name a state")
    if states["state"].str.contains(answer_state).any():

        correct_states.append(answer_state)

        answer_data = states.loc[states["state"] == answer_state]

        xcord = answer_data["x"].tolist()[0]
        ycord = answer_data["y"].tolist()[0]

        write_states(answer_state, xcord, ycord)

    if answer_state == 'exit':
        game_is_on = False

missing_states = states

print(correct_states)

correct_states= missing_states[missing_states.state.isin(
    correct_states) == True]
missing_states = missing_states[missing_states.state.isin(
    correct_states) == False]


correct_states.to_csv("Day25_UsStatesGuessGame\CorrectStates.csv")
missing_states.to_csv("Day25_UsStatesGuessGame\MissingStates.csv")

turtle.mainloop()
