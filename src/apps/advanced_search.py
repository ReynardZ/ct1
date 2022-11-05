def format_sql(form):
    if form.concert.data != '':
        a = "c.concert_name like '%{}%' ".format(form.concert.data)
    else:
        a = 'TRUE'
    if form.artist.data != '':
        b = "c.artist_name like '%{}%' ".format(form.artist.data)
    else:
        b = 'TRUE'
    if form.venue.data != '':
        c = "v.venue_name like '%{}%' ".format(form.venue.data)
    else:
        c = 'TRUE'
    if form.max.data != '' and form.min.data != '':
        d = "t.ticket_price between {} and {} ".format(form.min.data, form.max.data)
    elif form.max.data != '':
        d = "t.ticket_price < {}".format(form.max.data)
    elif form.min.data != '':
        d = "t.ticket_price > {}".format(form.min.data)
    else:
        d = 'TRUE'
    if form.month.data != "" and form.day.data != "" and form.year.data != "":
        e = "d.date = '{}/{}/{}' ".format(form.month.data, form.day.data, form.year.data)
    else:
        e = 'TRUE'
    statement = "select distinct c.concert_name, c.artist_name, v.venue_name,t.ticket_price " \
                "from aggregated_fact_table a " \
                "inner join concert_dimension c on c.concert_id=a.concert_id " \
                "inner join ticket_type_dimension t on t.ticket_number=a.ticket_number " \
                "inner join host_dimension v on v.venue_id=a.venue_id " \
                "inner join date_dimension d on d.date=a.date " \
                "where {} " \
                "and {} " \
                "and {} " \
                "and  {} " \
                "and {}; ".format(a,b,c,d,e)
    return statement