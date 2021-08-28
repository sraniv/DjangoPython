def getDBConnCursor():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tinitiate', db='loans')
    cursor = conn.cursor()
    return cursor,conn


@api_view(['GET', 'POST'])
def getempbyid(request):

    cursor,conn = getDBConnCursor()
    
    if request.method == 'GET' and 'N1' in request.GET:
        # request.GET is the parameter dictionary
        empid = request.GET['empid']
    else:
        empid = -1
        
    try:
        l_data_cnt = 0m
        
        l_sql = "select 
                   from   emp
                   where  empid=%i;"%empid

        cursor.execute(l_sql)
        for l_ename, l_sal, l_join_date in cursor.fetchall():
            l_data_cnt = 1 
            data = {'ename':l_ename
                    ,'sal':l_sal
                    ,'join_date':l_join_date}
                  
        cursor.close()
        conn.close()
    except:
        data = {"Error": {"status": 400,
                          "message": "No Data Found"}}

        return Response(data, status=status.HTTP_400_BAD_REQUEST)    
    else:    
        if l_data_cnt = 1:
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {"Error": {"status": 400,
                              "message": "No Data Found"}}

            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
# Read File Contents
# File Upload
# File Download
