# 文字列型

fruit = 'apple'
print(fruit)
print(type(fruit))

print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[-1])

# encode, decode => bytes[]

byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))

# count

msg = 'ABCDEABC'
print(msg.count('ABCDEF'))

# starswith, endswith

print(msg.startswith('ABCECF'))
print(msg.endswith('F'))

# strip(両端), rstrip(右端), lstrip(左端)

msg = ' ABC '
print(msg)
print(msg.strip())

msg = 'ABCDEFABC'
print(msg.strip('C'))
print(msg.strip('CBA'))
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))

# upper, lower, swapcase, replace, capitalize

msg = 'abcABC'
msg_u = msg.upper() # 大文字
msg_l = msg.lower() # 小文字
msg_s = msg.swapcase() # 大文字小文字入れ替え
print(msg_u, msg_l, msg_s)

msg = 'ABCEABC'
msg_r = msg.replace('ABC', 'FFF')
print(msg_r)

msg_r = msg.replace('ABC', 'FFF', 1)
print(msg_r)

msg_r = msg.replace('ABC', 'FFF', -1) # デフォルトですべて変換
print(msg_r)

msg = 'hello world'
print(msg.capitalize())

# 文字列の一部取り出し、fromat, islower, isupper

msg = 'hello, my name is taro'
print(msg[:5])
print(msg[:6])
print(msg[6:])
print(msg[1:6])
print(msg[1:10:2])
print(msg[1:10:3])

print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}') # 3.6以上
print(f'{name=}') #3.8以上 デバッグなどで使える

msg = 'APPLE'
print(msg.islower())
print(msg.isupper())

msg = 'ABCDEABC'
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE'))
print(msg.index('ABCE'))
