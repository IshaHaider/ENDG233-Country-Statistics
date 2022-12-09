# final_project.py
# ISHA HAIDER (30140419), ZAHWA FATIMA (30159309), PAIR L01-9, ENDG 233 F21
# A terminal based application to process and plot data based on given user input and provided csv files.
# Objective: To enable a user to retrieve and/or compare country statistics in terms of population and gross domestic product
# You must have numpy, matplotlib, and pandas installed for execution.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Country:
    '''A class used to create a Country object.

        Attributes: 
            country (str): String that represents the country's name
            code (str): String that represents country's code
            region (str): String that represents the country's UN region
            sub_region (str): String that represents the country's UN sub-region
            sq_km (int): Integer that represents the county's area in square kilometers
    '''

    def __init__(self, country, code, region, sub_region, sq_km):
        self.country = country
        self.code = code
        self.region = region
        self.sub_region = sub_region
        self.sq_km = sq_km

    def print_country_data(self):
        ''''
        Purpose: print basic country data
        Parameters: none
        Returns: none
        '''
        return ('Country Name: {}\nCountry Code: {}\nUN Region: {}\nUN Sub-Region: {}\nSq Km: {}\n'.format(self.country, self.code, self.region, self.sub_region, self.sq_km))

class Population:
    """
    A class used to create a Population object.

    Attributes:
        row (int): Index that represents the row where the country occurs in the Country_Data array
        pop_list (list): list of entire row associated with the country in the Population_Data array (country name, code, and population values over all years)
        years (list): list of all years from 2011 to 2020, inclusive
        sq_km (int): value of country's land area
    """
    def __init__(self, row, pop_list, years, sq_km):
        self.row = row
        self.pop_list = pop_list
        self.years = years
        self.sq_km = sq_km
    
    def min_pop(self):
        ''''
        Purpose: finds minimum population over ten years
        Parameters: none
        Returns: the value of minimum population 
        '''
        min_pop = min(self.pop_list[2:])
        return min_pop
    
    def max_pop(self):
        ''''
        Purpose: finds maximum population over ten years
        Parameters: none
        Returns: the value of maximum population 
        '''
        max_pop = max(self.pop_list[2:])
        return max_pop

    def range_pop(self):
        ''''
        Purpose: calculates range of population over ten years
        Parameters: none
        Returns: the value of the population range
        '''
        range_pop = self.max_pop() - self.min_pop()
        return range_pop
        
    def average_pop(self): 
        ''''
        Purpose: calculates average population over ten years
        Parameters: none
        Returns: average population
        '''
        average = sum(self.pop_list[2:])//len(self.pop_list[2:])
        return average
        
    def curr_pop(self):
        ''''
        Purpose: finds current population of country
        Parameters: none
        Returns: value of current population
        '''
        curr_pop = self.pop_list[-1]
        return curr_pop
    
    def pop_dens(self):
        ''''
        Purpose: calculates current population density of country
        Parameters: none
        Returns: value of current population density
        '''
        pop_dens = self.curr_pop()/self.sq_km
        return pop_dens

    def pop_growth_rate(self):
        ''''
        Purpose: calculates average population growth rate
        Parameters: none
        Returns: value of average population growth rate
        '''
        new_pop = self.pop_list[-1]
        old_pop = self.pop_list[2]
        pop_growth_rate = (((new_pop / old_pop) ** (1/len(self.years))) - 1) * 100
        return pop_growth_rate

class GDP:
    """
    A class used to create a GDP object.

    Attributes:
        row (int): Index that represents the row where the country occurs in the Country_Data array
        gdp_list (list): list of entire row associated with the country in the GDP_Data array (country name, code, and GDP values over all years)
        years (list): list of all years from 2011 to 2020, inclusive
    """
    def __init__(self, row, gdp_list, years):
        self.row = row
        self.gdp_list = gdp_list
        self.years = years

    def min_gdp(self):
        ''''
        Purpose: finds minimum GDP over ten years
        Parameters: none
        Returns: the value of minimum GDP 
        '''
        min_gdp = (min(self.gdp_list[2:]))/1000000
        return min_gdp
    
    def max_gdp(self):
        ''''
        Purpose: finds maximum GDP over ten years
        Parameters: none
        Returns: the value of maximum GDP 
        '''
        max_gdp = (max(self.gdp_list[2:]))/1000000
        return max_gdp

    def range_gdp(self):
        ''''
        Purpose: calculates range of GDP over ten years
        Parameters: none
        Returns: the value of the GDP range
        '''
        range_gdp = self.max_gdp() - self.min_gdp()
        return range_gdp
        
    def average_gdp(self):
        ''''
        Purpose: calculates average GDP over ten years
        Parameters: none
        Returns: average GDP
        '''
        average = (sum(self.gdp_list[2:])/len(self.gdp_list[2:]))/1000000
        return average

    def curr_gdp(self):
        ''''
        Purpose: finds current GDP of country
        Parameters: none
        Returns: value of current GDP
        '''
        curr_gdp = self.gdp_list[-1]/1000000
        return curr_gdp
        
    def gdp_growth_rate(self):
        ''''
        Purpose: calculates average GDP growth rate
        Parameters: none
        Returns: value of average GDP growth rate
        '''
        new_gdp = self.gdp_list[-1]
        old_gdp = self.gdp_list[2]
        gdp_growth_rate = (((new_gdp / old_gdp) ** (1/len(self.gdp_list[2:]))) - 1) * 100
        return gdp_growth_rate
                        
class Table:
    """
    A class used to create a Table object.

    Attributes:
        row1 (int): Index that represents the row where the first country occurs in the Country_Data array
        pop_data (array): the entire Population_Data array
        country_data (array): the entire Country_Data array
        gdp_data (array): the entire GDP_Data array
        years (list): list of all years from 2011 to 2020, inclusive
        sq_km (int): value of country's land area
        countries (list): list of all country names
        codes(list): list of all country codes
        country_name1 (str): first country input from user
        country_name2 (str): second country input from user (initially 0 if no second country is inputted)
        rowc2 (int) = Index that represents the row where the second country occurs in the Country_Data array (initially 0 if no second country is inputted)
    """
    def __init__(self, row1, pop_data, country_data, gdp_data, years, countries, codes, country_name1, country_name2 = 0, rowc2 = 0):
        self.row1 = row1
        self.pop_data = pop_data
        self.country_data = country_data
        self.gdp_data = gdp_data
        self.years = years
        self.countries = countries
        self.codes = codes
        self.country_name1 = country_name1
        self.country_name2 = country_name2
        self.rowc2 = rowc2

    def temp(self):
        ''''
        Purpose: 
            creates a list of all population data for first country and a list of all GDP data for first country;
            creates two additional lists of same type for second country only if user inputted a second country
        Parameters: none
        Returns: none
        '''
        self.pop_list = (self.pop_data.tolist())[self.row1]
        self.current_pop_year = self.years[len(self.pop_list[2:])-1]
        self.pop_print = Population(self.row1, self.pop_list, self.years, int(self.country_data[self.row1, 4]))

        self.gdp_list = (self.gdp_data.tolist())[self.row1]
        self.current_gdp_year = self.years[len(self.gdp_list[2:])-1]
        self.gdp_print = GDP(self.row1, self.gdp_list, self.years)

        # if second country was inputted, calculate second country data
        if self.rowc2 != 0: # if rowc2 not equal to 0, an argument with second country row index was passed
            self.pop_list2 = (self.pop_data.tolist())[self.rowc2]
            self.pop_print2 = Population(self.rowc2, self.pop_list2, self.years, int(self.country_data[self.rowc2, 4]))

            self.gdp_list2 = (self.gdp_data.tolist())[self.rowc2]
            self.gdp_print2 = GDP(self.rowc2, self.gdp_list2, self.years)            

    def gdp_per_capita(self):
        ''''
        Purpose: 
            calculates average gdp per capita for desired country;
            calculates average gdp per capita for second country if comparison indicated
        Parameters: none
        Returns: average gdp per capita
        '''
        self.gdp_per_capita = (self.gdp_print.average_gdp() * 1000000) / self.pop_print.average_pop()
        if self.rowc2 != 0: 
            self.gdp_per_capita2 = (self.gdp_print2.average_gdp() * 1000000) / self.pop_print2.average_pop()
        return self.gdp_per_capita 

    def print_all_data(self):
        ''''
        Purpose: prints all statistics in a table if user chose one country (no comparison)
        Parameters: none
        Returns: none
        '''
        old_year = self.years[0]
        
        print()
        print('{:<40}{:<25}{:<10}'.format('Statistic', self.country_name1, 'Units'))
        print('-' * 80)
        print('POPULATION STATS')
        print('-' * 30)
        print('{:<40}{:<25}{:<10}'.format('Minimum Population', self.pop_print.min_pop(), 'people'))
        print('{:<40}{:<25}{:<10}'.format('Maximum Population', self.pop_print.max_pop(), 'people'))
        print('{:<40}{:<25}{:<10}'.format('Range of Population', self.pop_print.range_pop(), 'people'))
        print('{:<40}{:<25}{:<10}\n'.format('Average Population', self.pop_print.average_pop(), 'people'))
            
        print('{:<40}{:<25}{:<10}'.format('Current Population', self.pop_print.curr_pop(), 'people'))
        print(f'as of {self.current_pop_year}\n')

        print('{:<40}{:<25.2f}{:<10}'.format('Current Population Density', self.pop_print.pop_dens(), 'people per'))
        print('as of {:<49}{:<10}{:<10}\n'.format(self.current_pop_year, ' ', 'square km'))

        print('{:<40}{:<25.2f}{:<10}'.format('Population Growth Rate', self.pop_print.pop_growth_rate(), '%'))
        print('from {} to {}\n'.format(old_year, self.current_gdp_year))

        print('GROSS DOMESTIC PRODUCT STATS')
        print('-' * 30)

        print('{:<40}{:<25.2f}{:<10}'.format('Minimum GDP', self.gdp_print.min_gdp(), 'million USD'))
        print('{:<40}{:<25.2f}{:<10}'.format('Maximum GDP', self.gdp_print.max_gdp(), 'million USD'))
        print('{:<40}{:<25.2f}{:<10}'.format('Range of GDP', self.gdp_print.range_gdp(), 'million USD'))
        print('{:<40}{:<25.2f}{:<10}\n'.format('Average GDP', self.gdp_print.average_gdp(), 'million USD'))
            
        print('{:<40}{:<25.2f}{:<10}'.format('Current GDP', self.gdp_print.curr_gdp(), 'million USD'))
        print(f'as of {self.current_gdp_year}\n')

        print('{:<40}{:<25.2f}{:<10}'.format('GDP Growth Rate', self.gdp_print.gdp_growth_rate(), '%'))
        print('from {} to {}\n'.format(old_year, self.current_gdp_year))

        print('{:<40}{:<25.2f}{:<10}\n'.format('Average GDP per capita', self.gdp_per_capita, 'million USD'))
        print('-' * 80)
        print()
    
    def compare_data(self):
        ''''
        Purpose: prints all statistics in a table if user chose two countries (comparison)
        Parameters: none
        Returns: none
        '''
        old_year = self.years[0]

        print()
        print('{:<40}{:<25}{:<25}{:<10}'.format('Statistic', self.country_name1, self.country_name2, 'Units'))
        print('-' * 105)
        print('POPULATION STATS')
        print('-' * 30)
        print('{:<40}{:<25}{:<25}{:<10}'.format('Minimum Population', self.pop_print.min_pop(), self.pop_print2.min_pop(), 'people'))
        print('{:<40}{:<25}{:<25}{:<10}'.format('Maximum Population', self.pop_print.max_pop(), self.pop_print2.max_pop(), 'people'))
        print('{:<40}{:<25}{:<25}{:<10}'.format('Range of Population', self.pop_print.range_pop(), self.pop_print2.range_pop(),'people'))
        print('{:<40}{:<25}{:<25}{:<10}\n'.format('Average Population', self.pop_print.average_pop(), self.pop_print2.average_pop(), 'people'))
            
        print('{:<40}{:<25}{:<25}{:<10}'.format('Current Population', self.pop_print.curr_pop(), self.pop_print2.curr_pop(),'people'))
        print(f'as of {self.current_pop_year}\n')

        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Current Population Density', self.pop_print.pop_dens(), self.pop_print2.pop_dens(),'people per'))
        print('as of {:<84}{:<10}\n'.format(self.current_pop_year,'square km'))

        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Population Growth Rate', self.pop_print.pop_growth_rate(), self.pop_print2.pop_growth_rate(),'%'))
        print('from {} to {}\n'.format(old_year, self.current_gdp_year))


        print('GROSS DOMESTIC PRODUCT STATS')
        print('-' * 30)

        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Minimum GDP', self.gdp_print.min_gdp(), self.gdp_print2.min_gdp(),'million USD'))
        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Maximum GDP', self.gdp_print.max_gdp(), self.gdp_print2.max_gdp(),'million USD'))
        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Range of GDP', self.gdp_print.range_gdp(), self.gdp_print2.range_gdp(), 'million USD'))
        print('{:<40}{:<25.2f}{:<25.2f}{:<10}\n'.format('Average GDP', self.gdp_print.average_gdp(), self.gdp_print2.average_gdp(), 'million USD'))
            
        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('Current GDP', self.gdp_print.curr_gdp(), self.gdp_print2.curr_gdp(),'million USD'))
        print(f'as of {self.current_gdp_year}\n')

        print('{:<40}{:<25.2f}{:<25.2f}{:<10}'.format('GDP Growth Rate', self.gdp_print.gdp_growth_rate(), self.gdp_print2.gdp_growth_rate(), '%'))
        print('from {} to {}\n'.format(old_year, self.current_gdp_year))

        print('{:<40}{:<25.2f}{:<25.2f}{:<10}\n'.format('Average GDP per capita', self.gdp_per_capita, self.gdp_per_capita2,'million USD'))
        print('-' * 105)
        print()

def print_countries_sub_regions(user_region, sub_regions, countries, codes):
    ''''
    Purpose: print all country names and codes corresponding to desired sub-region
    Parameters:
        user_region - user input for sub region 
        sub_regions - list of all sub regions
        countries - list of all country names
        codes - list of all country codes
    Returns: none
    '''
    print(f'\nCountries and their Corresponding Codes in {user_region}:')
    indices_regions = [x for x in range(len(sub_regions)) if sub_regions[x] == user_region]
    list_countries = [countries[x] for x in indices_regions]
    list_codes = [codes[x] for x in indices_regions]
    for x in list_countries:
        print(f'• {x}: {list_codes[list_countries.index(x)]}')
    print()

def bar_graph_country(user_region, country_name, countries, codes, country_data, pop_data, gdp_data, years):
    ''''
    Purpose: outputs bar graph for all countries within sub-region(s) as a function of their respective average gdp per capita
    Parameters:
        user_region - user input for sub region 
        country_name - name of country inputted from user
        countries - list of all country names
        codes - list of all country codes
        country_data - the entire Country_Data array
        pop_data - the entire Population_Data array
        gdp_data - the entire GDP_Data array
        years - list of all years from 2011 to 2020, inclusive
    Returns: none
    '''
    countries_in_subregion1 = [i for i in countries if country_data[countries.index(i)][3] == user_region] # list of countries in sub-region
    avg_gdp_cap1 = [] # list of average gdp per capita in each country within sub-region   
    for x in countries_in_subregion1:
        tablex = Table(countries.index(x), pop_data, country_data, gdp_data, years, countries, codes, country_name)
        tablex.temp()
        avg_gdp_cap1.append(tablex.gdp_per_capita())
    
    avg_gdp_cap_country1 = sorted(avg_gdp_cap1)

    plt.title(f'Countries in {user_region} vs. GDP per Capita')
    plt.bar(countries_in_subregion1, avg_gdp_cap_country1)
    xlabels = countries_in_subregion1.copy()
    xlabels_new = [label.replace(' ', ' \n') for label in xlabels]
    plt.xticks(countries_in_subregion1, xlabels_new, rotation = 'vertical')
    plt.tight_layout()
    plt.ylabel('GDP per Capita')


def line_graph_country(country_name1, countries, pop_data, gdp_data, years, years_label, country_name2 = 0):
    ''''
    Purpose: outputs line graph for change in GDP and population between 2011 - 2020 for one (no comparison) or two countries (comparison was indicated)
    Parameters:
        country_name1 - name of first country inputted from user
        countries - list of all country names
        pop_data - the entire Population_Data array
        gdp_data - the entire GDP_Data array
        years - list of all years from 2011 to 2020, inclusive, as integers
        years_label - list of all years from 2011 to 2020, inclusive, as string objects
        country_name2 - name of second country inputted from user (initially 0 if no second country is inputted)
    Returns: none
    '''
    gdp_data_country1 = (gdp_data[countries.index(country_name1)][2:]) / 10000000000
    if country_name2 != 0: # if country_name2 not equal to 0, an argument with second country was passed
        gdp_data_country2 = (gdp_data[countries.index(country_name2)][2:]) / 10000000000

    plt.subplot(2,1,1)
    plt.title('Years vs. GDP/Population')
    plt.plot(years, gdp_data_country1, 'o-', label=country_name1)
    if country_name2 != 0: # if comparison indicated, plot second country data
        plt.plot(years, gdp_data_country2, 'o-', label=country_name2)
    plt.xticks(years, years_label, rotation = 'horizontal')
    plt.xlabel('Years')
    plt.ylabel('GDP (USD x 1E10)')
    plt.legend(shadow=True, loc='best')

    pop_data_country1 = (pop_data[countries.index(country_name1)][2:]) / 1000000 
    if country_name2 != 0:
        pop_data_country2 = (pop_data[countries.index(country_name2)][2:]) / 1000000 

    plt.subplot(2,1,2)
    plt.plot(years, pop_data_country1, 'o-', label=country_name1)
    if country_name2 != 0:
        plt.plot(years, pop_data_country2, 'o-', label=country_name2) 
    plt.xticks(years, years_label, rotation = 'horizontal')
    plt.xlabel('Years')
    plt.ylabel('Population (people x 1E6)')
    plt.legend(shadow=True, loc='best')


def main():
    # import data 
    country_data1 = pd.DataFrame(pd.read_csv('Country_Data.csv', sep = ','))
    pop_data1 = pd.DataFrame(pd.read_csv('Population_Data.csv', sep = ','))
    gdp_data1 = pd.DataFrame(pd.read_csv('Country_GDP.csv', sep = ','))

    country_data = np.array(country_data1)
    pop_data = np.array(pop_data1)
    gdp_data = np.array(gdp_data1)

    # get list of countries and country codes
    sub_regions = list(country_data[:,3])
    countries = list(country_data[:,0])
    codes = list(country_data[:,1])


    print('\nENDG 233 Country Statistics\n')
    print('UN Sub-Regions:') # print all UN Sub-Regions
    set_regions = set(sub_regions)
    for x in sorted(set_regions):
        print(u'•', x) 
    user_region1 = input('\nPlease enter a UN sub-region from the above list: ') # prompt user for first UN Sub-Region
    region_loop1 = ''

    # user input
    while region_loop1 != 'end': # loop until valid sub-region inputted
        if user_region1 in sub_regions: # check if user-specified sub-region exists or else re-prompt user
            print_countries_sub_regions(user_region1, sub_regions, countries, codes) # call function to show all countries within user-specified sub-region
            user_country1 = input('Please enter a valid country name or country code within the specified sub-region: ') # prompt user for first country within user-specified sub-region
            country_loop1 = ''

            while country_loop1 != 'end': # loop until valid country inputted
                # assign first country name
                if user_country1 in countries: # if inputted user country is the country name
                    country_name1 = user_country1
                elif user_country1 in codes: # if inputted user country is the country code
                    country_name1 = countries[codes.index(user_country1)]
                else: #if invalid input
                    print('You must enter a valid country name or country code: ') 
                    user_country1 = input('Please enter a valid country name or country code: ')
                    continue
                
                row1 = countries.index(country_name1) # find index of row with first user-specified country data for following operations
                
                if country_data[row1, 3] == user_region1: # check if inputted country name or code is in specified sub-region
                    country1 = Country(country_name1, codes[row1], country_data[row1, 2], country_data[row1, 3], int(country_data[row1, 4])) # create class instance for first country
                    user_region2 = input('\nPlease enter another UN sub-region from the above list for comparison (enter SAME for previous sub-region, N/A for no comparison): ') # prompt user for second sub-region, providing option for no comparison or previous sub-region
                    region_loop2 = ''

                    while region_loop2 != 'end':
                        if user_region2 in sub_regions or user_region2 == 'SAME':
                            if user_region2 in sub_regions: # if second sub-region is different from first, call function to print all countries within user's second sub-region
                                print_countries_sub_regions(user_region2, sub_regions, countries, codes) 
                            elif user_region2 == 'SAME': # if second sub-region is same ad first, assign user_region2 as first
                                user_region2 = user_region1

                            user_country2 = input('Please enter a valid country name or country code within the specified sub-region: ') # prompt for second country within specified sub-region
                            country_loop2 = ''

                            while country_loop2 != 'end':
                                # assign second country
                                if user_country2 in countries: # if inputted user country is the country name
                                    country_name2 = user_country2
                                elif user_country2 in codes: # if inputted user country is the country code
                                    country_name2 = countries[codes.index(user_country2)]
                                else: #invalid input
                                    print('You must enter a valid country name or country code')
                                    user_country2 = input('Please enter a valid country name or country code within the specified sub-region: ')
                                    continue
                                
                                row2 = countries.index(country_name2) # find index of row with second user-specified country data for following operations
                            
                                if country_data[row2, 3] == user_region2: # check if second user_specified country is in specified sub-region
                                    country2 = Country(country_name2, codes[row2], country_data[row2, 2], country_data[row2, 3], int(country_data[row2, 4])) # create class instance for second country
                                    
                                    print("\n***Requested Country Data***\n")
                                    country1_prop = country1.print_country_data().split('\n') # make each country data property into token
                                    country2_prop = country2.print_country_data().split('\n') # tokens in these two lists correspond in terms of property (i.e first token is country name in both lists)

                                    format_string = '{country1:<50}{country2:<50}' # format to print country data side by side only if country comparison is indicated by user
                                    print(format_string.format(country1 = 'COUNTRY 1', country2 = 'COUNTRY 2'))
                                    print(format_string.format(country1 = '-' * 48, country2 = '-' * 48))
                                    for i in range(len(country1_prop)): # use list of tokens to print country data properties side by side for two countries (can use same index as order of tokens in both lists correspond to specific country data property)
                                        print(format_string.format(country1 = country1_prop[i], country2 = country2_prop[i]))
                                    
                                    country_loop2 = 'end'
                                else: # valid country input, but not in specified subregion
                                    print('You must enter a country name or country code within the specified sub-region')
                                    user_country2 = input('Please enter a valid country name or country code within the specified sub-region: ')
                                    continue

                            region_loop2 = 'end'
                        elif user_region2 == 'N/A':
                            print("\n***Requested Country Data***\n")
                            print(country1.print_country_data())
                            
                            region_loop2 = 'end'
                        else:
                            print('You must enter a valid UN sub-region: ') 
                            user_region2 = input('Please enter a UN sub-region: ')

                    country_loop1 = 'end'
                else: #valid input, but not in subregion 
                    print('You must enter a country name or country code within the specified sub-region')
                    user_country1 = input('Please enter a valid country name or country code within the specified sub-region: ')
                    continue
            
            region_loop1 = 'end'
        else:
            print('You must enter a valid UN sub-region: ') 
            user_region1 = input('Please enter a UN sub-region: ')
        
    # BASIC DATA PROCESSING
    years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

    # print all calculations using given class Population and class GDP
    if user_region2 != 'N/A': # if comparison is desired, extra column is printed with second country's data
        table1 = Table(row1, pop_data, country_data, gdp_data, years, countries, codes, country_name1, country_name2 = country_name2, rowc2 = row2)
        table1.temp()
        table1.gdp_per_capita()
        table1.compare_data() 
    else: # no comparison desired, and only first country's data is printed
        table1 = Table(row1, pop_data, country_data, gdp_data, years, countries, codes, country_name1)     
        table1.temp()
        table1.gdp_per_capita()
        table1.print_all_data()
    print('\nThe figures will now display.\nThank you for using our program!\n')
    
    # PLOTTING

    years_label = ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

    # graph 1 - plot of all countries within sub-region(s) as a function of their respective average gdp per capita as a bar graph
    plt.figure('Sub-Region(s) vs. GDP per Capita')
    if user_region2 == 'N/A' or user_region2 == user_region1: # if no comparison indicated or if second sub-region is same as first
        bar_graph_country(user_region1, country_name1, countries, codes, country_data, pop_data, gdp_data, years)
    elif user_region2 != 'N/A' and user_region2 != user_region1: # if different second subregion that from first
        plt.subplot(1,2,1)
        bar_graph_country(user_region1, country_name1, countries, codes, country_data, pop_data, gdp_data, years)
        plt.subplot(1,2,2)
        bar_graph_country(user_region2, country_name2, countries, codes, country_data, pop_data, gdp_data, years)

    # graph 2 - plot change in GDP and population between 2011 - 2020 for one or two countries if comparison was indicated
    plt.figure('Years vs. GDP/Population')
    if (user_region2 != 'N/A'):
        line_graph_country(country_name1, countries, pop_data, gdp_data, years, years_label, country_name2 = country_name2)
    else:
        line_graph_country(country_name1, countries, pop_data, gdp_data, years, years_label)

    plt.show()

if __name__ == '__main__':
    main()
    