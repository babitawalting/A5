

"""

Aan deze code hoeft je niet te doen, en niets te begrijpen!
Deze kleine "library" zorgt ervoor dat je op een makkelijke manier,
de resultaten vanuit pandas netjes kunt printen.

"""

















import math
from datetime import datetime

def prettify(dataframe, type="", columns=None):

    df = dataframe.copy()
    index = True
    if type == "zwartboek" or type == "eregalerij":
        columns = ["datum", "team1", "team2", "uitslag", "scheidsrechter"]
        if type == "zwartboek":
            columns.append("overtredingen")
            
        df["datum"] = dataframe["datum"].dt.strftime("%d-%m-%Y")
        index = False


    return df.to_string(columns=columns, index=index, na_rep="0", float_format=round_str)

def round_str(num):
    if(math.isnan(num)):
        return "0"
    else:
        return str(round(num))
