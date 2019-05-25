import numpy as np
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox


class MainClass(object):
    def __init__(self):
        self.main()

    def main(self):
        Tk().withdraw()
        filename = filedialog.askopenfilename()

        try:
            data1 = np.genfromtxt(filename, dtype=None, delimiter=',', names=True, skip_header=0)
        except:
            string = "The File:\n"
            string += filename + "\n"
            string += "is not a valid data file!"
            messagebox.showerror("File Open Error", string)

        print(len(data1))

        Timestamp = data1['Timestamp']
        Name = data1['Name']
        entry1 = data1['Robby_Albreicht']
        entry2 = data1['Jack_Baker']
        entry3 = data1['Josh_Blamer']
        entry4 = data1['Ray_Carofano']
        entry5 = data1['Connor_Cummings']
        entry6 = data1['John_Delmastro']
        entry7 = data1['Joey_Dinko']
        entry8 = data1['Charlie_Fink']
        entry9 = data1['Alex_Glatz']
        entry10 = data1['Dante_Grecco']
        entry11 = data1['Thomas_Hankey']
        entry12 = data1['Thomas_Koss']
        entry13 = data1['Anton_Molnar']
        entry14 = data1['Jonathan_Ockunzzi']
        entry15 = data1['Max_Winebrake']

        """
        entryArray = [entry1, entry2, entry3,
                      entry4, entry5, entry6,
                      entry7, entry8, entry9,
                      entry10, entry11, entry12,
                      entry13, entry14, entry15]

        phikeia_array = [None] * len(Name)
        x = 0
        for y in Name:
            phikeia_array[x] = PhikeiaData(entryArray[x], str(Name[x]))
            x += 1
        """

        entry1Total = PhikeiaData(entry1, "Robby Albreicht")
        entry2Total = PhikeiaData(entry2, "Jack Baker")
        entry3Total = PhikeiaData(entry3, "Josh Blamer")
        entry4Total = PhikeiaData(entry4, "Ray Carofano")
        entry5Total = PhikeiaData(entry5, "Connor Cummings")
        entry6Total = PhikeiaData(entry6, "John Delmastro")
        entry7Total = PhikeiaData(entry7, "Joey Dinko")
        entry8Total = PhikeiaData(entry8, "Charlie Fink")
        entry9Total = PhikeiaData(entry9, "Alex Glatz")
        entry10Total = PhikeiaData(entry10, "Dante Grecco")
        entry11Total = PhikeiaData(entry11, "Thomas Hankey")
        entry12Total = PhikeiaData(entry12, "Thomas Koss")
        entry13Total = PhikeiaData(entry13, "Anton Molnar")
        entry14Total = PhikeiaData(entry14, "Jonathan Ockunzzi")
        entry15Total = PhikeiaData(entry15, "Max Winebrake")

        phikeia_array = [entry1Total, entry2Total, entry3Total,
                         entry4Total, entry5Total, entry6Total,
                         entry7Total, entry8Total, entry9Total,
                         entry10Total, entry11Total, entry12Total,
                         entry13Total, entry14Total, entry15Total]

        phikeia_array_sorted = sorted(phikeia_array)

        for x in range(len(phikeia_array_sorted)):
            phikeia_array_sorted[x].set_position(x + 1)

        print(phikeia_array_sorted)

        brother_list = [None] * len(Name)

        for x in range(len(Name)):
            brother_guess = [entry1[x], entry2[x], entry3[x], entry4[x],
                             entry5[x], entry6[x], entry7[x], entry8[x],
                             entry9[x], entry10[x], entry11[x], entry12[x],
                             entry13[x], entry14[x], entry15[x]]
            brother_list[x] = (BrotherData(brother_guess, str(Name[x]), phikeia_array))

        brother_list_sorted = sorted(brother_list)

        print(brother_list_sorted)


# this is a class that stores the phikeia name and their respective score in one data type
# it also implements the comparable data methods for sorting
class PhikeiaData(object):
    def __init__(self, scores, name):
        self._scores = scores
        self._score = 0
        self._name = name
        self._position = 0

        self._minIndex = -1
        self._maxIndex = -1

        self.normalize()
        self.total_calculator()

    def get_score(self):
        return self._score

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def total_calculator(self):
        self._score = 0
        for x in range(len(self._scores)):
            if x != self._minIndex and x != self._maxIndex:
                self._score += self._scores[x]

        self._score = self._score / (len(self._scores) - 2)

    def normalize(self):
        maxIndex = 0
        minIndex = 0
        for x in range(len(self._scores)):
            if self._scores[x] > self._scores[maxIndex]:
                maxIndex = x

            if self._scores[x] < self._scores[minIndex]:
                minIndex = x

        self._maxIndex = maxIndex
        self._minIndex = minIndex

    def __eq__(self, other):
        return self._score == other.get_score()

    def __ne__(self, other):
        return self._score != other.get_score()

    def __lt__(self, other):
        return self._score < other.get_score()

    def __le__(self, other):
        return self._score <= other.get_score()

    def __gt__(self, other):
        return self._score > other.get_score()

    def __ge__(self, other):
        return self._score >= other.get_score

    def __repr__(self):
        return str(self._name) + " with a score of " + str(self._score) + ", \n\tnormalized scores: " + str(
            self._scores[self._minIndex]) + " and: " + str(
            self._scores[self._maxIndex]) + "\n"

    def __str__(self):
        return str(self._name) + " with a score of " + str(self._score) + ", \n\tnormalized scores: " + str(
            self._scores[self._minIndex]) + " and: " + str(
            self._scores[self._maxIndex]) + "\n"


class BrotherData(object):
    def __init__(self, list, name, phikiealist):
        self._list = list
        self._name = name
        self._phikeialist = phikiealist
        self._offscore = 0

        self.calculate_offscore()

    def calculate_offscore(self):
        self._offscore = 0
        for x in range(len(self._phikeialist)):
            self._offscore += abs(self._list[x] - self._phikeialist[x].get_position())

        self._offscore = self._offscore / len(self._list)

    def get_offscore(self):
        return self._offscore

    def __eq__(self, other):
        return self._offscore == other.get_offscore()

    def __ne__(self, other):
        return self._offscore != other.get_offscore()

    def __lt__(self, other):
        return self._offscore < other.get_offscore()

    def __le__(self, other):
        return self._offscore <= other.get_offscore()

    def __gt__(self, other):
        return self._offscore > other.get_offscore()

    def __ge__(self, other):
        return self._offscore >= other.get_offscore()

    def __repr__(self):
        return str(self._name) + " has a score " + str(self._offscore) + "\n"

    def __str__(self):
        return str(self._name) + " has a score " + str(self._offscore) + "\n"


if __name__ == "__main__":
    t = MainClass()
