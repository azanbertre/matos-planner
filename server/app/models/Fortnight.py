from datetime import datetime


class Fortnight:

    months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    @classmethod
    def get_slug(cls, fortnight_date):

        if isinstance(fortnight_date, datetime):
            fortnight_date = fortnight_date.isoformat()

        fortnight_date = str(fortnight_date)[:10]

        year = int(fortnight_date.split('-')[0])
        month = int(fortnight_date.split('-')[1])
        day = int(fortnight_date.split('-')[2])

        return f'{cls.months[month - 1]} {"1" if day < 15 else "2"}/2 - {year}'
