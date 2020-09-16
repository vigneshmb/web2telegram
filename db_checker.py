import tlgram_sender as df
import pymysql
import urllib.parse

def db_chk(agg_urls):
    titles_agg=[]
    for tm in agg_urls:
        if agg_urls.index(tm)%2==0:
            titles_agg.append(tm)
    
    hst='server name or ip address'
    uid='user id'
    pswd='password'
    db_id='database name'
    
    cnctn = pymysql.connect(host=hst,user=uid,password=pswd,db=db_id,charset='utf8mb4')
    cursor = cnctn.cursor()	
    cursor.execute("query to select titles of articles sent already from your table") 
    rows = cursor.fetchall()
    titles_db=[]
    for row in rows:
        titles_db.append(row[0])
    
    titles_new=[]
    for i in titles_agg:
        if i not in titles_db:
            titles_new.append(i)

    for i in titles_new:
        for j in agg_urls:
            if i==j:
                title=str(j)
                url=agg_urls[agg_urls.index(j)+1]
                msg=title+"  "+url
                msg=urllib.parse.quote(msg)
                sent_flag=df.send_msg(msg)
                if sent_flag: #if msg was sent or not sent, flag will be 1 or 0 respectively
                    ins_qry=f"query to insert titles of articles sent already into your table"
                    cursor.execute(ins_qry)
                if sent_flag==False:
                    ins_qry=f"query to insert titles of articles sent already into your table"
                    cursor.execute(ins_qry)
    cnctn.commit()
    cnctn.close()


if __name__ == "__main__":
    lnk=[["Updated: Nokia 6.1, Nokia 6.1 Plus, Nokia 7 Plus & Nokia 7.1 receiving August Security update now",
    "https://nokiapoweruser.com/nokia-7-1-nokia-6-1-plus-nokia-7-plus-receiving-august-security-update-now/"],
    ["test1","test1"]]
    db_chk(lnk)