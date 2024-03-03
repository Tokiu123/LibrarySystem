import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog,messagebox
from  PIL import ImageTk,Image

class LibrarySystem:
    #初始化图书馆管理系统类，初始化根窗口，并设置窗口标题和窗口大小，调用creation函数创建界面
    def __init__(self,root):#利用构造方法初始化
        self.root = root
        self.root.title('图书馆管理系统') # 设置主窗口标题
        self.root.geometry("600x400")
        self.creation()

    #创建图书馆管理系统的界面，包括背景图片标签、用户选项标签、用户选项的下拉框、确定按钮
    def creation(self):#创建相关基本信息
            self.operator_dict={}
            self.student_dict={}

            self.read_operator()
            self.read_student()

            self.bg_image=Image.open("广州商学院图书馆.jpg")
            self.bg_photo=ImageTk.PhotoImage(self.bg_image)

            self.bg_lable=tk.Label(self.root,image=self.bg_photo)
            self.bg_lable.place(x=0,y=0,relwidth=1,relheight=1)


            self.chacterist_lable = tk.Label(self.root, text="用户选项")
            self.chacterist_lable.place(x=290, y=110)

            self.chacterist_Combobox = ttk.Combobox(self.root,values=("图书管理员","学生用户"),width=20)#使用Entry输入组件，用于显示和输入'用户名'信息
            self.chacterist_Combobox.place(x=240,y=130)

            self.login_button = tk.Button(self.root, text="确定",
                                     command=self.change)  # 使用tkinter的button点击组件，用于用户输入完用户名和密码然后登录,且设置了点击登录会有相应的反应
            self.login_button.place(x=300, y=155)

    #读取包含图书管理员账号和密码的txt文件，将账号和密码写入operator_dict字典中
    def read_operator(self):
        # 将带有账号密码的txt文件写入装有账号密码的字典中
        with open('图书管理员账号密码文件.txt', 'r', encoding='utf-8') as f:
            content = f.readlines()
            print(content)
            for lines in content:
                line = lines.split(' ')
                key = line[0]
                value = line[1].replace('\n', '')
                self.operator_dict[key] = value

    #读取包含学生用户账号和密码的txt文件，将账号和密码写入student_dict字典中
    def read_student(self):
        # 将带有账号密码的txt文件写入装有账号密码的字典中
        with open('学生用户账号密码文件.txt', 'r', encoding='utf-8') as f:
            content = f.readlines()
            print(content)
            for lines in content:
                line = lines.split(' ')
                key = line[0]
                value = line[1].replace('\n', '')
                self.student_dict[key] = value



    def writer_operator(self):
        # 将带有账号密码的txt文件写入装有账号密码的字典中
        with open('图书管理员账号密码文件.txt', 'w+', encoding='utf-8') as f:
            for key in self.operator_dict:
                f.write(key)
                f.write(' ')
                f.write(self.operator_dict[key])
                f.write('\n')


    def writer_student(self):
        # 将带有账号密码的txt文件写入装有账号密码的字典中
        with open('学生用户账号密码文件.txt', 'w+', encoding='utf-8') as f:
            for key in self.student_dict:
                f.write(key)
                f.write(' ')
                f.write(self.student_dict[key])
                f.write('\n')






    #隐藏登录界面的一些组件，显示登录成功标签
    def disapper(self):#将组件销毁
        self.username_lable.place_forget()  # 让控件“不再显示”但控件还存在可以再次pack出来，既实现跳转操作
        self.username_entry.place_forget()
        self.password_lable.place_forget()
        self.password_entry.place_forget()
        self.login_button.place_forget()
        self.option_lable.place_forget()
        self.login_Combobox.place_forget()
        self.signup_lable = tk.Label(self.root, text="您已成功登录！")
        self.signup_lable.place(x=210, y=140)
        self.signup_lable.config(font=("宋体", 24))

    def register_operator(self):
        usernaem=self.username_entry.get()
        password=self.password_entry.get()
        if len(usernaem)==0:
            messagebox.showerror("错误","请输入有效信息")
        else:
            if usernaem not in self.operator_dict:
                self.operator_dict[usernaem]=password
                messagebox.showinfo("成功","已经成功创建账号")
                print(self.operator_dict)
                self.writer_operator()

            else:
                messagebox.showinfo("错误", "该账号已经存在")


    def register_student(self):
        usernaem=self.username_entry.get()
        password=self.password_entry.get()
        if len(usernaem)==0:
            messagebox.showerror("错误","请输入有效信息")
        else:
            if usernaem not in self.student_dict:
                self.student_dict[usernaem]=password
                messagebox.showinfo("成功","已经成功创建账号")
                print(self.student_dict)
                self.writer_student()

            else:
                messagebox.showinfo("错误", "该账号已经存在")



    def delete_operator(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirmed = messagebox.askokcancel("确认删除", "确定注销该用户吗？")
        if confirmed:
            if username in self.operator_dict:
                if password==self.operator_dict[username]:
                    del self.operator_dict[username]
                    self.writer_operator()
                    self.operator_dict.clear()
                    self.read_operator()
                    messagebox.showinfo("成功","已经成功注销账号")



    def delete_student(self):#注销用户
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirmed = messagebox.askokcancel("确认删除", "确定注销该用户吗？")
        if confirmed:
            if username in self.student_dict:
                if password == self.student_dict[username]:
                    del self.student_dict[username]
                    self.writer_student()
                    self.student_dict.clear()
                    self.read_student()
                    messagebox.showinfo("成功", "已经成功注销账号")



    #隐藏登录界面的一些组件，创建图书管理员登录界面，包括功能模块标签、功能选项的下拉框、图书列表框、确定按钮
    def user1_page(self):
        self.disapper()

        self.books=[]
        self.aaa=tk.Tk()
        self.aaa.title("图书管理员")
        self.aaa.geometry("400x400")#300x400
        self.student_lable=tk.Label(self.aaa,text='功能模块')
        self.student_lable.place(x=160,y=80)
        self.student_lable.config(font=("宋体", 16))
        self.option_Combobox = ttk.Combobox(self.aaa, values=("查找图书","添加图书","删除图书","查重","导出文件","导入文件"),
                                                width=43)  # 使用Entry输入组件，用于显示和输入'用户名'信息
        self.option_Combobox.place(x=40, y=110)
        self.book_listbox = tk.Listbox(self.aaa, width=46)
        self.book_listbox.place(x=40,y=130)

        self.option_button=tk.Button(self.aaa,text="确定",command=self.option1)
        self.option_button.place(x=190,y=320)

    #隐藏登录界面的一些组件，创建学生用户登录界面，包括功能模块标签、功能选项的下拉框、图书列表框、确定按钮。
    def user2_page(self):
        self.disapper()
        self.books = []
        self.aaa = tk.Tk()
        self.aaa.title("学生用户")
        self.aaa.geometry("400x400")  # 300x400
        self.student_lable=tk.Label(self.aaa,text='功能模块')
        self.student_lable.place(x=160,y=80)
        self.student_lable.config(font=("宋体", 16))
        self.option_Combobox = ttk.Combobox(self.aaa,
                                            values=("查找图书", "借用图书", "归还图书"),
                                            width=43)  # 使用Entry输入组件，用于显示和输入'用户名'信息
        self.option_Combobox.place(x=40, y=110)
        self.book_listbox = tk.Listbox(self.aaa, width=46)
        self.book_listbox.place(x=40, y=130)
        with open("书籍文件.txt", 'r+', encoding='utf-8') as fp:
            content = fp.readlines()
        for lines in content:
            line = lines.split(' ')
            self.books.append({'标题': line[0], '出版时间': line[1], '作者': line[2]})
        self.load_books()

        self.option_button = tk.Button(self.aaa, text="确定", command=self.option2)
        self.option_button.place(x=190, y=320)

    #隐藏用户选项标签、用户选项下拉框、确定按钮，显示用户名标签、用户名输入框、密码标签、密码输入框，根据用户类型创建登录按钮。
    def sign_up(self, number):
        self.chacterist_lable.place_forget()
        self.chacterist_Combobox.place_forget()
        self.login_button.place_forget()

        self.username_lable = tk.Label(self.root, text="用户名")
        self.username_lable.place(x=200, y=110)

        self.username_entry = tk.Entry(self.root)  # 使用Entry输入组件，用于显示和输入'用户名'信息
        self.username_entry.place(x=240, y=110)

        self.password_lable = tk.Label(self.root, text="密码")
        self.password_lable.place(x=210, y=140)

        self.password_entry = tk.Entry(self.root, show='*')  # 使用Entry输入组件，用于显示和输入"密码"信息，且输出的方式为‘*’
        self.password_entry.place(x=240, y=140)
        if number == '图书管理员':
            self.option_lable = tk.Label(self.root, text="选项")
            self.option_lable.place(x=210, y=170)
            self.login_Combobox=ttk.Combobox(self.root,values=("登录", "注册", "注销"),width=17)
            self.login_Combobox.place(x=241,y=170)
            self.login_button = tk.Button(self.root, text="确定",
                                          command=self.user_option1)  # 使用tkinter的button点击组件，用于用户输入完用户名和密码然后登录,且设置了点击登录会有相应的反应
            self.login_button.place(x=295, y=205)

        elif number == '学生用户':
            self.option_lable = tk.Label(self.root, text="选项")
            self.option_lable.place(x=210, y=170)
            self.login_Combobox = ttk.Combobox(self.root, values=("登录", "注册", "注销"), width=17)
            self.login_Combobox.place(x=241, y=170)
            self.login_button = tk.Button(self.root, text="确定",
                                          command=self.user_option2)  # 使用tkinter的button点击组件，用于用户输入完用户名和密码然后登录,且设置了点击登录会有相应的反应
            self.login_button.place(x=295, y=205)

    def user_option1(self):
        option=str(self.login_Combobox.get())
        if option=="登录":
            self.login1()
        elif option=="注册":
            self.register_operator()
        elif option=="注销":
            self.delete_operator()
        else:
            messagebox.showinfo("提示","不存在任何有效信息")

    def user_option2(self):
        option = str(self.login_Combobox.get())
        if option == "登录":
            self.login2()
        elif option == "注册":
            self.register_student()
        elif option == "注销":
            self.delete_student()
        else:
            messagebox.showinfo("提示", "不存在任何有效信息")




    #获取图书管理员登录界面输入的用户名和密码，判断是否存在于operator_dict字典中，如果存在则登录成功，调用user1_page函数进入图书管理员页面，否则弹出用户名或密码错误的提示框
    def login1(self):  # 成员方法
        username = self.username_entry.get()
        passwork = self.password_entry.get()
        if username in self.operator_dict:
            if passwork==self.operator_dict[username]:
                self.user1_page()
            else:
                messagebox.showerror("错误", "用户名或密码错误")
        else:
            messagebox.showerror("错误","用户名或密码错误")


    #获取学生用户登录界面输入的用户名和密码，判断是否存在于student_dict字典中，如果存在则登录成功，调用user2_page函数进入学生用户页面，否则弹出用户名或密码错误的提示框
    def login2(self):  # 成员方法
        username = self.username_entry.get()
        passwork = self.password_entry.get()
        if username in self.student_dict:
            if passwork==self.operator_dict[username]:
                self.user2_page()
            else:
                messagebox.showerror("错误", "用户名或密码错误")
        else:
            messagebox.showerror("错误","用户名或密码错误")


    #获取用户选择的用户类型，根据用户类型设置窗口标题，调用sign_up函数创建登录界面
    def change(self):
        number = str(self.chacterist_Combobox.get())
        print(number)
        if number=="图书管理员":
            self.root.title("图书管理员")
            self.sign_up(number)
        elif number=="学生用户":
            self.root.title("学生用户")
            self.sign_up(number)
        else:
            messagebox.showerror("错误","请重新输入！")





    #获取图书管理员登录界面选择的功能模块，根据选择的功能模块执行相应的操作
    def option1(self):
        option = str(self.option_Combobox.get())
        print(option)
        if option == "查找图书":
            self.find_book()
        elif option == "添加图书":
            self.add_book()
        elif option == "删除图书":
            self.delete_book()
        elif option == "查重":
            self.check_book()
        elif option == "导入文件":
            self.input_file()
        elif option == "导出文件":
            self.out_file()

    #获取学生用户登录界面选择的功能模块，根据选择的功能模块执行相应的操作
    def option2(self):
        option = str(self.option_Combobox.get())
        print(option)
        if option == "查找图书":
            self.find_book()
        elif option == "借用图书":
            self.brrow_book()
        elif option == "归还图书":
            self.back_book()






    def load_books(self):  # 自定义一个下载书籍函数
        # 使用Listbox列表框的delete()函数删除[0,tk.END]的列表项，其中0为第一项，tk.END为最后一项；注意：这里对每一次去除是为了将新插入的字符连同上一次所携带的字符插入到列表框中！而不是清除了原有的数据！
        self.book_listbox.delete(0, tk.END)
        for book in self.books:  # 对books列表进行遍历
            # 在列表框中利用insert()函数在列表框的尾部以字符串格式化的方式加入书籍（包括标题，出版时间，作者）
            self.book_listbox.insert(tk.END, f"{book['标题']} {book['出版时间']} {book['作者']}")

    def find_book(self):#自定义查重书籍模块函数
        title=tk.simpledialog.askstring("查找图书","请输入图书标题")#simpledialog.askstring()函数为tkinter用于创建一个简单的对话框来让用户输入字符串（书名）。它通常用于获取用户输入的文本信息
        if title:#如果输入title为一个字符串
            found_books=[]#建立一个found_books列表
            for book in self.books:#遍历图书列表，每一本图书对应3个值
                if book['标题']==title:#如果存在标题与输入title相同的书
                    found_books.append(book)#found_books列表写入该书籍
            if found_books:#如果found_books列表存在
                self.book_listbox.delete(0,tk.END)#将在Librarysystem类中已经定义好的book_listbox列表框进行初始化操作，则先将该按钮下对应的列表框内的内容全部删除
                for book in found_books:#对found_books进行遍历操作
                    self.book_listbox.insert(tk.END,f"{book['标题']} {book['出版时间']} {book['作者']}")#对已经初始完的列表框重新插入符合该标题的书籍信息
            else:#found_list若不存在
                # messagebox为显示一个模态对话框，第一个元title=tk.simpledialog.askstring("查找图书","请输入图书标题")#simpledialog.askstring()函数为tkinter用于创建一个简单的对话框来让用户输入字符串（书名）。它通常用于获取用户输入的文本信息
                messagebox.showinfo("提示","未找到该图书")


    def add_book(self):#自定义添加书籍模块函数
        title = tk.simpledialog.askstring("添加图书", "请输入图书标题")#输入图书标题
        date = tk.simpledialog.askstring("添加图书", "请输入图书出版时间")#输入图书出版时间
        author = tk.simpledialog.askstring("添加图书", "请输入图书作者")#输入图书作者
        if title and date and author:#如果三个元素都存在
            self.books.append({"标题": title, "出版时间":date,"作者": author})#将book以字典的形式（键值对）写入books列表中即为[{},{},{}]
            self.load_books()#调用已经定义好的self.load_books()函数对列表框进行清洗
            messagebox.showinfo("提示", "图书添加成功")#使用messagebox.showinfo(“”,””)函数提示操作成功
        else:
            messagebox.showinfo("提示", "请输入有效信息")#使用messagebox.showinfo(“”,””)函数进行报错


    def delete_book(self):#自定义删除书籍模块函数
        selected_books=self.book_listbox.curselection()#获得当前选中的条目，返回值是一个列表。列表中的内容是选中的列表项的索引值，既可对应图书列表内相关图书的索引值
        if selected_books:
            book_index=selected_books[0]#返回列表的第一个元素
            # print(book_index)#输出观察
            confirmed=messagebox.askokcancel("确认删除","确定删除该图书吗？")#使用messagebox.askokcancel(“元素1”,”元素2”)函数点击确定对目标列表项从列表框删去。
            if confirmed:
                del self.books[book_index]#删除图书列表内符合该索引值的图书信息
                self.load_books()#使用messagebox.showinfo(“”,””)函数进行报错
            else:
                pass
        else:
            messagebox.showinfo("错误","无获取任何信息")#messagebox.showinfo(“”,””)函数进行报错。

    def check_book(self):#自定义查重书籍模块函数
        duplicate = []#该模块首先先定义一个列表用于存放存在相同书籍的列表。
        for i, book in zip(range(0, len(self.books)), self.books):#利用嵌套循环，外循环使用i、book对zip关键字对图书列表中的索引值、书籍字典进行循环
            for j in range(i + 1, len(self.books)):#内循环使用j对i+1进行循环，使用if语句如果有图书列表中的书籍存在书名与图书列表的剩下的总数-第i本书的书名进行比较
                if book['标题'] == self.books[j]['标题']:
                    duplicate.append(book['标题'])#若找到则在存放相同书籍的列表中加入该书名
        if len(duplicate) != 0:
            for book2 in duplicate:
                index=duplicate.index(book2)
                for i in range(index+1,len(duplicate)):
                    try:
                        if duplicate[i]==book2:
                            del duplicate[i]
                    except:
                        duplicate=duplicate[:-1]
                        break
            if len(duplicate) != 0:
                for book2 in duplicate:
                    messagebox.showinfo("提示",
                                        book2 + "存在重复")  # 3.若存放存在相同书籍的列表长度不为0，则使用message.showinfo()函数对重复书籍进行输出。
            else:
                pass
        else:
            messagebox.showinfo("提示", "无重复图书")  # messagebox.showinfo(“”,””)函数进行报错。


    def input_file(self):#自定义导入文件模块函数
        try:
            with open("书籍文件.txt",'r',encoding='utf-8')as fp:#以”r+”打开装有图书信息的txt文件
                content=fp.readlines()#readlines()方法可以按照行（‘\n’）的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素。
                print(content)
            for lines in content:#使用for循环对该列表进行遍历
                line=lines.split(' ')#使用字符串的split(‘ ‘)的方法对空格进行分割
                self.books.append({'标题':line[0],'出版时间':line[1],'作者':line[2]})#获取标题、出版时间、作者三个字段，再以字典的字符串形式写入图书列表
            self.load_books()#使用定义好的load_books()函数，对列表框进行清洗
            messagebox.showinfo("提醒","导入文件成功")#使用messagebox.showinfo()函数提醒成功
        except:
            messagebox.showinfo("提醒","导入文件失败")#否则使用messagebox.showinfo()函数提醒失败


    def out_file(self):#自定义导出文件模块函数
        # print(self.books)
        with open("书籍文件.txt","w+",encoding='utf-8')as fp:#首先以”w+”打开装有图书信息的txt文件
            #使用for循环对图书列表进行循环，获取其中的图书字典，并使用write()函数将图书标题、图书出版时间、图书作者写入txt文件。
            for book in self.books:
                book_title=book['标题']
                book_date=book['出版时间']
                book_author1=book['作者']
                book_author2=book_author1.replace('\n','')
                fp.write(book_title)
                fp.write(' ')
                fp.write(book_date)
                fp.write(' ')
                fp.write(book_author2)
                fp.write('\n')
        messagebox.showinfo("提醒","导出文件成功")#再利用message.showinfo()函数输出操作成功

    def brrow_book(self):#自定义借书模块
        title = tk.simpledialog.askstring("添加图书", "请输入图书标题")  # 1.使用tk.simpledialog.askstring("", "") 函数输入要借用的书籍的书名
        #使用for循环对图书列表进行遍历，若存在符合输入的书名，则利用列表的remove()方法删除该书籍
        for book in self.books:
            if title==book['标题']:
                messagebox.showinfo("提醒","成功借出图书")#再利用message.showinfo()函数输出操作成功
                self.books.remove(book)
                #再依次引用已经自定义好的def output_file(self)以及def input_file(self)函数对后台进行操作。
                self.load_books()#调用自定义函数self.load_books()对列表框进行清洗。
                with open("书籍文件.txt", "w+", encoding='utf-8') as fp:
                    for book in self.books:
                        book_title = book['标题']
                        book_date = book['出版时间']
                        book_author1 = book['作者']
                        book_author2 = book_author1.replace('\n', '')
                        fp.write(book_title)
                        fp.write(' ')
                        fp.write(book_date)
                        fp.write(' ')
                        fp.write(book_author2)
                        fp.write('\n')
                with open("书籍文件.txt", 'r+', encoding='utf-8') as fp:
                    content = fp.readlines()
                for lines in content:
                    line = lines.split(' ')
                    self.books.append({'标题': line[0], '出版时间': line[1], '作者': line[2]})
                break#使用break退出for循环
        else:
            messagebox.showinfo("提醒","无相关书籍")#否则，再利用message.showinfo()函数输出操作失败

    def back_book(self):#自定义归还图书模块
        title = tk.simpledialog.askstring("添加图书", "请输入图书标题")#输入图书标题
        date = tk.simpledialog.askstring("添加图书", "请输入图书出版时间")#输入图书出版时间
        author = tk.simpledialog.askstring("添加图书", "请输入图书作者")#输入图书作者
        if title and date and author:#如果三个元素都存在
            self.books.append({"标题": title, "出版时间":date,"作者": author})#将book以字典的形式（键值对）写入books列表中即为[{},{},{}]
            messagebox.showinfo("提示", "图书归还成功")#再利用message.showinfo()函数输出操作成功
            #引用def input_file(self)以及def ouput_file(self)函数对后台进行操作。
            with open("书籍文件.txt", "w+", encoding='utf-8') as fp:
                for book in self.books:
                    book_title = book['标题']
                    book_date = book['出版时间']
                    book_author1 = book['作者']
                    book_author2 = book_author1.replace('\n', '')
                    fp.write(book_title)
                    fp.write(' ')
                    fp.write(book_date)
                    fp.write(' ')
                    fp.write(book_author2)
                    fp.write('\n')
            with open("书籍文件.txt", 'r', encoding='utf-8') as fp:
                content = fp.readlines()
            for lines in content:
                line = lines.split(' ')
                self.books.append({'标题': line[0], '出版时间': line[1], '作者': line[2]})
            self.load_books()
        else:
            messagebox.showinfo("提示", "图书归还失败")#否则，使用message.showinfo(“”,””)函数提醒操作失败。

if __name__=='__main__':
    root=tk.Tk()#对root赋值
    system = LibrarySystem(root)#实例化对象
    root.mainloop()#不断循环