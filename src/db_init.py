def init_database(file, models):
    db_file = open(file, 'r')
    succeed = 0
    failed = 0
    for line in db_file:
        line = line.strip()
        if len(line) != 0 and line.endswith(";"):
            try:
                models.execute_sql(line)
            except:
                failed += 1
            finally:
                succeed += 1
    print(
        "Initialization Finished. {} sql statements executed successfully and {} sql statements failed to executed".format(
            succeed, failed))
