import xlwt
import pandas as pd 

def func( htmlfilepath , excelfilepath  ):
    with open(htmlfilepath,'r') as G:                                           #here our html file is read
        table = pd.read_html(G,index_col=False)[1]                              #we read our secound file

        table = table[['Variables','Tasks (Write)','Tasks (Read)','Usage','Detailed Type','Nb Read','Nb Write']]
        table.reset_index(drop=True,inplace = True)                             

    for ele in table['Variables']:                                              #we get the desired variable name
        s = str(ele)
        if '.' in s:
            table.replace(ele, s[s.index('.')+1:], inplace = True)

    table = table.loc[table['Usage'] == 'shared']                   #we store only those rows where Usage is shared
    del table['Usage']                                                                   #removes Usage column 
    table.rename(columns={"Tasks (Write)": "W.T", "Tasks (Read)": "R.T"},inplace = True)        #rename the columns
    
    print("Excel file is created!!!!!")
    table.to_excel(excelfilepath,index=False)                       #creates the excel file with given requirements

if __name__ == '__main__':
    ##########Set Default value for input file and output file#########
    
    defaultInput = "file.html"
    defaultDestination = "ex.xlsx"
    
    ###################################################################
    
    htmlfile = input("What's the file name of .html format? 'Hit Enter to skip!' ")  or defaultInput
    excelfile = input("What's the file name of destination .xlsx format? 'Hit Enter to skip!' ") or defaultDestination
    func(htmlfile,excelfile)