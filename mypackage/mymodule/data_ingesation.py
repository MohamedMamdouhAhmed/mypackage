def create_db_engine(db_path):
    """
    Creates a SQLAlchemy engine connected to a database specified by path.

    Args:
        db_path (str): Path to the database file. The format depends on the database engine.
            For example, for SQLite, it is `sqlite:///path/to/file.db`.

    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine object connected to the database.
    """
    engine = create_engine(db_path)
    return engine


def query_data(engine, sql_query):
    """
    Creates a DataFrame using tables in a Database using a SQL code

    Args:
        engine(engine): A SQLAlchemy engine object connected to the database.
        sql_query(str): an sql code that retrieve a data from a db.
    
    Returns:
        MD_agric_df(DataFrame): A data frame has all the data specified in the SQL code.

    """
    with engine.connect() as connection:
    
        MD_agric_df = pd.read_sql_query(text(sql_query), connection)

