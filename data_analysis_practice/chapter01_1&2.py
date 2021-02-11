#!/usr/bin/env python
# coding: utf-8

# ## 01 데이터에서 인사이트 발견하기

# ### 1.1 탐색적 데이터 분석의 과정

# #### 데이터와의 첫 만남

# raw data : 아직 분석에 활용된 적이 없는 혹은 정제되지 않은 데이터
# 
# 탐색적 데이터 분석은 데이터를 열어보는 상황에서부터 시작되며 다음과 같은 과정 수행
# 
#     1. 데이터의 출처와 주제에 대해 이해합니다.
#     2. 데이터의 크기를 알아봅니다.
#     3. 데이터의 구성 요소(피처)를 살펴봅니다.

# #### 데이터의 속성 탐색하기

# - 피처의 속성 탐색
# 
#     가장 중요한 것은 '데이터에 질문을 던지는 것'. 피치의 속성 탐색은 '우리 반의 평균 키는 몇이나 될까?'와 같은 질문에서부터 출발하기 때문
# 
# 
# 
# - 피처 간의 상관 관계 탐색
# 
#     학급의 신체검사 데이터를 살펴봄 -> '우리 학급은 비만이 아닐까?' -> '몸무게' 피처 살펴봄 -> 가정 확인
#     
#     but, 몸무게는 키와도 관계가 있음 -> 이런 상황에서 필요한 것이 피처 간의 상관 관계 탐색
#     
#     피처 간의 공분산, 혹은 상관 계수와 같은 개념 포함

# #### 탐색한 데이터의 시각화

# 데이터 시각화는 수치적 자료만 가지고는 파악하기 힘든 패턴이나 인사이트를 발현하는 데 유용

# ### 1.2 멕시코풍 프랜차이즈 chipotle의 주문 데이터 분석하기

# #### Step1. 탐색 : 데이터의 기초 정보 살펴보기

# ##### chipotle 데이터셋의 기초 정보 출력하기

# In[31]:


import pandas as pd

file_path = 'python-data-analysis-master/data/chipotle.tsv'
# read_csv() 함수로 데이터를 데이터 프레임 형태로 불러옵니다.
chipo = pd.read_csv(file_path, sep = '\t')

print(chipo.shape) # shape : 데이터의 행과 열의 크기를 반환
print("-----------------------------")
print(chipo.info()) # info() : 행과 열의 구성 정보


## '../data/...' 에서 맨 앞의 ..은 한 폴더 위 라는 의미


# ##### chipotle 데이터셋의 행과 열, 데이터 확인하기

# In[32]:


# chipo라는 데이터 프레임에서 순서대로 10개의 데이터를 보여줍니다.
chipo.head(10)


# In[33]:


print(chipo.columns)
print("-------------------------------------")
print(chipo.index)


# order_id : 주문 번호
# 
# quantity : 아이템의 주문 수량
# 
# item_name : 주문한 아이템의 이름
# 
# choice_description : 주문한 아이템의 상세 선택 옵션
# 
# item_price : 주문 아이템의 가격 정보

# ##### quantity와 item_price의 수치적 특징

# quantity와 item_price는 연속성 피처(키와 몸무게처럼 어떠한 값도 가질 수 있는 연속적인 숫자 형태)
# 
# describe() : 피처의 기초 통계량
# 
# but, 현재 유일한 수치형 피처는 quantity 뿐이기 때문에 오직 quantity에 대한 정보만을 출력할 수 있음

# ##### describe() 함수로 기초 통계량 출력하기

# In[34]:


# order_id는 숫자의 의미를 가지지 않기 때문에 str으로 변환합니다.
chipo['order_id'] = chipo['order_id'].astype(str)
print(chipo.describe()) # chipo 데이터 프레임에서 수치형 피처들의 기초 통계량을 확인합니다.


# 평균 주문 수량(mean)은 약 1.07
# 
# -> 대부분이 한 아이템에 대해서 1개 정도만 주문했다는 것이고, '한 사람이 같은 메뉴를 여러 개 구매하는 경우는 많지 않다.'는 인사이트를 얻을 수 있음

# 그렇다면 item_price의 수치적 특징은 어떻게 알아볼 수 있을까?
# 
# 현재 item_price 피처는 object 타입이기 때문에 describe() 함수로 기초 통계량을 확인할 수 없음
# 
# 따라서 추가적인 데이터 전처리 작업이 필요

# ##### order_id와 item_name의 개수

# order_id와 item_name의 개수 탐색
# 
# 두 피처는 범주형 피처이기 때문에 unique() 함수 사용

# ##### unique() 함수로 범주형 피처의 개수 출력하기

# In[35]:


print(len(chipo['order_id'].unique())) # order_id의 개수를 출력합니다.
print(len(chipo['item_name'].unique())) # item_name의 개수를 출력합니다.


# #### Step2. 인사이트의 발견 : 탐색과 시각화하기

# ##### 가장 많이 주문한 아이템 Top 10 출력하기

# In[36]:


# 가장 많이 주문한 아이템 Top 10을 출력합니다.
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(), 1) :
    print("Top", idx, ":", val, cnt)

    
## iteritems() : 행 번호와 값을 출력


# ##### 아이템별 주문 개수와 총량 구하기

# In[37]:


# 아이템별 주문 개수를 출력합니다.
order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10] # 아이템별 주문 개수를 출력합니다.


# groupby() : 데이터 프레임에서 특정 피처를 기준으로 그룹을 생성하며 이를 통해 그룹별 연산을 적용
# 
# 예를 들어 '학급'이라는 그룹을 만들었을 때, '학급별 평균 키', '학급별 평균 몸무게' 등을 구하는 것

# In[38]:


# 아이템별 주문 총량을 출력합니다.
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10] # 아이템별 주문 총량을 출력합니다.


# #### 시각화

# ##### 시각화로 분석 결과 살펴보기

# In[39]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos, order_cnt, align = 'center')
plt.ylabel('ordered_item_count')
plt.title('Distribution of all ordered item')

plt.show()

# 주문 총량 - item_quantity.values.tolist()


# ### Step3. 데이터 전처리 : 전처리 함수 사용하기

# ##### item_price 피처 살펴보기

# 앞선 내용의 item_price의 수치적 특징을 탐색하는 과정에서 우리는 item_price 피처의 요약 통계를 구할 수 없었다.
# 
# 이는 item_price 피처가 문자열 타입이었기 때문이다.
# 
# 따라서 이러한 데이터를 전처리 하는 방법에 대해 알아보자.

# In[40]:


print(chipo.info())
print("---------------------")
chipo['item_price'].head()


# item_price 피처를 살펴본 결과, 가격을 나타내는 숫자 앞에 '$' 기호가 붙어있다.
# 
# 따라서 이 기호를 제거해주는 전처리 작업을 해보자.

# ##### apply()와 lambda를 이용해 데이터 전처리하기

# In[41]:


# column 단위 데이터에 apply() 함수로 전처리를 적용합니다.
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
chipo.describe()

# apply(lambda x: float(x[1:])) : item_price 내의 내용을 1부터 저장
# 0에는 '$'가 저장되어있기 때문


# ### Step4. 탐색적 분석 : 스무고개로 개념적 탐색 분석하기

# ##### 주문당 평균 계산 금액 출력하기

# In[42]:


# 주문당 평균 계산금액을 출력합니다.
chipo.groupby('order_id')['item_price'].sum().mean()


# ##### 한 주문에 10달러 이상 지불한 주문 번호(id) 출력하기

# In[46]:


# 한 주문에 10달러 이상 지불한 id를 출력합니다.

chipo_orderid_group = chipo.groupby('order_id').sum()
# order_id 피처를 기준으로 그룹 생성
# quantity, item_price 피처의 합계 계산

results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]
# 10 이상인 값을 필터링 후, results에 저장

print(results[:10])
print(results.index.values)


# ##### 각 아이템의 가격 구하기

#     1. chipo[chipo.quantity == 1]으로 동일 아이템을 1개만 구매한 주문을 선별합니다.
#     2. item_name을 기준으로 groupby 연산을 수행한 뒤, min() 함수로 각 그룹별 최저가를 계산합니다.
#     3. item_price를 기준으로 정렬하는 sort_values() 함수를 적용합니다. sort_values()는 series 데이터를 정렬해주는 함수입니다.

# In[48]:


# 각 아이템의 가격을 계산합니다.
chipo_one_item = chipo[chipo.quantity == 1] # 1
price_per_item = chipo_one_item.groupby('item_name').min() # 2
price_per_item.sort_values(by = "item_price", ascending = False)[:10] # 3


# In[49]:


# 아이템 가격 분포 그래프를 출력합니다.
item_name_list = price_per_item.index.tolist()
x_pos = np.arange(len(item_name_list))
item_price = price_per_item['item_price'].tolist()

plt.bar(x_pos, item_price, align = 'center')
plt.ylabel('item price($)')
plt.title('Distribution of item price')
plt.show()

# 아이템 가격 히스토그램을 출력합니다.
plt.hist(item_price)
plt.ylabel('counts')
plt.title('Histogram of item price')
plt.show()


# ##### 가장 비싼 주문에서 아이템이 총 몇 개 팔렸는지 구하기

# In[50]:


# 가장 비싼 주문에서 아이템이 총 몇 개 팔렸는지 구하기
chipo.groupby('order_id').sum().sort_values(by='item_price', ascending = False)[:5]


# ##### 'Veggie Salad Bowl'이 몇 번 주문되었는지 구하기

# In[52]:


# 'Veggie Salad Bowl'이 몇 번 주문되었는지를 계산합니다.
chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
# 한 주문 내에서 중복 집계된 item_name을 제거합니다.
chipo_salad = chipo_salad.drop_duplicates(['item_name', 'order_id'])
# drop_duplicates : 한 주문 내에서 item_name이 중복 집계된 경우를 제거해주기 위함

print(len(chipo_salad))
chipo_salad.head(5)


# ##### 'Chicken Bowl'을 2개 이상 주문한 주문 횟수 구하기

# In[53]:


# 'Chicken Bowl'을 2개 이상 주문한 주문 횟수를 구합니다.
chipo_chicken = chipo[chipo['item_name'] == "Chicken Bowl"]
chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']
chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]

print(len(chipo_chicken_result))
chipo_chicken_result.head(5)

