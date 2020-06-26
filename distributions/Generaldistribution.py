class Distribution:
    def __init__(self, mu=0, sigma=1):
    
        """ Distribution class for calculating and 
        visualizing a probability distribution.
    
        Attributes:
            mu represents the mean value of the distribution
            sigma represents the standard deviation of the distribution
            data_list a list of floats extracted from the data file
        """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []

def read_data_file(self, file_name):
   
        """Function to read in data from a txt file. The txt file should have
        one number per line. The numbers are stored in the data attribute.
                
        Args:
            file_name: name of a file to read from

        """
            
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()
    
        self.data = data_list
    
