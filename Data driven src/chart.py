import matplotlib.pyplot as plt
import csv


def chart():
    """
    Read the csv file created by main script
    Return: none
    """
    try:
        x = []
        y = []
        with open('humidity-data5.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y.append(int(row[0]))

        plt.plot(x, y, color='g', linestyle='dashed',
                 marker='o', label="Soil humidity data")

        plt.xticks(rotation=25)
        plt.xlabel('Humidity')
        plt.ylabel('Date & Time')
        plt.title('Humidity according to time')
        plt.grid()
        plt.legend()
        plt.show()
    except Exception as EX:
        print(EX.__class__.__name__)


if __name__ == "__main__":
    chart()
