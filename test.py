# มีลิสต์ s ที่เป็นลิสต์ของสตริง ให้หาความยาวเฉลี่ยของสตริงใน s เก็บในตัวแปรชื่อ avg_len
import re

texts = []
num_re = re.compile(r'\d{2,3}')
with open("youtube.txt",'r', encoding = 'utf-8') as f:
    for line in f:
        if re.match(r'อายุ|ม\.', line):
            found = num_re.findall(line)
            if len(found) > 1:
                texts.append(line)

print(len(texts))
with open("result.txt",'w', encoding = 'utf-8') as f:
    for line in texts:
        f.write(line)