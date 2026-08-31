#创建一个demo文档并写入
# 蒹葭
# 蒹葭苍苍,白露为霜。
# 所谓伊人,在水一方。

with open('demo.txt','w' , encoding='utf-8') as f:
    f.write('蒹葭\n')
    f.write('蒹葭苍苍,白露为霜。\n')
    f.write('所谓伊人,在水一方。\n')

#追加模式下写入
# 溯洄从之,道阻且长。
# 溯游从之,宛在水中央。

with open('demo.txt', 'a+', encoding='utf-8') as f:
    f.write('溯洄从之,道阻且长。\n')
    f.write('溯游从之,宛在水中央。\n')
    f.seek(0)
    print(f.read())