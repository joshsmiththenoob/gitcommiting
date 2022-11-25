# 資料形式

a = "123"   # string字串形式
b = 123     # 輸入數值時，python會以目前數值型態給予適當的資料形式ex:123的資料形式為int(整數)
# 使用type 查看各個變數的資料形式
print(type(a),type(b))

# 資料形式 : 1. int:integer 整數 2. float:浮點數 (擁有小數的數值) 3.string: 字串(可放文字等不用處理的資料→讓自己看懂!)
# int(),float()將資料型態轉換為整數、浮點數
print(float(777),type(float(777)))
print(int(8.6),type(int(8.6)))        # 如果浮點數8.6轉換為整數時，會直接將小數點後的數值排除，只剩整數
print(str(888.888),type(str(888.888)))   # 當然，也可以將整數、浮點數轉換為字串的資料形式
# """ """:三個冒號可使用多行字串
print(""""Hello worlds 
I am josh""")


# 二進位、八進位、十六進位
# 二進位binary(使用數字0、1表示)，數值前面加上0b已表示此數值為二進位
# 八進位octal(使用數字0~7表示)，數值前面加上0o已表示此數值為二進位
# 十六進位hexadecimal(使用數字0~9,A~F表示)，數值前面加上0x已表示此數值為二進位 (記憶體!!)

# 十進位不用說了吧?
# 進位制的轉換
a=10
print(int(a))       #十進位可單純用整數資料型態表示
print(bin(a))       #將變數a的數值轉換為二進位進制
print(oct(a))       #將變數a的數值轉轉換為八進位進制
print(hex(a))       #將變數a的數值轉轉換為十六進位進制


#\的作用
print("adsf\'")                     # \':在字串內顯示單引號(避免與字串資料形式的引號混淆)
print("adfasdf \n I\'m Josh")       #\n:換行
print("adfs\t adsf")                # \t:使用tab做縮排→做間隔
print("adf\\ adsf")                 #\\:印出\

print("adsf",end="\n")                #在預設的情況下，print後面還有end=\n→自動換行執行下一列程式
print("test")

# 可以改變 print內語法end的資料→決定印出資料後進行什麼步驟(其實目前沒什麼用)
print("I\'m Josh", end="\t")         #結尾後面加上tab 縮排
print("Hello", end=",")
print("Lisa", end=".")
print(end="\n")


# Variable 變數 : 除了英文，不可以"數字"為開頭，使用特殊字元以及特殊語法的名稱
coffee_price = 30
print("咖啡價格:\t", coffee_price, "元/杯")

product_name = "coffee"                     # 將字串資料"coffee" 指定給變數 product_name
product_price = 100                         # 將數值資料100 指定給變數product_price

# print("產品名稱:", product_name, "產品價格:", product_price)
print(type(product_name),type(product_price))

# 數值、變數的運算
c=8+9
# 運算子範例
c=15/2                         # 除法
print(c)
c=15//2                        # 除後得出的"商數"
print(c)
c=15%2                         # 除後得出的"餘數" (相當於matlab中的mod())
print(c)
c=15**2                        # 指數運算 (相當於matlab中的15^2)
print(c)

# 判斷(比較)運算子
print(15==2)                   # "="是指定變數一個數值(資料)，"=="→判斷左右數值是否相等
print(15!=2)                   # "!="→判斷兩邊數值是否"不相等"
print(15>2)
print(15>=2)
print(15<2)
print(15<=2)
print("-"*20)
# 邏輯運算子 and or not
T = True
F = False
print(T and F)               # 是否同時符合 T、F
print(T or F)
print(not T)
print(not F)

# !!!id 可顯示儲存該變數的"記憶體位置(地址)"!!!
a = 1000
b = 1000
print(id(a))
print(id(b))
# !!!python 會自動將數值1000放在一個記憶體位址並使變數a、b指向數值1000→∴記憶體位置相同!!!

# 身分運算子is;is not:使用記憶體位置，判斷資料是否相等
print(a is b)                                      # a與b變數使用的記憶體位置相同(∵都是同一個數值1000，數值1000只占用一個記憶體空間，並指向變數a、b)
print(a is not b)
print(T is True)
print(T is not True)

# 聯集 交集 差集
# 集合Set :可改變、沒有順序的列表
a={1,2,3}
b={3,4,5}
print(a&b)    #交集:a、b均有的資料 :and
print(a|b)    #聯集:a、b全部的資料 :or
print(a^b)    #除了共有資料之外,a、b所有資料 :xor

# 指定運算子 +=、-=
a=10
b=2
a=a+b
print(a)
a=10
b=2
a+=b          # a+=b → a=a+b
print(a)

# 字串間的運算
a="Hello"+"Taiwan"
print(a)
# a = 100+"Hello" # Error! 錯誤! 數值不可以與字串相加!
a = "Hello"*5
print(a)

# 由鍵盤輸入字串:input()
# input("描述的文字"):給使用者輸入資料，且資料形式為!!字串形式!!

x = input("請輸入密碼:")       # 系統告訴使用者"請輸入密碼"，讓使用者輸入的密碼為變數x，其資料形式為!!字串形式!!
print(x,type(x))

# x = int(input("請輸入價格:"))  # 可以使用int將資料格式轉成整數
# print(x,type(x))
#
# x = float(input("請輸入價格:"))  # 可以使用float將資料格式轉成浮點數
# print(x,type(x))



price = int(input("請輸入價格"))
# 因為故意輸入文字時會出現錯誤，所以之嘔可以加入try..except的概念(之後會教)
discount = float(input("請輸入打折資訊"))
total_price=price*discount
print("總價",total_price,type(total_price))