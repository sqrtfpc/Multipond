def sumHydrographs(resultsTable, hydrographs, direction):
    
    if direction == 'East':
        inflowDirection = 'East Flow'
    elif direction == 'West':
        inflowDirection = 'West Flow'
    else:
        print('Invalid direction')
        return()
        
    for basin in hydrographs:
        for index, rows in resultsTable.iterrows():
            rows[inflowDirection] = rows[inflowDirection] + basin.loc[index, 'Total Flow (CFS)']
            
    return resultsTable
            
            
#This function takes a previously computed tailwater and headwater,
#then returns a value for the flowrate

def hy8Interpolation(hy8, headwater, tailwater):
    subHy8 = hy8[hy8.Tailwater == tailwater]
    for index, row in subHy8.iterrows():
        headwaterLesserComparison = row['Headwater'] - headwater
    
        if headwaterLesserComparison <= 0:
            lowerResult  = index
        
        if headwaterLesserComparison > 0:
            break
        
        greaterResult = lowerResult + 1
        
        return(lowerResult, greaterResult)