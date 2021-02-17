#!/usr/bin/env python
# coding: utf-8

# ## 01 데이터에서 인사이트 발견하기

# ### 1.3 국가별 음주 데이터 분석하기

# #### STEP 1. 탐색 : 데이터의 기초 정보 살펴보기

# ##### drinks 데이터셋의 기초 정보 출력하기

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'python-data-analysis-master/data/drinks.csv'
drinks = pd.read_csv(file_path) # read_csv() 함수로 데이터를 데이터 프레임 형태로 불러옵니다.
print(drinks.info())
drinks.head(10)


# * contry : 국가 정보
# * beer_servings : beer 소비량
# * spirit_servings : spirit 소비량
# * wine_servings : wine 소비량
# * total_litres_of_pure_alcohol : 총 알코올 소비량
# * continent : 국가의 대륙 정보

# In[2]:


drinks.describe()


# #### STEP 2. 인사이트의 발견 : 탐색과 시각화하기

# ##### 두 피처 간의 상관 계수 구하기

# In[3]:


# beer_servings, wine_servings 두 피처 간의 상관 계수를 계산합니다.
# pearson은 상관 계수를 구하는 계산 방법 중 하나를 의미하며, 가장 널리 쓰이는 방법입니다.
corr = drinks[['beer_servings', 'wine_servings']].corr(method='pearson')
print(corr)


# ##### 여러 피처의 상관 관계 분석하기

# In[4]:


# 피처 간의 상관 계수 행렬을 구합니다.
cols = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
corr = drinks[cols].corr(method = 'pearson')
print(corr)


# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt

# corr 행렬 히트맵을 시각화합니다.
cols_view = ['beer', 'spirit', 'wine', 'alcohol'] # 그래프 출력을 위한 cols 이름을 축약합니다.
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values,
                cbar = True,
                annot = True,
                square = True,
                fmt = '.2f',
                annot_kws = {'size': 15},
                yticklabels = cols_view,
                xticklabels = cols_view)

plt.tight_layout()
plt.show()

# 시각화 라이브러리를 이용한 피처 간의 산점도 그래프를 출력합니다.
sns.set(style = "whitegrid", context='notebook')
sns.pairplot(drinks[['beer_servings', 'spirit_servings',
                    'wine_servings', 'total_litres_of_pure_alcohol']], height = 2.5)
plt.show()


# #### STEP 3. 탐색적 분석 : 스무고개로 개념적 탐색 분석하기

# ##### 결측 데이터 전처리하기

# In[6]:


# 결측 데이터를 처리합니다: 기타 대륙으로 통합 -> 'OT'
drinks['continent'] = drinks['continent'].fillna('OT')
drinks.head(10)


# ##### 파이차트로 시각화하기

# In[7]:


labels = drinks['continent'].value_counts().index.tolist()
fracs1 = drinks['continent'].value_counts().values.tolist()
explode = (0, 0, 0, 0.25, 0, 0)

plt.pie(fracs1, explode=explode, labels=labels, autopct='%.0f%%', shadow=True)
plt.title('null data to \'OT\'')
plt.show()


# In[8]:


drinks['continent'].value_counts().index.tolist()


# In[9]:


drinks['continent'].value_counts().values.tolist()


# #### 대륙별 spirit_servings의 통계적 정보는 어느 정도일까?

# ##### agg() 함수를 이용해 대륙별로 분석하기

# In[10]:


# 대륙별 spirit_serving의 평균, 최소, 최대, 합계를 계산합니다.
result = drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max', 'sum'])
result.head()


# agg() 함수는 apply() 함수와 거의 동일한 기능을 한다.
# 
# 다만 agg() 함수는 apply()에 들어가는 함수 파라미터를 병렬로 설정하여 그룹에 대한 여러 가지 연산 결과를 동시에 얻을 수 있는 함수이다.

# #### 전체 평균보다 많은 알코올을 섭취하는 대륙은 어디일까?

# In[11]:


# 전체 평균보다 많은 알코올을 섭취하는 대륙을 구합니다.
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()
continent_over_mean = continent_mean[continent_mean >= total_mean]
print(continent_over_mean)


# 전체 평균보다 많은 알코올을 섭취하는 대륙을 탐색할 때는 apply()나 agg() 함수 없이도 mean() 함수만을 이용한 탐색을 수행할 수 있다.

# #### 평균 beer_servings가 가장 높은 대륙은 어디일까?

# In[12]:


# 평균 beer_servings가 가장 높은 대륙을 구합니다.
beer_continent = drinks.groupby('continent').beer_servings.mean().idxmax()
print(beer_continent)


# #### 시각화

# ##### 분석 결과를 시각화하기

# In[13]:


# 대륙별 spirit_servings의 평균, 최소, 최대, 합계를 시각화합니다.
n_groups = len(result.index)
means = result['mean'].tolist()
mins = result['min'].tolist()
maxs = result['max'].tolist()
sums = result['sum'].tolist()

index = np.arange(n_groups)
bar_width = 0.1

rects1 = plt.bar(index, means, bar_width, color='r', label='Mean')
rects2 = plt.bar(index + bar_width, mins, bar_width, color='g', label='Min')
rects3 = plt.bar(index + bar_width * 2, maxs, bar_width, color='b', label='Max')
rects4 = plt.bar(index + bar_width * 3, sums, bar_width, color='y', label='Sum')

plt.xticks(index, result.index.tolist())
plt.legend()
plt.show()


# In[14]:


# 대륙별 total_litres_of_pure_alcohol을 시각화합니다.
continents = continent_mean.index.tolist()
continents.append('mean')
x_pos = np.arange(len(continents))
alcohol = continent_mean.tolist()
alcohol.append(total_mean)

bar_list = plt.bar(x_pos, alcohol, align='center', alpha=0.5)
bar_list[len(continents) - 1].set_color('r')
plt.plot([0., 6], [total_mean. total_mean], "k--")
plt.xticks(x_pos, continents)

plt.ylabel('total_litres_of_pure_alcohol')
plt.title('total_litres_of_pure_alcohol by Continent')

plt.show()


# In[15]:


# 대륙별 beer_servings를 시각화합니다.
beer_group = drinks.groupby('continent')['beer_servings'].sum()
continents = beer_group.index.tolist()
y_pos = np.arange(len(continents))
alcohol = beer_group.tolist()

bar_list = plt.bar(y_pos, alcohol, align = 'center', alpha=0.5)
bar_list[continents.index("EU")].set_color('r')
plt.xticks(y_pos, continents)
plt.ylabel('beer_servings')
plt.title('beer_servings by Continent')

plt.show()


# In[16]:


result['mean'].tolist()


# In[17]:


result['min'].tolist()


# In[18]:


result['max'].tolist()


# In[19]:


result['sum'].tolist()


# #### STEP 4. 통계적 분석 : 분석 대상 간의 통계적 차이 검정하기

# ##### 아프리카와 유럽 간의 맥주 소비량 차이 검정하기

# In[20]:


# 아프리카와 유럽 간의 맥주 소비량 차이를 검정합니다.
africa = drinks.loc[drinks['continent']=='AF']
europe = drinks.loc[drinks['continent']=='EU']

from scipy import stats
tTestResult = stats.ttest_ind(africa['beer_servings'], europe['beer_servings'])
tTestResultDiffVar = stats.ttest_ind(africa['beer_servings'],
                                    europe['beer_servings'], equal_var=False)

print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f." % tTestResultDiffVar)


# ##### '대한민국은 얼마나 술을 독하게 마시는 나라일까?'에 대한 탐색 코드 살펴보기

# In[21]:


# total_servings 피처를 생성합니다.
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 술 소비량 대비 알코올 비율 피처를 생성합니다.
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

# 순위 정보를 생성합니다,
country_with_rank = drinks[['country', 'alcohol_rate']]
country_with_rank = country_with_rank.sort_values(by=['alcohol_rate'], ascending = 0)
country_with_rank.head(5)


# ##### 국가별 순위 정보를 시각화하기

# In[22]:


# 국가별 순위 정보를 그래프로 시각화합니다.
country_list = country_with_rank.country.tolist()
x_pos = np.arange(len(country_list))
rank = country_with_rank.alcohol_rate.tolist()

bar_list = plt.bar(x_pos, rank)
bar_list[country_list.index("South Korea")].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by country')
plt.axis([0, 200, 0, 0.3])

korea_rank = country_list.index("South Korea")
korea_alc_rate = country_with_rank[country_with_rank['country'] == 'South Korea']['alcohol_rate'].values[0]
plt.annotate('South Korea : ' + str(korea_rank - 1),
            xy = (korea_rank, korea_alc_rate), 
            xytext = (korea_rank + 10, korea_alc_rate + 0.05), # 텍스트 위치
            arrowprops = dict(facecolor='red', shrink=0.05)) # 화살표

plt.show()


# ### 연습 문제

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'python-data-analysis-master/data/drinks.csv'
# read_csv() 함수로 데이터를 데이터 프레임 형태로 불러옵니다.
drinks = pd.read_csv(file_path)
drinks['continent'] = drinks['continent'].fillna('OT')


# 1) 대륙별 평균 wine_servings를 탐색합니다.

# In[24]:


# 대륙별 평균 wine_servings 피처를 만들어서 병합합니다.
result = drinks.groupby('continent').mean()['wine_servings']
df = result.to_frame().reset_index()
df = df.rename(columns={'wine_servings': 'wine_servings_cont_avg'})
drinks = pd.merge(drinks, df, on='continent', how='outer')

# 위와 같은 방법의 코드입니다.
drinks['wine_servings_cont_avg'] = drinks.groupby('continent')['wine_servings'].transform(np.mean)

# 결과를 출력합니다.
drinks[['country', 'continent', 'wine_servings_cont_avg']].sample(5).head()


# 2) 국가별 모든 servings의 합을 계산한 total_servings 라는 피처를 생성합니다.

# In[25]:


# 국가별 total_servings 피처를 만들어서 병합합니다.
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 결과를 출력합니다.
drinks[['country', 'beer_servings', 'wine_servings', 'spirit_servings', 'total_servings']].sample(5).head()


# 3) 전체 평균보다 적은 알코올을 마시는 대륙 중, spirit를 가장 많이 마시는 국가를 찾아봅니다.

# In[27]:


# 전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit를 가장 많이 마시는 국가를 구합니다.
total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_under_mean = continent_mean[continent_mean <= total_mean].index.tolist()
df_continent_under_mean = drinks.loc[drinks.continent.isin(continent_under_mean)]

most_spirit_under_mean = df_continent_under_mean.loc[df_continent_under_mean['spirit_servings'].idxmax()]

# 결과를 출력합니다.
most_spirit_under_mean['country']


# 4) 술 소비량 대비 알코올 비율을 구해봅니다.

# In[31]:


# 술 소비량 대비 알코올 비율에 대한 칼럼을 만들어서 병합합니다.
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

# 술 소비량 대비 알코올 비율 : 전체 순위 중 한국의 순위를 구합니다.
drinks['alcohol_rate_rank'] = drinks['alcohol_rate'].rank(ascending=False)
drinks['alcohol_rate_rank'] = drinks['alcohol_rate_rank'].apply(np.floor)
drinks.loc[drinks['country'] == 'South Korea'].alcohol_rate_rank


# 5) 대륙별로 술 소비량 대비 알코올 비율을 계산합니다.

# In[35]:


# 내가 푼거
result = drinks.groupby('continent').mean()['alcohol_rate']
df = result.to_frame().reset_index()

drinks[['continent', 'alcohol_rate']].sample(5).head()


# In[42]:


# 답

# 대륙별 술 소비량 대비 알코올 비율을 구합니다.
continent_sum = drinks.groupby('continent').sum()
continent_sum['alcohol_rate_continent'] = continent_sum['total_litres_of_pure_alcohol'] / continent_sum['total_servings']
continent_sum = continent_sum.reset_index()
continent_sum = continent_sum[['continent', 'alcohol_rate_continent']]

drinks = pd.merge(drinks, continent_sum, on='continent', how='outer')

# 결과를 출력합니다.
drinks[['country', 'continent', 'alcohol_rate_continent']].sample(5).head()

