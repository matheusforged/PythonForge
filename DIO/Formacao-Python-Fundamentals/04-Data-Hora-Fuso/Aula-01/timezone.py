from datetime import datetime, timedelta, timezone

data_olso = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))

print(data_olso)
print(data_sao_paulo)