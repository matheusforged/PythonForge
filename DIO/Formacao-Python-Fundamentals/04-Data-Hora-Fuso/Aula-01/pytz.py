import sys
from datetime import datetime

pytz_path = "D:/Support/Library/pytz"

sys.path.insert(0, pytz_path)

import pytz # type: ignore

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)


