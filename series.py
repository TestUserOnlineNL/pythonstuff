import re

def checkSeriesData(lineText) -> None:
    # get serie title, season number and episode number from text input
    seriesData = re.search("^(.+)\s(season||deel)\s([0-9]+)\s\-\s([0-9]+)\s.+$", lineText)

    if seriesData is None:
        if(len(lineText.strip())>0):
            invalidData = ("---invalid---",lineText.strip(),'')
            return(invalidData)
        pass
    else:
        return(seriesData.group(1,3,4))
    
def exportToDelimited()->None:
    lnv = 0;lni = 0;count = 0
    with open(r"./series_data.txt", 'r') as fp:
        with open(r"./serie_data_cleaned.txt", 'w') as f_data_valid:
            with open(r"./serie_data_invalid.txt", 'w') as f_data_invalid:
                for line in fp:
                    result = checkSeriesData(line)
                    if result != None and result[0] != ("---invalid---"):
                        count = count + 1
                        lnv = lnv + 1
                        f_data_valid.writelines(str(lnv) + "|" + result[0] + "|" + result[1] + "|" + result[2] + '\n')
                    elif result != None and result[0] == ("---invalid---"):
                        count = count + 1
                        lni = lni + 1
                        f_data_invalid.writelines(result[0] + " " + result[1] + " ---line: " + str(count) + '\n')
        
    return lnv,lni,count

if __name__ == '__main__':
    a,b,c = exportToDelimited()

    print(f"Total valid #{a}")
    print(f"Total invalid #{b}")
    print(f"Total lines #{c}")