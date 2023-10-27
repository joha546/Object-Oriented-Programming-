import math
import matplotlib.pyplot as plt

class Gaussian():
    """ Gaussian distribution class for calculating and
        visualizing a Gaussian distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file

        """
    def __init__(self,mu=0,sigma=1):
        self.mean=mu
        self.stdev=sigma
        self.data=[]

    def calculate_mean(self):
        """Method to calculate the mean of the data set.

                Args:
                    None

                Returns:
                    float: mean of the data set

                """
        if not self.data:
            return None
        mean = sum(self.data) / len(self.data)
        self.mean = mean
        return mean

    def calculate_stdev(self,sample=True):
        if not self.data:
            return None
        n=len(self.calculate_mean())
        mean = self.calculate_mean()
        squared_diff = [(x-mean)**2 for x in self.data]

        if sample and n>1:
            stdev=math.sqrt(sum(squared_diff)/(n-1))
        else:
            stdev=math.sqrt(sum(squared_diff)/n)
        self.stdev=stdev
        return stdev

    def read_data_file(self,file_name, sample=True):
        try:
            with open(file_name, 'r') as file:
                self.data=[float(line) for line in file]
            self.calculate_mean()
            self.calculate_stdev(sample)
        except FileNotFoundError:
            return None

    def plot_histogram(self):
        plt.hist(self.data, bins=10, density=True)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('Histogram of Data')
        plt.show()

    def pdf(self, x):
        mean = self.mean
        stdev = self.stdev
        coefficient = 1 / (stdev * math.sqrt(2 * math.pi))
        exponent = -((x - mean) ** 2) / (2 * stdev ** 2)
        return coefficient * math.exp(exponent)

