from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox


class Phikeia:
    def __init__(self, _name):
        """
        Constructor
        :param _name: the name of the phikeia
        """
        self._name = _name
        self._scores = []
        self._average = 0

    def __str__(self):
        return str(self._name) + " average: " + str(self._average) + "\n"

    def __repr__(self):
        return str(self._name) + " average: " + str(self._average) + "\n"

    def add_score(self, score):
        """
        Adds a score to the local scores list
        :param score: new score to add
        :return: nothing
        """
        self._scores.append(score)

    def calculate_average(self, total_num):
        """
        Calculates the average given a total
        sets the local average to what is calculated
        :param total_num: total number to divide by
        :return: nothing
        """
        sum = 0
        for score in self._scores:
            sum += int(score)

        self._average = sum / total_num

    def get_average(self):
        """
        Returns the local average
        :return: self._average
        """
        return self._average


if __name__ == "__main__":
    Tk().withdraw()
    filename = filedialog.askopenfilename(title="Open .csv file")

    try:
        data = open(filename, 'r')
    except:
        string = "The File:\n"
        string += filename + "\n"
        string += "is not a valid data file!"
        messagebox.showerror("File Open Error", string)
        exit(1)

    first_line = data.readline().split(',')

    phikeias = []
    for name in first_line:
        name = name.replace("\n", "")
        if not name.__contains__('Timestamp') and not name.__contains__('Name'):
            phikeias.append(Phikeia(name))

    brother_total = 0
    # go through the rest of the lines and add the scores to the corresponding phikeia
    for line in data:
        line = line.replace("\n", "")
        line_split = line.split(',')

        for x in range(2, len(line_split)):
            phikeias[x - 2].add_score(line_split[x])

        brother_total += 1

    for phikeia in phikeias:
        phikeia.calculate_average(brother_total)

    phikeias = sorted(phikeias, key=lambda phikeia: phikeia.get_average())

    final_string = ""
    for phikeia in phikeias:
        final_string += str(phikeia)
    messagebox.showinfo(title="Results", message=final_string)
