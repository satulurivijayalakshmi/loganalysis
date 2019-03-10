#! /usr/bin/env python

import psycopg2

DATABASE = "news"


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    data = psycopg2.connect('dbname=' + DATABASE)
    conn = data.cursor()
    conn.execute(query)
    chain = conn.fetchall()
    data.close()
    return chain


def outstanding_articles():
    """print the top 3 articles"""

    # Build Query String
    query = ''' SELECT articles.title,
                   count(*)
             as views FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY views DESC
            limit 3; '''
    query1 = ''' select * from articles;'''

    if(query):
        al = run_query(query)

        print('\n PRINT THE TOP THREE ARTICLES:')
        count = 1
        for available in al:
            no = '(' + str(count) + ') "'
            svl = available[0]
            svm = '" -------> ' + str(available[1]) + " views"
            print(no + svl + svm)
            count += 1
    if(query1):
        al = run_query(query1)
    elif():
        print('statement is wrong')
    else:
        print("the query is wrong")


def top4_applauded_authors():
    """print all the top most authors in descending order"""

    # Build Query String
    query = (
                "select authors.name, count(*) as views from articles inner "
                "join authors on articles.author = authors.id inner join log "
                "on log.path like concat('%', articles.slug, '%') "
                "group by authors.name order by count(*) desc limit 4;")
    if(query):
        al = run_query(query)
        print('\n PRINT THE TOP FOUR AUTHORS:')
        count = 1
        for available in al:
            print('(' + str(count) + ') ' + available[0] + ' ******* ' + str(
                        available[1]) + " views")
            count += 1
    else:
        print("The query is wrong")


def get_days_withmorethan1_errors():
    """print the days with more than 1% errors"""

    # Build Query String
    query = '''
            select * from (select date(time),round(100.0*sum(case log.status
            when '200 OK'  then 0 else 1 end)/count(log.status),3) as error
            from log group
            by date(time) order by error desc) as subq where error > 1;
                '''
    try:
        al = run_query(query)

        print('\nPRINT THE DAYS WITH MORE THAN 1% ERRORS:')
        for available in al:

            print('\n  On ' + str(available[0]) + '   ######>>   ' + '%.1f' %
                  available[1]+'% errors\n')
    except Exception as e:
        print("e")

print('Calculating Results...\n')
outstanding_articles()
top4_applauded_authors()
get_days_withmorethan1_errors()
