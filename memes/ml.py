import subprocess


def doMachineLearning():
    """ Uses machine learning algorithms to procure a placement. """

    print("You got placed for a job in Machine Learning")
    VICTORY_MUSIC = 'assets/music/victory.wav'
    subprocess.call(['ffplay', "-nodisp", "-autoexit",
                     "-hide_banner", "-loglevel", "quiet", VICTORY_MUSIC])


def getPersonalisedGreeting(name):
    """ Uses machine learning algorithms to generate a personalised message for the user. """

    return ("Hello " + name)


if __name__ == "__main__":
    doMachineLearning()
