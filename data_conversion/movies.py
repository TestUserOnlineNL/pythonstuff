import re


def checkMoviesData(lineText):
# get movie title and year and return them in a tuple
    movieData = re.search(r"^(.+)\s\(([0-9]+)\)$", lineText)

    if movieData is None:
        if(len(lineText.strip())>0):
            invalidData = ("---invalid---",lineText.strip(),'')
        return(invalidData)
    else:
        return(movieData.group(1,2))


# filter movie data and save it in a text file
def exportToDelimited():
    lnv = 0; lni = 0; count = 0;
    with open(r"./movies_data.txt", 'r',encoding='UTF8') as fp: 
        with open(r"./movies_data_cleaned.txt", 'w',encoding='UTF8') as f_data_valid:
            with open(r"./movies_data_invalid.txt", 'w',encoding='UTF8') as f_data_invalid:
                for line in fp:
                    result = checkMoviesData(line)
                    if result != None and result[0] != ("---invalid---"):
                        lnv = lnv + 1
                        count = count + 1
                        newline = str(lnv) + '|' + result[0] + '|' + result[1] + '\n'
                        f_data_valid.writelines(newline)
                    elif result != None and result[0] == ("---invalid---"):
                        count = count + 1
                        lni = lni + 1
                        f_data_invalid.writelines(result[0] + " " + result[1] + " ---line: " + str(count) +'\n')
    return(lnv,lni,count)


if __name__ == '__main__':
    
    a,b,c = exportToDelimited()
    print(f"Total valid #{a}")
    print(f"Total invalid #{b}")
    print(f"Total lines #{c}")