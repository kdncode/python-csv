import csv, re

results = []

with open('sum.csv') as csvfile:
    
    newCsv = csv.reader(csvfile)

    for row in newCsv:
        
        for line in row:

            numbers = line.split('/')

            # print(numbers)
            numbers = [float(i) for i in numbers]       

            results.append(numbers)

            # Average
            average = [sum(x) for x in zip(*results)]
            average = average[0] / 6

            
        print('*****AVERAGE')
        print(round(average, 2))
        print('\n')

        print('*****RESULTS')
        print(results)
        print('\n')
    # for column in newCsv:
    # Value 

        for i in results:

            print(i)

            value = results[0][0]
            print('Value')
            print(round(value, 2)) 

            # Delta 1 (+ || -)
            delta1 = value - average
            print('Delta 1')
            print(round(delta1, 2)) 

            # Delta 2 (+ || -)
            delta2 = abs(delta1) - 394.60
            print('Delta 2')
            print(round(delta2, 2)) 

            # Delta 3 (+ || -)
            delta3 = 100 * (float(delta2) / value)
            print('Delta 3')
            print(round(delta3, 2))

            ''' Compare data '''
            if value > 100 and delta1 < 0 and delta3 >= 20:
                print('Yellow')
                print('\n')
            elif value > 100 and delta1 > 0 and delta3 >= 20:
                print('Red')
                print('\n')
            else:
                print('Gray')
                print('\n')


''' 
Average StdDev Median Highest
676.67	394.60	650	   1365 


662/-14.67/-379.93/-57.39	
699/22.33/-372.27/-53.26	
696/19.33/-375.27/-53.92	
638/-38.67/-355.93/-55.79	
1365/688.33/293.73/21.52	******
0/-676.67/282.07/0	

'''