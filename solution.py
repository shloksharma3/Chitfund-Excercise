import pandas as pd
import numpy as np

class ChitFund:
    def __init__(self, filename):
        self.df = pd.read_csv(filename)
        self.totalReturn = self.total_return()

    def total_return(self):
        bid_return = np.array(self.df['Net amount recd by Bid winner'])
        each_month_return = np.array(self.df['Amount returned to everyone in the group'])
        for i in each_month_return:
            bid_return += i
        return bid_return

    def annual_return(self):
        temp = self.totalReturn * (12/25)
        return temp

    def return_percentage(self):
        temp = self.totalReturn * (100 / 50000)
        return temp

    def show_data(self, size):
        print(self.df.head(size))



def main():
    C1 = ChitFund('input.csv')

    C1.df['Total Return'] = C1.totalReturn
    C1.df['Annualized Return'] = C1.annual_return()
    C1.df['Return Percentage'] = C1.return_percentage()
    print('Annualized  Return of the person who bids in the last month is: {}'.format(list(C1.df['Annualized Return'])[-1]))
    print('Annualized Return of the person who bids in the first month is: {}'.format(list(C1.df['Annualized Return'])[0]))
    C1.show_data(5)
    C1.df.to_csv('output.csv')


if __name__ =='__main__':
    main()