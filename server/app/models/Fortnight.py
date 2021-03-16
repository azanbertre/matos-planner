from datetime import datetime


class Fortnight:

    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    @classmethod
    def get(cls):
        now = datetime.utcnow()

        last_year = now.replace(year=now.year - 1)

        date_1 = last_year.replace(month=12, day=1, hour=0, minute=0, second=0, microsecond=0)
        date_2 = date_1.replace(day=15)

        months = cls.months

        fortnights = [
            {
                'name': cls.get_slug(date_1),
                'value': date_1
            },
            {
                'name': cls.get_slug(date_2),
                'value': date_2
            }
        ]

        date_1 = date_1.replace(month=1, year=date_1.year + 1)
        date_2 = date_2.replace(month=1, year=date_1.year)

        for m in months:

            fortnights.append({
                'name': cls.get_slug(date_1),
                'value': date_1
            })

            fortnights.append({
                'name': cls.get_slug(date_2),
                'value': date_2
            })

            if date_1.month < 12:
                date_1 = date_1.replace(month=date_1.month + 1)
                date_2 = date_2.replace(month=date_1.month)

        return fortnights

    @classmethod
    def get_slug(cls, fortnight_date):

        if isinstance(fortnight_date, datetime):
            fortnight_date = fortnight_date.isoformat()

        fortnight_date = str(fortnight_date)[:10]

        year = int(fortnight_date.split('-')[0])
        month = int(fortnight_date.split('-')[1])
        day = int(fortnight_date.split('-')[2])

        return f'{cls.months[month - 1]} {"1" if day < 15 else "2"}/2 - {year}'
