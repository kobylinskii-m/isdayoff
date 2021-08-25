# isdayoff

Production Calendar API

Description:
* Checking the date for belonging to a non-working day, according to official decrees and orders.


Official API website - https://isdayoff.ru

# install 

```bash
pip install isdayoff
```

## Checking tomorrow

```python
import asyncio

from isdayoff import DateType, ProdCalendar

calendar = ProdCalendar(locale='us')


async def main():
    if await calendar.tomorrow() == DateType.WORKING:
        print('Tomorrow is a working day')
    else:
        print('Tomorrow is a day off')
    
    
loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
```

## Checking today

### params 

+ locale: str - country code (by, kz, ru, ua)

+ pre: bool - mark shortened working days

+ covid: bool - mark working days (due to the COVID-19 pandemic)

+ sd: bool - consider that the week is six days long


```python
await calendar.today(locale='ru', pre=True, covid=True, sd=True)
```


## Weekend on this date

### params

+ date: datetime.date - date

+ locale: str - country code (by, kz, ru, ua)

+ pre: bool - mark shortened working days

+ covid: bool - mark working days (due to the COVID-19 pandemic)

+ sd: bool - consider that the week is six days long

```python
import asyncio
from datetime import date

from isdayoff import DateType, ProdCalendar

calendar = ProdCalendar(locale='us')


async def main():
    if await calendar.date(date(2021, 8, 25)) == DateType.WORKING:
        print('Is a working day')
    else:
        print('Is a day off')
...
```


## Getting information about days for a month

+ date: datetime.date - date

+ locale: str - country code (by, kz, ru, ua)

+ pre: bool - mark shortened working days

+ covid: bool - mark working days (due to the COVID-19 pandemic)

+ sd: bool - consider that the week is six days long

```python
await calendar.month(date(2021, 8, 1))
```

## Getting information about days for the year

+ date: datetime.date - date

+ locale: str - country code (by, kz, ru, ua)

+ pre: bool - mark shortened working days

+ covid: bool - mark working days (due to the COVID-19 pandemic)

+ sd: bool - consider that the week is six days long

```python
await calendar.year(date(2021, 1, 1))
```

## Getting information about days for a derived period

+ start_date: datetime.date - date

+ end_date: datetime.date - date

+ locale: str - country code (by, kz, ru, ua)

+ pre: bool - mark shortened working days

+ covid: bool - mark working days (due to the COVID-19 pandemic)

+ sd: bool - consider that the week is six days long

```python
await calendar.range_date(date(2021, 1, 1), date(2021, 5, 1))
```

## Is it a leap year

+ date: datetime.date - date

```python
await calendar.is_leap(date(2021, 1, 1))
```


# Example

```python
from isdayoff import ProdCalendar, DateType
from datetime import date
import asyncio


calendar = ProdCalendar(locale='us')


async def main():
    res = await calendar.month(date(2021, 8, 1), locale='ru')
    count = len([DateType.NOT_WORKING for day in res if res[day] == DateType.NOT_WORKING])
    print('Days off in a month', count)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()

```
