import mysql.connector
import streamlit as st
import pandas as pd
import datetime
st.set_page_config(page_title="Library Management System",page_icon="https://cdn-icons-png.flaticon.com/512/4318/4318379.png")
st.title("LIBRARY MANAGEMENT SYSTEM")
choice=st.sidebar.selectbox("Main Menu",("HOME","STUDENT","ADMIN","REGISTRATION"))
if(choice=="HOME"):
    st.image("https://5.imimg.com/data5/SELLER/Default/2021/12/XQ/XT/NB/52242850/1-5--500x500.png")
    st.sidebar.image("https://static.vecteezy.com/system/resources/previews/000/449/897/original/home-vector-icon.jpg")
    st.write("This is an application used for Library Management Report")
elif(choice=="STUDENT"):
    st.sidebar.image("https://toppng.com/uploads/preview/icon-student-icon-for-new-student-11553429035frago151ec.png")
    if "islogin" not in st.session_state:
        st.session_state['islogin']=False
    sid=st.text_input("Enter Student ID")
    pwd=st.text_input("Enter Student Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
        c=mydb.cursor()
        c.execute("select * from student")
        data=c.fetchall()
        for k in data:
            if(k[0]==sid and k[1]==pwd):
                st.session_state['islogin']=True
                break
        if not st.session_state['islogin']:
            st.subheader("Incorrect ID or Password")
    if st.session_state['islogin']:
        st.subheader("Login Successfull")
        choice2=st.selectbox("Features",("None","View All Books","Issue Books"))
        if(choice2=="View All Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
            c=mydb.cursor()
            c.execute("select * from books")
            mydata=c.fetchall()
            mycolumns=c.column_names
            df=pd.DataFrame(data=mydata,columns=mycolumns)
            st.dataframe(df)
        elif(choice2=="Issue Books"):
            bid=st.text_input("Enter Book ID")
            stid=st.text_input("Enter your Student ID")
            btn2=st.button("Issue Book")
            if btn2:
                iid=str(datetime.datetime.now())
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
                c=mydb.cursor()
                c.execute("insert into issue values(%s,%s,%s)",(iid,bid,stid))
                mydb.commit()
                st.subheader("Book Issued Successfully")
elif(choice=="ADMIN"):
    st.sidebar.image("https://th.bing.com/th/id/OIP.iJ8GDoxdjs8WQWFfSd4cLwHaHa?rs=1&pid=ImgDetMain")
    if "islogin2" not in st.session_state:
        st.session_state['islogin2']=False
    sid=st.text_input("Enter Librarian ID")
    pwd=st.text_input("Enter Librarian Password")
    btn=st.button("Login")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
        c=mydb.cursor()
        c.execute("select * from admin")
        data=c.fetchall()
        for k in data:
            if(k[0]==sid and k[1]==pwd):
                st.session_state['islogin2']=True
                break
        if not st.session_state['islogin2']:
            st.subheader("Incorrect ID or Password")
    if st.session_state['islogin2']:
        st.subheader("Login Successfull")
        choice2=st.selectbox("Features",("None","View Issue Books","Add Books","Delete Book"))
        if(choice2=="View Issue Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
            c=mydb.cursor()
            c.execute("select * from issue")
            mydata=c.fetchall()
            mycolumns=c.column_names
            df=pd.DataFrame(data=mydata,columns=mycolumns)
            st.dataframe(df)
        elif(choice2=="Add Books"):
            bid=st.text_input("Enter Book ID")
            bname=st.text_input("Enter Book Name")
            aname=st.text_input("Enter Author Name")
            btn2=st.button("Add Book")
            if btn2:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
                c=mydb.cursor()
                c.execute("insert into books values(%s,%s,%s)",(bid,bname,aname))
                mydb.commit()
                st.subheader("Book Added Successfully")
        elif(choice2=="Delete Book"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
            c=mydb.cursor()
            c.execute("select * from books")
            mydata=c.fetchall()
            mycolumns=c.column_names
            df=pd.DataFrame(data=mydata,columns=mycolumns)            
            bid=st.selectbox("Choose Book ID to delete",df['book_id'])          
            btn2=st.button("Delete Book")
            if btn2:                
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
                c=mydb.cursor()
                c.execute("delete from books where book_id=%s",(bid,))
                mydb.commit()
                st.subheader("Book Deleted Successfully")
elif(choice=="REGISTRATION"):
    st.sidebar.image("https://icon-library.com/images/registration-icon-png/registration-icon-png-6.jpg")
    stid=st.text_input("Enter User ID")
    pwd=st.text_input("Choose a Password")
    btn=st.button("Register")
    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="lms")
        c=mydb.cursor()
        c.execute("insert into  student values(%s,%s)",(stid,pwd))
        mydb.commit()
        st.subheader("Registration Successfully")











                
        
    
    
                

