print("Hello World")
print("莎士比亚说；\"to be or not to be,that\'s the question\"")
print("2024""2025""2026")
print("2024","2025","2026")
print("2024","2025","2026",sep="->")
print("2024","2025","2026",end="->")
print("2027","2028","2029")
print("蒹葭苍苍\n白露为霜")
print(r"蒹葭苍苍\n白露为霜")
print('''
a
 b 
  c
   d 
    e''')
print("Python")
print("\tpython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#删除空格
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())#删除右端空格
print(favorite_language.lstrip())#删除左端空格
print(favorite_language.strip())#删除两端空格

#删除前缀
web="https://123456.com"
print(web)
print(web.removeprefix('https://') )