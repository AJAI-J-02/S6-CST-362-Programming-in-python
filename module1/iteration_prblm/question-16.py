# Generate the numbers between 100 and 200 which are divisible by 3 but not divisible by 4

for i in range(100,201):
    if i%3==0 and i%4!=0:
        print(i)


'''
ouput

102
105
111
114
117
123
126
129
135
138
141
147
150
153
159
162
165
171
174
177
183
186
189
195
198

'''