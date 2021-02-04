#!/usr/bin/env python
# coding: utf-8

# ## 15 테이블 형태의 데이터를 쉽게 다루도록 도와주는 pandas 라이브러리

# ### (1) 위키피디아 데이터 엑셀로 저장하기

# In[2]:


import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
print(df)


# In[3]:


import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table')
df[1]


# In[4]:


import pandas as pd
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table',
                 header = 0, index_col = 0)
df[1]


# In[19]:


# 데이터 중 하계올림픽에 대한 데이터만 추출
summer = df[1].iloc[1:,:5]
summer


# In[20]:


summer.columns = ['경기수', '금', '은', '동', '계']
print(summer)


# In[21]:


print(summer.sort_values('금', ascending=False))


# In[22]:


summer.to_excel('하계올림픽메달.xlsx')


# ### (2) 데이터 프레임 기초

# In[23]:


import pandas as pd
index = pd.date_range('1/1/2000', periods=8)
print(index)


# In[24]:


import numpy as np
df = pd.DataFrame(np.random.rand(8,3), index = index, columns=list('ABC'))
df


# In[26]:


import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B'])


# In[27]:


import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B'] > 0.4)


# In[28]:


df2 = df[df['B'] > 0.4]
df2


# In[29]:


import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B'] # A열의 값을 B열의 값으로 나눈 값을 D열에 저장
df


# In[30]:


import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis=1) # 행 우선 계산 값을 E열에 저장
df.head()

# 열 방향(axis=1)
# 행 방향(axis=0)


# In[31]:


import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis=1)
df = df.sub(df['A'], axis=0) # A열의 데이터를 기준으로 열 우선 계산
df.head()


# In[34]:


import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis=1)
df = df.sub(df['A'], axis=0)
df = df.div(df['C'], axis=0) # C열 데이터를 기준으로 열 우선 계산
df.to_csv('test.csv') # 데이터 프레임을 test.csv 파일로 저장
df.head()


# ### (4) pandas로 인구 구조 분석하기

# 1. 데이터 읽어오기

# In[36]:


import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df.head()


# In[1]:


import pandas as pd
df = pd.read_csv('age.csv', encoding='cp949', index_col=0)
df = df.div(df['총인구수'], axis=0) # 1 | 전체 데이터를 총인구수로 나눠서 비율로 변환
del df['총인구수'], df['연령구간인구수']# 2 | 총인구수, 연령구간인구수 열 삭제


# 2~3. 궁금한 지역 이름을 입력받고 해당 지역의 인구 구조 저장하기

# In[2]:


name = input('원하는 지역의 이름을 입력해주세요 : ') # 2 | 지역 이름 입력
a = df.index.str.contains(name) # 3 | 해당 행을 찾아서 해당 지역의 인구 구조를 저장
df2 = df[a]
df2


# In[4]:


import matplotlib.pyplot as plt
plt.rc('font', family = 'Malgun Gothic')
df2.T.plot()
plt.show()


# 4~5. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역 시각화하기

# In[5]:


import numpy as np
# 4 | 궁금한 지역 A의 인구 비율에서 B의 인구 비율을 뺀다.
x = df.sub(df2.iloc[0], axis=1)
# 4 | A의 인구 비율에서 B의 인구 비율을 뺀 값의 제곱 값을 모두 더한다.
y = np.power(x, 2)
z = y.sum(axis=1)


# In[7]:


i = z.sort_values().index[:5] # 4 | 그 차이가 가장 작은 지역 5곳을 찾는다.


# In[8]:


df.loc[i].T.plot() # 4 | 결과를 꺾은선 그래프로 보여준다.
plt.show()


# In[9]:


# 4 | 궁금한 지역 A의 인구 비율에서 B의 인구 비율을 뺀다.
x = df.sub(df2.iloc[0], axis=1)
# 4 | A의 인구 비율에서 B의 인구 비율을 뺀 값의 제곱값을 모두 더한다.
y = np.power(x, 2)
z = y.sum(axis=1)
i = z.sort_values().index[:5] # 4 | 그 차이가 가장 작은 지역 5곳을 찾는다.
df.loc[i].T.plot() # 4 | 결과를 꺾은선 그래프로 보여준다.


# #### 우리 동네와 인구 구조와 비슷한 지역들을 그래프로 나타내기(pandas 사용)

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family = 'Malgun Gothic')
df = pd.read_csv('age.csv', encoding = 'cp949', index_col=0)
df = df.div(df['총인구수'], axis=0)
del df['총인구수'], df['연령구간인구수']

name = input('원하는 지역의 이름을 입력해주세요 : ')
a = df.index.str.contains(name)
df2 = df[a]

df.loc[np.power(df.sub(df2.iloc[0], axis=1), 2).sum(axis=1).sort_values().index[:5]].T.plot()

plt.show()

